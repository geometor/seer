from typing import TYPE_CHECKING, List, Any, Dict
import jinja2
from pathlib import Path

# Local application/library specific imports
from ..base import WorkflowBase
from geometor.seer.prompts import get_pair_prompt
from geometor.seer.session.task_step import TaskStep
from geometor.seer.trials.code_trial import CodeTrial
from geometor.seer.tasks.tasks import TaskPair # Import TaskPair from tasks.py

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task


# Changed class name
class IncrementalWorkflow(WorkflowBase):
    """
    Implements an incremental workflow: dreamer sees one pair at a time,
    then coder generates code, followed by refinement loops.
    Uses Jinja2 templates loaded from the package.
    """

    def __init__(self):
        """Initializes the workflow and sets up the Jinja2 environment."""
        super().__init__()
        # Set up Jinja2 environment to load templates from the 'templates' subdirectory
        # within *this* package (incremental)
        self.jinja_env = jinja2.Environment(
            # Changed package path
            loader=jinja2.PackageLoader("geometor.seer.workflows.incremental", "templates"),
            autoescape=False,  # We are generating text/code, not HTML
        )
        # print("      IncrementalWorkflow initialized with Jinja2 PackageLoader.") # Optional debug print

    def _render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Loads and renders a Jinja2 template."""
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(context)
        except jinja2.TemplateNotFound:
            # Use the correct template directory name in the error
            raise FileNotFoundError(f"Workflow template not found in 'incremental' workflow: {template_name}")
        except Exception as e:
            raise RuntimeError(f"Error rendering template {template_name}: {e}")

    def execute(
        self, session_task: "SessionTask", task: "Task", seer_instance: "Seer"
    ) -> None:
        """Orchestrates the incremental dreamer -> coder -> refine process."""
        history: List[Any] = []
        task_step: TaskStep | None = None  # Keep track of the last step

        try:
            # --- Incremental Investigation Phase ---
            # Loop through each training pair for the dreamer
            for i, pair in enumerate(task.train):
                is_first_pair = (i == 0)
                task_step = self._investigate_dreamer_step(
                    session_task,
                    task,
                    seer_instance,
                    history, # Pass mutable history
                    pair,
                    i + 1, # Use 1-based index for naming/logging
                    is_first_pair,
                )
                # Update history *after* successful step execution
                # Add the content (pair data) and the response to history
                history.extend(task_step.content)
                history.extend(task_step.response_parts)

                # Optional: Check for success after each dreamer step?
                # Usually, we wait for the coder, but could add a check here.
                # if self._check_success_and_log(task_step, f"investigate_dreamer_pair_{i+1}"):
                #     return # Task solved early (unlikely without code)


            # --- Coding Phase (after all dreamer steps) ---
            if not task_step: # Should not happen if there's at least one train pair
                 raise Exception("No dreamer steps were executed.")

            # Coder acts based on the final accumulated history from the dreamer
            task_step = self._investigate_coder(
                session_task, task, seer_instance, history # Pass final history
            )
            # Update history *after* successful step execution
            # Add only the response to history (content was empty)
            history.extend(task_step.response_parts)

            if self._check_success_and_log(task_step, "investigate_coder"):
                return  # Task solved by the first coder attempt

            # --- Refinement Phase ---
            current_iteration = 0
            max_iterations = (
                seer_instance.config.max_iterations
            )

            while current_iteration < max_iterations:
                if not task_step:
                    raise Exception(
                        "task_step became None unexpectedly before refinement loop."
                    )

                code_trial = task_step.get_first_code_trial()
                if not code_trial:
                    error_msg = f"No code trial found from step '{task_step.title}' to start refinement iteration {current_iteration}."
                    print(f"            ERROR: {error_msg}")
                    session_task.log_error(Exception(error_msg), "Refinement Start")
                    return

                # History is updated *within* _refine_iteration
                task_step = self._refine_iteration(
                    session_task,
                    task,
                    seer_instance,
                    history,  # Pass mutable history
                    code_trial,
                    current_iteration,
                )

                if self._check_success_and_log(
                    task_step, f"refine_iteration_{current_iteration}"
                ):
                    return # Task solved

                current_iteration += 1

            print(
                f"            INFO: Reached max iterations ({max_iterations}) without solving task {task.id}."
            )

        except Exception as e:
            print(
                f"      ERROR during IncrementalWorkflow execution for task {task.id}: {e}"
            )
            if not session_task.errors or str(e) not in str(
                session_task.errors.values()
            ):
                session_task.log_error(
                    e, f"IncrementalWorkflow execution failed for task {task.id}"
                )

    # Renamed from _investigate_dreamer and modified significantly
    def _investigate_dreamer_step(
        self,
        session_task: "SessionTask",
        task: "Task", # Keep task for context if needed, though pair is primary
        seer_instance: "Seer",
        history: List[Any],  # History is read-only here, but updated in execute
        pair: TaskPair,      # The specific pair for this step
        pair_index: int,     # 1-based index of the pair
        is_first: bool,      # Flag for first pair
    ) -> TaskStep:
        """Handles a single dreamer step for one training pair."""
        title = f"investigate • dreamer • pair {pair_index}"
        template_name = "investigate_dreamer_initial.j2" if is_first else "investigate_dreamer_incremental.j2"

        # Prepare content (just the current pair's data)
        content = get_pair_prompt(
            f"train_{pair_index}", pair, include_images=seer_instance.use_images
        )
        # Optionally add full task image only on first step? Or never? Let's omit for now.
        # if is_first and seer_instance.use_images:
        #     content.append(task.to_image(show_test=False))

        # Prepare instructions (rendered template)
        instruction_text = self._render_template(template_name, {}) # No context needed for these static templates
        instructions = [instruction_text]

        try:
            # Note: History passed here contains analysis from *previous* pairs
            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history,      # Pass existing history
                content,      # Pass *current pair* data as content
                instructions, # Pass rendered template as instructions
                tools="code_execution", # Dreamer might still use tools
            )
            # Trials are usually run on coder output, but dreamer *could* generate code
            # Let's run trials here too, in case the dreamer tries to solve it directly
            # or uses code_execution effectively.
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise

    # This method remains largely the same as in DefaultWorkflow,
    # but it now acts on the history accumulated from *all* dreamer steps.
    def _investigate_coder(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any],  # History contains all dreamer outputs
    ) -> TaskStep:
        """Handles the 'investigate coder' step after all dreamer steps."""
        title = "investigate • coder • final" # Adjusted title slightly

        # Content is empty; coder works from history + instructions
        content = [""]

        # Prepare instructions (rendered template)
        # Uses the standard coder template
        instruction_text = self._render_template("investigate_coder.j2", {})
        instructions = [instruction_text]

        try:
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history,      # Pass history (includes all dreamer outputs)
                content,      # Pass empty content
                instructions, # Pass rendered template as instructions
                # No tools needed for coder by default
            )
            task_step.run_trials() # Crucial: run trials on the generated code
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise

    # This method should be identical to the one in DefaultWorkflow,
    # as the refinement logic (based on code trials) is the same.
    # It uses the history accumulated up to that point.
    def _refine_iteration(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any],  # Pass the mutable history list
        code_trial: CodeTrial,
        iteration: int,
    ) -> TaskStep:
        """Handles one iteration of the refinement loop using templates."""
        task_step: TaskStep | None = None # To hold the latest step in the iteration

        # --- Refine Dreamer ---
        title = f"refine • {iteration} • dreamer"
        try:
            # Prepare content (code + report)
            content = []
            content.append("\nPrevious Code:\n")
            content.append(f"```python\n{code_trial.code}\n```\n")
            content.append(code_trial.generate_report())

            # Prepare instructions (rendered template)
            instruction_text = self._render_template("refine_dreamer.j2", {})
            instructions = [instruction_text]

            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history,      # Pass current history state
                content,      # Pass code+report as content
                instructions, # Pass rendered template as instructions
                tools="code_execution",
            )
            # Update history *after* successful generation
            history.extend(content) # Add the code/report content
            history.extend(task_step.response_parts) # Add the response

            task_step.run_trials()
            task_step.summarize()
            if self._check_success_and_log(task_step, title):
                return task_step # Solved by dreamer refinement

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise

        # --- Refine Coder ---
        # This runs only if dreamer refinement didn't solve the task
        title = f"refine • {iteration} • coder"
        try:
            # Content is empty for this step
            content = [""]

            # Prepare instructions (rendered template)
            instruction_text = self._render_template("refine_coder.j2", {})
            instructions = [instruction_text]

            # Use the history updated by the dreamer step above
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history,      # Pass history including dreamer's output
                content,      # Pass empty content
                instructions, # Pass rendered template as instructions
                # No tools needed for coder by default
            )
            # Update history *after* successful generation
            # Add only the response to history (content was empty)
            history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()
            return task_step # Return coder step; outer loop checks success

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise

    # This method is identical to the one in DefaultWorkflow
    def _check_success_and_log(self, task_step: TaskStep, step_name: str) -> bool:
        """Checks if a step was successful and logs appropriately."""
        # Check if *any* trial within this step passed train
        train_passed = task_step.any_trials_successful("train")

        # Handle the case where trials might not have run or produced results
        if train_passed is None:
            # print(f"            Step '{step_name}': train status unknown (no successful trials or trials not run).")
            return False # Treat unknown as not passed for success checking

        elif train_passed:
            print(f"            train: passed")
            # Check test pass status only if train passed
            test_passed = task_step.any_trials_successful("test")
            if test_passed is None:
                # print(f"            Step '{step_name}': test status unknown.")
                pass # Don't log anything specific for unknown test status
            elif test_passed:
                print(f"            test: passed")
            else:
                # print(f"            Step '{step_name}': test failed")
                pass # Don't log test failed if train passed, focus is on train success
            return True  # Training passed, signal success for this step check

        else: # train_passed is False
            #  print(f"            Step '{step_name}': train failed")
            return False
