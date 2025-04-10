from typing import TYPE_CHECKING, List, Any, Dict
import jinja2
from pathlib import Path

# Local application/library specific imports
from ..base import WorkflowBase # Changed import path
from geometor.seer.prompts import get_pair_prompt # Keep for formatting pair data
from geometor.seer.session.task_step import TaskStep
from geometor.seer.trials.code_trial import CodeTrial

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task


class DefaultWorkflow(WorkflowBase):
    """
    Implements the standard investigate-all-pairs then refine workflow using
    Jinja2 templates for prompts loaded from the package.
    """

    def __init__(self):
        """Initializes the workflow and sets up the Jinja2 environment."""
        super().__init__()
        # Set up Jinja2 environment to load templates from the 'templates' subdirectory
        # within this package
        self.jinja_env = jinja2.Environment(
            loader=jinja2.PackageLoader("geometor.seer.workflows.default", "templates"),
            autoescape=False # We are generating text/code, not HTML
        )
        print("      DefaultWorkflow initialized with Jinja2 PackageLoader.")


    def _render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Loads and renders a Jinja2 template."""
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(context)
        except jinja2.TemplateNotFound:
            raise FileNotFoundError(f"Workflow template not found: {template_name}")
        except Exception as e:
            raise RuntimeError(f"Error rendering template {template_name}: {e}")


    def execute(
        self, session_task: "SessionTask", task: "Task", seer_instance: "Seer"
    ) -> None:
        """Orchestrates the default dreamer -> coder -> refine process."""
        history: List[Any] = []
        task_step: TaskStep | None = None  # Keep track of the last step

        try:
            # --- Investigation Phase ---
            # Step 1: Dreamer (All Pairs)
            task_step = self._investigate_dreamer(
                session_task, task, seer_instance, history
            )
            # Update history *after* successful step execution
            # History now includes the rendered prompt + response
            history.extend(task_step.content) # Rendered prompt content
            # history.extend(task_step.instructions) # Instructions are part of rendered content now
            history.extend(task_step.response_parts) # Add response to history

            if self._check_success_and_log(task_step, "investigate_dreamer"):
                return  # Task solved

            # Step 2: Coder (All Pairs) - Only if Dreamer didn't solve
            task_step = self._investigate_coder(
                session_task, task, seer_instance, history
            )
            # Update history *after* successful step execution
            history.extend(task_step.content)
            # history.extend(task_step.instructions) # Part of rendered content
            history.extend(task_step.response_parts)

            if self._check_success_and_log(task_step, "investigate_coder"):
                return  # Task solved

            # --- Refinement Phase ---
            current_iteration = 0
            max_iterations = seer_instance.config.max_iterations # Get from Seer's config

            while current_iteration < max_iterations:
                if not task_step:  # Safety check
                    raise Exception(
                        "task_step became None unexpectedly before refinement loop."
                    )

                code_trial = task_step.get_first_code_trial()
                if not code_trial:
                    error_msg = f"No code trial found from step '{task_step.title}' to start refinement iteration {current_iteration}."
                    print(f"            ERROR: {error_msg}")
                    session_task.log_error(Exception(error_msg), "Refinement Start")
                    return # Cannot proceed

                # History is updated *within* _refine_iteration
                task_step = self._refine_iteration(
                    session_task,
                    task,
                    seer_instance,
                    history, # Pass mutable history
                    code_trial,
                    current_iteration,
                )

                if self._check_success_and_log(
                    task_step, f"refine_iteration_{current_iteration}"
                ):
                    return  # Task solved

                current_iteration += 1

            print(
                f"            INFO: Reached max iterations ({max_iterations}) without solving task {task.id}."
            )

        except Exception as e:
            print(f"      ERROR during DefaultWorkflow execution for task {task.id}: {e}")
            if not session_task.errors or str(e) not in str(session_task.errors.values()):
                 session_task.log_error(e, f"DefaultWorkflow execution failed for task {task.id}")


    def _investigate_dreamer(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any], # History is read-only here
    ) -> TaskStep:
        """Handles the 'investigate dreamer' step using templates."""
        title = "investigate • dreamer • all training"

        # Prepare context for the template
        pair_data_str = ""
        for i, pair in enumerate(task.train, 1):
             # Use get_pair_prompt but only take the string parts for the template
             pair_prompt_parts = get_pair_prompt(f"train_{i}", pair, include_images=False) # Don't include images in text prompt
             pair_data_str += "".join(part for part in pair_prompt_parts if isinstance(part, str))
        # Add full task image separately if needed (though template doesn't explicitly ask)
        # if seer_instance.use_images:
        #     pair_data_str += "\n## Full Task (Train)\n"
        #     # How to represent image in template? Maybe not needed for dreamer text analysis

        context = {"pair_data": pair_data_str}
        rendered_prompt = self._render_template("investigate_dreamer.j2", context)

        # Content for _generate is the rendered prompt
        # Instructions are now part of the rendered prompt
        content = [rendered_prompt]
        instructions = [] # No separate instructions needed

        try:
            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history, # Pass existing history
                content, # Pass rendered prompt as content
                instructions, # Empty list
                tools="code_execution", # Dreamer might still use tools for analysis
            )
            task_step.run_trials() # Dreamer might generate initial code to test hypothesis
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise


    def _investigate_coder(
        self,
        session_task: "SessionTask",
        task: "Task", # Task might not be needed if context comes from history
        seer_instance: "Seer",
        history: List[Any], # History contains dreamer's output
    ) -> TaskStep:
        """Handles the 'investigate coder' step using templates."""
        title = "investigate • coder • all training"

        # Prepare context for the template
        # Extract relevant parts from history (e.g., dreamer's NLP)
        # This might need refinement based on how dreamer structures its response
        history_context_str = "\n".join(str(part) for part in history[-2:] if isinstance(part, str)) # Example: take last 2 text parts
        natural_language_program = "Extracted NLP from Dreamer's response" # TODO: Implement robust extraction

        context = {
            "history_context": history_context_str,
            "natural_language_program": natural_language_program
        }
        rendered_prompt = self._render_template("investigate_coder.j2", context)

        content = [rendered_prompt]
        instructions = []

        try:
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history, # Pass history (includes dreamer's output)
                content, # Pass rendered prompt
                instructions,
                # No tools needed for coder by default?
            )
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise


    def _refine_iteration(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any], # Pass the mutable history list
        code_trial: CodeTrial,
        iteration: int,
    ) -> TaskStep:
        """Handles one iteration of the refinement loop using templates."""
        task_step: TaskStep | None = None

        # --- Refine Dreamer ---
        title = f"refine • {iteration} • dreamer"
        try:
            # Prepare context
            pair_data_str = ""
            for i, pair in enumerate(task.train, 1): # Include train pairs for context
                 pair_prompt_parts = get_pair_prompt(f"train_{i}", pair, include_images=False)
                 pair_data_str += "".join(part for part in pair_prompt_parts if isinstance(part, str))
            # Add test pairs too? Maybe just the failing ones from the report?

            context = {
                "pair_data": pair_data_str,
                "previous_code": code_trial.code,
                "execution_report": code_trial.generate_report()
            }
            rendered_prompt = self._render_template("refine_dreamer.j2", context)
            content = [rendered_prompt]
            instructions = []

            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history, # Pass current history state
                content,
                instructions,
                tools="code_execution", # Dreamer might use tools for analysis
            )
            # Update history *after* successful generation
            history.extend(content)
            history.extend(task_step.response_parts)

            task_step.run_trials() # Dreamer refinement might produce testable code
            task_step.summarize()
            if self._check_success_and_log(task_step, title):
                return task_step  # Solved by dreamer refinement

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise

        # --- Refine Coder ---
        title = f"refine • {iteration} • coder"
        try:
            # Prepare context - history already includes dreamer's refinement output
            history_context_str = "\n".join(str(part) for part in history[-4:] if isinstance(part, str)) # Example: take last few parts
            natural_language_program = "Extracted refined NLP from Dreamer's response" # TODO: Implement robust extraction

            context = {
                "history_context": history_context_str,
                "natural_language_program": natural_language_program
            }
            rendered_prompt = self._render_template("refine_coder.j2", context)
            content = [rendered_prompt]
            instructions = []

            # Use the history updated by the dreamer step above
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history, # Pass history including dreamer's output
                content,
                instructions,
                # No tools needed?
            )
            # Update history *after* successful generation
            history.extend(content)
            history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()
            return task_step # Return coder step; outer loop checks success

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise


    def _check_success_and_log(self, task_step: TaskStep, step_name: str) -> bool:
        """Checks if a step was successful and logs appropriately."""
        train_passed = task_step.any_trials_successful("train")
        if train_passed is None:
             print(f"            Step '{step_name}': train status unknown.")
             return False
        elif train_passed:
            print(f"            Step '{step_name}': train passed")
            test_passed = task_step.any_trials_successful("test")
            if test_passed is None:
                 print(f"            Step '{step_name}': test status unknown.")
            elif test_passed:
                print(f"            Step '{step_name}': test passed")
            else:
                 print(f"            Step '{step_name}': test failed")
            return True # Training passed
        else:
            print(f"            Step '{step_name}': train failed")
            return False
