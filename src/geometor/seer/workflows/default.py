from typing import TYPE_CHECKING, List, Any

# Local application/library specific imports
from .base import WorkflowBase
from geometor.seer.prompts import get_pair_prompt
from geometor.seer.session.task_step import TaskStep # Import TaskStep
from geometor.seer.trials.code_trial import CodeTrial # Import CodeTrial

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task


class DefaultWorkflow(WorkflowBase):
    """Implements the standard investigate-all-pairs then refine workflow."""

    def execute(
        self, session_task: "SessionTask", task: "Task", seer_instance: "Seer"
    ) -> None:
        """Orchestrates the default dreamer -> coder -> refine process."""
        # print(f"      Executing DefaultWorkflow for task {task.id}") # Removed redundant print
        history: List[Any] = []
        task_step: TaskStep | None = None  # Keep track of the last step

        try:
            # --- Investigation Phase ---
            # Step 1: Dreamer (All Pairs)
            task_step = self._investigate_dreamer(
                session_task, task, seer_instance, history
            )
            # Update history *after* successful step execution
            history.extend(task_step.content) # Add input content to history
            history.extend(task_step.instructions) # Add instructions to history
            history.extend(task_step.response_parts) # Add response to history

            if self._check_success_and_log(task_step, "investigate_dreamer"):
                return  # Task solved

            # Step 2: Coder (All Pairs) - Only if Dreamer didn't solve
            task_step = self._investigate_coder(
                session_task, task, seer_instance, history
            )
            # Update history *after* successful step execution
            history.extend(task_step.content)
            history.extend(task_step.instructions)
            history.extend(task_step.response_parts)

            if self._check_success_and_log(task_step, "investigate_coder"):
                return  # Task solved

            # --- Refinement Phase ---
            current_iteration = 0
            max_iterations = seer_instance.config.max_iterations

            while current_iteration < max_iterations:
                if not task_step:  # Safety check
                    raise Exception(
                        "task_step became None unexpectedly before refinement loop."
                    )

                code_trial = task_step.get_first_code_trial()
                if not code_trial:
                    # Log specific error if coder step didn't produce code
                    error_msg = f"No code trial found from step '{task_step.title}' to start refinement iteration {current_iteration}."
                    print(f"            ERROR: {error_msg}")
                    session_task.log_error(Exception(error_msg), "Refinement Start")
                    return # Cannot proceed

                # Refine returns the *last* step performed within it (usually coder)
                # History is updated *within* _refine_iteration
                task_step = self._refine_iteration(
                    session_task,
                    task,
                    seer_instance,
                    history, # Pass mutable history
                    code_trial,
                    current_iteration,
                )
                # No need to extend history here, _refine_iteration handles it internally

                if self._check_success_and_log(
                    task_step, f"refine_iteration_{current_iteration}"
                ):
                    return  # Task solved

                current_iteration += 1

            print(
                f"            INFO: Reached max iterations ({max_iterations}) without solving task {task.id}."
            )

        except Exception as e:
            # Catch errors from _investigate_*, _refine_iteration, or _check_success_and_log
            # Error should ideally be logged within the failing sub-method first
            print(f"      ERROR during DefaultWorkflow execution for task {task.id}: {e}")
            # Log a general workflow execution error if not already logged more specifically
            # Check if the specific error message is already in the log to avoid duplicates
            if not session_task.errors or str(e) not in str(session_task.errors.values()):
                 session_task.log_error(e, f"DefaultWorkflow execution failed for task {task.id}")
            # Allow execution to proceed to session_task.summarize() in Seer.solve

    def _investigate_dreamer(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any],
    ) -> TaskStep:
        """Handles the 'investigate dreamer' step."""
        title = "investigate • dreamer • all training"
        instruction_key = "investigate_dreamer"
        instruction_content = seer_instance.instructions.get(instruction_key)
        if not instruction_content:
            raise ValueError(f"Missing instruction: '{instruction_key}'")
        instructions = [instruction_content]

        content: List[Any] = []  # Build content list (prompts, images)
        for i, pair in enumerate(task.train, 1):
            content.extend(
                get_pair_prompt(f"train_{i}", pair, seer_instance.use_images)
            )
        if seer_instance.use_images:
            # show full task image
            content.append(task.to_image(show_test=False))

        try:
            # Call _generate via the seer_instance
            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history,
                content,
                instructions,
                tools="code_execution",
            )
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            # Error is already logged within _generate's exception handling
            # Re-raise to be caught by the main execute block
            raise

    def _investigate_coder(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any],
    ) -> TaskStep:
        """Handles the 'investigate coder' step."""
        title = "investigate • coder • all training"
        instruction_key = "investigate_coder"
        instruction_content = seer_instance.instructions.get(instruction_key)
        if not instruction_content:
            raise ValueError(f"Missing instruction: '{instruction_key}'")
        instructions = [instruction_content]
        content: List[Any] = [""]  # Minimal content, relies on history

        try:
            # Call _generate via the seer_instance
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history,
                content,
                instructions,
                # tools=... # Coder might not need tools initially
            )
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            # Error is already logged within _generate's exception handling
            # Re-raise to be caught by the main execute block
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
        """
        Handles one iteration of the refinement loop (dreamer and coder).
        Updates the passed history list internally.
        Returns the final task_step of this refinement iteration (coder step).
        Raises Exception if a sub-step (_generate) fails critically.
        """
        # History is passed in and modified *within* this method
        task_step: TaskStep | None = None # Initialize task_step for this scope

        # --- Refine Dreamer ---
        title = f"refine • {iteration} • dreamer"
        try:
            instruction_key = "refine_dreamer"
            instruction_content = seer_instance.instructions.get(instruction_key)
            if not instruction_content:
                raise ValueError(f"Missing instruction: '{instruction_key}'")
            instructions = [instruction_content]

            content: List[Any] = []
            content.append("\nPrevious Code:\n")
            content.append(f"```python\n{code_trial.code}\n```\n")
            content.append(code_trial.generate_report())

            # Call _generate via the seer_instance
            task_step = seer_instance._generate(
                session_task,
                "dreamer",
                title,
                history, # Pass current history state
                content,
                instructions,
                tools="code_execution",
            )
            # Update history *after* successful generation
            history.extend(content) # Add input content
            history.extend(instructions) # Add instructions
            history.extend(task_step.response_parts) # Add response

            task_step.run_trials()
            task_step.summarize()
            if self._check_success_and_log(task_step, title):
                return task_step  # Solved by dreamer refinement

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            # Error is already logged within _generate's exception handling
            # Re-raise to stop this iteration/workflow
            raise

        # --- Refine Coder (only if dreamer didn't solve but didn't fail critically) ---
        title = f"refine • {iteration} • coder"
        try:
            instruction_key = "refine_coder"
            instruction_content = seer_instance.instructions.get(instruction_key)
            if not instruction_content:
                raise ValueError(f"Missing instruction: '{instruction_key}'")
            instructions = [instruction_content]
            content: List[Any] = [""]  # Minimal content

            # Use the history updated by the dreamer step above
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history, # Pass history including dreamer's output
                content,
                instructions,
                # tools=... # Coder might not need tools
            )
            # Update history *after* successful generation
            history.extend(content) # Add input content (empty string)
            history.extend(instructions) # Add instructions
            history.extend(task_step.response_parts) # Add response

            task_step.run_trials()
            task_step.summarize()
            # Return the coder step regardless of success; outer loop checks
            return task_step

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            # Error is already logged within _generate's exception handling
            # Re-raise to stop this iteration/workflow
            raise

    def _check_success_and_log(self, task_step: TaskStep, step_name: str) -> bool:
        """Checks if a step was successful and logs appropriately."""
        # Check train success first
        train_passed = task_step.any_trials_successful("train")
        if train_passed is None: # Handle case where trials might not have run or produced results
             print(f"            Step '{step_name}': train status unknown (no successful trials found or trials not run).")
             return False
        elif train_passed:
            print(f"            Step '{step_name}': train passed")
            # Check test success only if train passed
            test_passed = task_step.any_trials_successful("test")
            if test_passed is None:
                 print(f"            Step '{step_name}': test status unknown.")
            elif test_passed:
                print(f"            Step '{step_name}': test passed")
            else:
                 print(f"            Step '{step_name}': test failed")
            return True # Return True because training passed
        else:
            print(f"            Step '{step_name}': train failed")
            return False
