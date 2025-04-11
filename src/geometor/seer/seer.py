"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

# Standard library imports
from __future__ import annotations
from typing import TYPE_CHECKING, List, Any, Dict, Union, Callable
from datetime import datetime
import time
from pathlib import Path
import json

# Local application/library specific imports
from geometor.seer.config import Config
from geometor.seer.session import (
    Session,
    SessionTask,
    TaskStep,
)  # Add TaskStep import if needed by _generate

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

# Import the default workflow from its new package location
from geometor.seer.workflows.default import DefaultWorkflow

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client

from geometor.seer.trials.code_trial import CodeTrial


class Seer:
    def __init__(self, config: Config):
        """
        Initializes the Seer orchestrator.

        Args:
            config: The loaded Config object containing all settings.

        Raises:
            ValueError: If essential configuration is missing or invalid.
            RuntimeError: If GeminiClient initialization fails.
        """
        self.config = config

        # Initialize Gemini clients for each role defined in the config
        self.roles: Dict[str, Client] = {}
        try:
            # Access roles via the Config object's property
            for role_name in config.roles.keys():
                # Pass the whole Config object and the role name to the client
                # constructor
                self.roles[role_name] = Client(config, role_name)
        except Exception as e:
            # Catch errors during client initialization (e.g., missing API key, model init failure)
            raise RuntimeError(f"Failed to initialize Gemini clients: {e}") from e

        # Instructions are now pre-loaded by the Config object
        # Access instructions via the property (content is already loaded)
        self.instructions: Dict[str, str] = config.instructions
        if not self.instructions:
            print("Warning: No instructions loaded from configuration.")

        # Access other configuration parameters via properties
        self.max_iterations = config.max_iterations
        self.use_images = config.use_images

        # Ensure essential roles are present
        if "dreamer" not in self.roles or "coder" not in self.roles:
            raise ValueError(
                "Configuration must define at least 'dreamer' and 'coder' roles."
            )

    def run(self, tasks: Tasks, output_dir: Path, description: str):
        """
        Runs the task-solving process for a collection of tasks.

        Args:
            tasks: A Tasks object containing the tasks to solve.
            output_dir: The root directory for saving session output.
            description: A description for this session run.
        """
        session = Session(self.config, output_dir, description)

        for task in tasks:
            self.solve(session, task)

        session.summarize()
        self._generate_submission_file(session)

    def solve(self, session: Session, task: Task):
        """Sets up the SessionTask and delegates solving to the configured workflow."""
        session_task = session.add_task(task)
        # TODO: Get workflow name from config, providing a default
        # workflow_name = self.config.get("workflow", "default")
        workflow_name = "default"  # Hardcode for now

        try:
            # TODO: Implement _get_workflow factory method later
            # workflow = self._get_workflow(workflow_name)
            if workflow_name == "default":
                workflow = DefaultWorkflow()
            else:
                # Fallback or error
                print(
                    f"Warning: Unknown workflow '{workflow_name}', falling back to 'default'."
                )
                #  workflow = DefaultWorkflow()
                raise ValueError(f"Unknown workflow: {workflow_name}")

            print(f"        workflow: {workflow_name}")
            # Pass self (Seer instance) to the workflow's execute method
            workflow.execute(session_task, task, self)
        except Exception as e:
            # Catch top-level errors during workflow instantiation or execution
            error_msg = f"         Workflow '{workflow_name}' failed for task {task.id}: {e}"
            print(f"          ERROR: {error_msg}")
            # Ensure error is logged even if it happened during workflow execution
            # Check if the specific error message is already in the log
            if not session_task.errors or str(e) not in str(
                session_task.errors.values()
            ):
                session_task.log_error(e, error_msg)
            # Potentially log traceback for detailed debugging
            # import traceback
            # session_task.log_error(traceback.format_exc(), f"Traceback for {error_msg}")

        # Summarization always happens after the workflow attempts execution
        session_task.summarize()

    # _investigate method is removed

    # refine method is removed

    def _generate_submission_file(self, session: Session):
        """
        Generates the submission.json file based on the best test predictions
        for tasks that passed training. Uses the specific Kaggle format provided.
        """
        submission_data = {}
        print("\nGenerating submission file...")

        for task_id, session_task in session.tasks.items():
            best_task_trial: CodeTrial | None = None

            # Find the best trial from the latest step that passed training
            for step in reversed(session_task.steps):  # Check latest steps first
                if step.train_passed is True:
                    # Assuming get_best_trial() gives the best trial *for that step*
                    step_best_trial = step.step_code_trials.get_best_trial()
                    if step_best_trial:
                        best_task_trial = step_best_trial
                        break  # Found the best trial from the latest successful step

            if not best_task_trial:
                print(
                    f"    Skipping task {task_id}: No successful training step found."
                )
                continue

            # Check if the best trial has test results and at least one trial
            if (
                best_task_trial.test_results
                and best_task_trial.test_results.get("trials")
                and len(best_task_trial.test_results["trials"]) > 0
            ):

                first_test_pair_trial = best_task_trial.test_results["trials"][0]
                predicted_grid_obj = first_test_pair_trial.transformed_output

                if predicted_grid_obj and isinstance(predicted_grid_obj, Grid):
                    try:
                        # Convert grid to list of lists Assuming Grid object
                        # stores data in .grid attribute which might be numpy
                        # array
                        if hasattr(predicted_grid_obj.grid, "tolist"):
                            output_list = predicted_grid_obj.grid.tolist()
                        elif isinstance(predicted_grid_obj.grid, list):
                            output_list = predicted_grid_obj.grid
                        else:
                            raise TypeError("Grid data is not a list or numpy array.")

                        # Add to submission data using the specified format
                        submission_data[task_id] = [
                            {
                                "attempt_1": output_list,
                                "attempt_2": None,  # Explicitly None (null in JSON)
                            }
                        ]
                        print(f"    Added prediction for task {task_id}")

                    except (AttributeError, TypeError, Exception) as e:
                        print(f"    ERROR processing grid for task {task_id}: {e}")
                        session_task.log_error(
                            e,
                            f"Error converting predicted grid for submission file for task {task_id}",
                        )
                else:
                    print(
                        f"    Skipping task {task_id}: No valid predicted grid found for the first test pair in the best trial."
                    )
                    # Log this potentially unexpected situation
                    if best_task_trial:
                        session_task.log_warning(
                            f"Best trial for task {task_id} found, but no valid predicted grid for first test pair.",
                            "Submission Generation",
                        )

            else:
                print(
                    f"    Skipping task {task_id}: Best trial found, but no test results available."
                )
                # Log this potentially unexpected situation
                if best_task_trial:
                    session_task.log_warning(
                        f"Best trial for task {task_id} found, but no test results available.",
                        "Submission Generation",
                    )

        # Write the submission file
        submission_file_path = session.dir / "submission.json"
        try:
            with open(submission_file_path, "w") as f:
                json.dump(submission_data, f, indent=2)
            print(f"Submission file generated: {submission_file_path}")
        except (IOError, TypeError) as e:
            print(f"    ERROR writing submission file: {e}")
            # Log error at the session level
            session.log_error(e, "Failed to write submission.json")

    def _generate(
        self,
        session_task: SessionTask,
        role_name: str,
        title: str,
        history: List[Any],
        content: List[Any],
        instructions: List[str],
        tools: Union[
            List[Callable], str, None
        ] = None,  # Tools (functions or "code_execution")
        # functions argument seems redundant if tools handles function calling
        # functions=None,
    ):
        """
        Generate content from the model, handling logging and retries with clearer output.
        """
        # Ensure the role exists
        client = self.roles.get(role_name)
        if not client:
            # Log error at session_task level? Or raise immediately?
            # Raising immediately might be better to stop faulty execution flow.
            raise ValueError(f"Invalid role name '{role_name}' provided to _generate.")

        # init step - Pass the client's model name for potential logging/debugging
        task_step = session_task.add_step(
            title, history, content, instructions, client.model_name
        )

        # --- Start of improved retry logic with clearer logging ---
        # Get max_attempts from config (using max_retries key for now), fallback to default
        # Let's interpret max_retries as total attempts for clarity in logging
        max_attempts = self.config.get("max_retries", 2) # e.g., 2 means try up to 2 times
        if max_attempts < 1: # Ensure at least one attempt
            max_attempts = 1

        response = None
        start_time = datetime.now()
        valid_response_received = False
        last_concise_error = "Unknown failure" # Store the last concise error message

        # Loop from attempt 1 up to max_attempts
        for current_attempt in range(1, max_attempts + 1):
            task_step.attempts = current_attempt # Update step's attempt count

            # If not the first attempt, wait before retrying
            if current_attempt > 1:
                retry_delay = self.config.get("retry_delay_seconds", 10)
                # No separate print for waiting, just sleep
                time.sleep(retry_delay)

            total_prompt: List[Any] = history + content + instructions
            concise_error = None # Reset error for this attempt

            try:
                response = client.generate_content(total_prompt, tools=tools)

                # Check for valid response
                if response.candidates:
                    try:
                        _ = response.text # Attempt access, raises ValueError if not usable
                        # If we got here, the response is likely valid
                        valid_response_received = True
                        break # Exit the loop successfully
                    except ValueError as ve:
                        # Text not accessible (e.g., safety, other finish reasons)
                        finish_reason_str = "UNKNOWN"
                        if response.candidates[0].finish_reason:
                             finish_reason_str = getattr(response.candidates[0].finish_reason, "name", str(response.candidates[0].finish_reason))
                        concise_error = f"Response text inaccessible (finish reason: {finish_reason_str})"
                        # Log the detailed error internally
                        task_step.log_error(ve, f"Response text inaccessible on attempt {current_attempt}/{max_attempts}")

                else:
                    # Handle cases with no candidates
                    concise_error = "No response candidates received"
                    task_step.log_error(Exception(concise_error), f"Attempt {current_attempt}/{max_attempts}")

            except Exception as e:
                # Catch errors during the API call itself
                concise_error = f"API call failed ({type(e).__name__})"
                # Log the detailed error internally
                task_step.log_error(e, f"API call failed on attempt {current_attempt}/{max_attempts}")
                # Optionally log traceback for debugging internal errors:
                # task_step.log_error(traceback.format_exc(), f"Traceback on attempt {current_attempt}/{max_attempts}")
                response = None # Ensure response is None if API call failed

            # If this attempt failed (concise_error is set)
            if concise_error:
                print(f"            attempt {current_attempt}/{max_attempts} failed: {concise_error}")
                last_concise_error = concise_error # Store for final error message

        # --- After the loop ---
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        # Check if the loop completed without getting a valid response
        if not valid_response_received:
            # Use the last recorded concise error message
            error_msg = f"ERROR: Failed to get a valid response after {task_step.attempts} attempts. Last error: {last_concise_error}"
            print(f"            {error_msg}")

            # Log the final response received (even if invalid or None)
            # Pass the actual number of attempts made
            task_step.log_response(response, response_time, retries=task_step.attempts)

            # Log a final summary error indicating failure after all attempts
            exc = Exception(error_msg) # Use the summary message for the exception
            task_step.log_error(exc, "Final Generate Failure after all attempts")
            raise exc # Raise the exception to be caught by the caller

        # --- If we reach here, it means loop broke successfully with a valid response ---
        # Log the successful response, including the number of attempts it took
        task_step.log_response(response, response_time, retries=task_step.attempts)

        # Process the valid response
        response_parts = task_step.process_response(response)
        return task_step
        # --- End of improved retry logic ---

    # refine method is removed
