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
from pathlib import Path # Ensure Path is imported

# Local application/library specific imports
from geometor.seer.config import Config # Import the new Config class
from geometor.seer.session import Session, SessionTask

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client

from geometor.seer.trials.code_trial import CodeTrial


class Seer:
    # Change type hint from dict to Config
    def __init__(self, config: Config):
        """
        Initializes the Seer orchestrator.

        Args:
            config: The loaded Config object containing all settings.

        Raises:
            ValueError: If essential configuration is missing or invalid.
            RuntimeError: If GeminiClient initialization fails.
        """
        self.config = config # Store the Config object

        # Initialize Gemini clients for each role defined in the config
        self.roles: Dict[str, Client] = {}
        try:
            # Access roles via the Config object's property
            for role_name in config.roles.keys():
                # Pass the whole Config object and the role name to the client constructor
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
            raise ValueError("Configuration must define at least 'dreamer' and 'coder' roles.")


    def run(self, tasks: Tasks, output_dir: Path, description: str):
        """
        Runs the task-solving process for a collection of tasks.

        Args:
            tasks: A Tasks object containing the tasks to solve.
            output_dir: The root directory for saving session output.
            description: A description for this session run.
        """
        # Pass the Config object to the Session constructor
        session = Session(self.config, output_dir, description)

        for task in tasks:
            self.solve(session, task)

        session.summarize()

    def solve(self, session: Session, task: Task):
        session_task = session.add_task(task)

        try:
            self._investigate(task, session_task)
        except Exception as e:
            # Log the error at the SessionTask level
            session_task.log_error(e, "Investigation failed")

        session_task.summarize()

    def _investigate(self, task: Task, session_task: SessionTask):
        """
        Investigate all training pairs, stopping if a step fails critically.
        """
        history = [] # Define history at the start
        task_step = None # Initialize task_step to avoid potential UnboundLocalError

        # STEP: dreamer *****************************
        title = "investigate • dreamer • all training" # Define title here for except block
        try:
            content = []
            for i, pair in enumerate(task.train, 1):
                content.extend(get_pair_prompt(f"train_{i}", pair, self.use_images))

            if self.use_images:
                #  show full task image
                content.append(task.to_image(show_test=False))

            # Access instruction content directly from the pre-loaded dictionary
            instruction_content = self.instructions.get("investigate_dreamer")
            if not instruction_content:
                raise ValueError("Missing instruction: 'investigate_dreamer'")
            instructions = [instruction_content]

            task_step = self._generate(
                session_task,
                "dreamer",
                title,
                history,
                content,
                instructions,
                tools="code_execution",
            )

            history.extend(content)
            history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()

            if task_step.any_trials_successful("train"):
                print("            train passed")
                if task_step.any_trials_successful("test"):
                    print("            test passed")
                return # Success, exit investigation

        except Exception as e:
            # _generate raises Exception on failure after retries
            print(f"            ERROR: unable to get valid response. ")
            print(f"            Stopping investigation for task {task.id}.")
            # Error is already logged within _generate or by the exception handler in SessionTask/Level
            # We log the context of the failure here.
            session_task.log_error(e, f"Unable to get valid response. Stopping investigation.")
            return # Stop investigation for this task

        # STEP: coder *********************************
        title = "investigate • coder • all training" # Define title here for except block
        try:
            # Access instruction content directly
            instruction_content = self.instructions.get("investigate_coder")
            if not instruction_content:
                raise ValueError("Missing instruction: 'investigate_coder'")
            instructions = [instruction_content]

            content = [""] # Minimal content for coder based on history
            task_step = self._generate(
                session_task,
                "coder",
                title,
                history, # History includes dreamer prompt and response
                content,
                instructions,
                #  tools="code_execution", # Coder might not need tools initially
            )
            # History update is tricky here, coder prompt is minimal, response is key
            # history.extend(prompt) # Probably not useful to add empty prompt
            history.extend(task_step.response_parts) # Add coder's response/code

            task_step.run_trials()
            task_step.summarize()

            if task_step.any_trials_successful("train"):
                print("            train passed")
                if task_step.any_trials_successful("test"):
                    print("            test passed")
                return # Success, exit investigation

        except Exception as e:
            print(f"            ERROR: unable to get valid response. ")
            print(f"            Stopping investigation for task {task.id}.")
            session_task.log_error(e, f"Unable to get valid reponse. Stopping investigation.")
            return # Stop investigation for this task


        # Refinement Loop ****************************
        current_iteration = 0
        while current_iteration < self.max_iterations:
            # Get the first (and presumably only) CodeTrial from the *previous* step (coder or last refine)
            if not task_step: # Should not happen if coder step succeeded, but safety check
                 session_task.log_error(Exception("task_step is None before refinement loop."))
                 return

            code_trial = task_step.get_first_code_trial()
            if not code_trial:
                # Handle the case where there's no code trial (e.g., coder failed to produce code)
                session_task.log_error(Exception(f"No code trial found to start refinement iteration {current_iteration}."))
                return # Cannot proceed with refinement

            code = code_trial.code

            try:
                # Call refine, which now also handles exceptions from its _generate calls
                # Pass the current history state into refine
                task_step = self.refine(
                    session_task,
                    task,
                    code,
                    code_trial,
                    current_iteration,
                    history, # Pass current history state
                )

                # Update history with the parts from the *last* step of refine (refine_coder response)
                # refine method itself should manage its internal history flow.
                # The task_step returned by refine contains the response_parts of its last internal step.
                # We need to add these to the main history for the *next* iteration or if we exit here.
                # Note: refine takes history as input, so it sees the state *before* its execution.
                # We add its final output *after* it returns.
                if task_step and task_step.response_parts:
                     # Avoid adding empty lists if refine failed early or had no response parts
                     # This assumes refine returns the last step it executed, even on partial success/failure before exception.
                     # If refine raises an exception, task_step might be from the failed sub-step.
                     # Let's only update history based on the *returned* task_step from a *successful* refine call.
                     # The exception block handles the failure case.
                     # We need the history from the *end* of the refine call for the *next* iteration.
                     # refine doesn't explicitly return the new history state.
                     # Let's assume the task_step.response_parts are what we need to append.
                     # This might need refinement based on exactly what `refine` puts in response_parts.
                     # For now, append the response parts of the step returned by refine.
                     history.extend(task_step.response_parts)


                # Check if the refinement step was successful
                if task_step.any_trials_successful("train"):
                    print("            train passed")
                    if task_step.any_trials_successful("test"):
                        print("            test passed")
                    return # Success, exit investigation

                # If refine completed but didn't pass, the loop continues.
                # History has been updated with the output of the refine step.

            except Exception as e:
                # Catch critical failure from _generate within refine
                print(f"            ERROR: unable to get valid response. ")
                print(f"            Stopping investigation for task {task.id}.")
                # Error is already logged within refine's exception handler before re-raising
                # We log the context of the failure during refinement here.
                session_task.log_error(e, f"Unable to get valid response. Stopping investigation.")
                return # Stop investigation

            current_iteration += 1

        print(f"            INFO: Reached max iterations ({self.max_iterations}) without solving task {task.id}.")


    def _generate(
        self,
        session_task: SessionTask,
        role_name: str, # e.g., "dreamer", "coder"
        title: str,     # Title for the step being generated
        history: List[Any], # Conversation history (text, images)
        content: List[Any], # New content for this turn (text, images)
        instructions: List[str], # Specific instructions for this turn
        tools: Union[List[Callable], str, None] = None, # Tools (functions or "code_execution")
        # functions argument seems redundant if tools handles function calling
        # functions=None,
    ):
        """
        Generate content from the model, handling logging and retries.
        """

        # Ensure the role exists
        client = self.roles.get(role_name)
        if not client:
            # Log error at session_task level? Or raise immediately?
            # Raising immediately might be better to stop faulty execution flow.
            raise ValueError(f"Invalid role name '{role_name}' provided to _generate.")

        # init step - Pass the client's model name for potential logging/debugging
        task_step = session_task.add_step(title, history, content, instructions, client.model_name)

        # --- Start of improved retry logic ---
        # Get max_retries from config, fallback to default
        max_retries = self.config.get("max_retries", 2)
        response = None
        start_time = datetime.now()  # Start timer before loop
        valid_response_received = False # Flag to track success

        while task_step.attempts < max_retries:
            # Combine history, new content, and instructions for the prompt
            # Ensure all parts are suitable for the API (e.g., strings, PIL Images)
            # The GeminiClient expects a List[Any] where Any can be str or Image.
            total_prompt: List[Any] = history + content + instructions

            # If not the first attempt, wait before retrying
            if task_step.attempts > 0:
                # Get retry delay from config, fallback to default
                retry_delay = self.config.get("retry_delay_seconds", 10)
                print(f"            ...waiting {retry_delay} seconds before retry ({task_step.attempts + 1}/{max_retries})")
                time.sleep(retry_delay)

            task_step.attempts += 1
            current_attempt = task_step.attempts # For logging clarity

            try:
                response = client.generate_content(total_prompt, tools=tools)

                # Check for valid response: Must have candidates, finish_reason=STOP, and accessible text
                #  if response.candidates and response.candidates[0].finish_reason == 1: # STOP
                if response.candidates:
                    try:
                        _ = response.text  # Attempt access
                        # Valid response received!
                        valid_response_received = True
                        break # Exit the retry loop successfully
                    except ValueError as ve:
                        # Finish reason is STOP, but text is not accessible (e.g., safety)
                        finish_reason_str = getattr(response.candidates[0].finish_reason, 'name', 'STOP')
                        print(f"            retry {current_attempt}/{max_retries} - Response finished ({finish_reason_str}), but text not accessible: {ve}")
                        task_step.log_error(ve, f"Response STOP but text inaccessible on attempt {current_attempt}/{max_retries}")
                        # Continue loop if retries remain
                else:
                    # Handle cases with no candidates or non-STOP finish reasons
                    finish_reason = response.candidates[0].finish_reason if response.candidates else "NO_CANDIDATES"
                    finish_reason_str = getattr(finish_reason, 'name', str(finish_reason))
                    print(f"            RETRY: {current_attempt}/{max_retries} - Invalid response or finish reason: {finish_reason_str}")
                    task_step.log_error(Exception(f"Invalid response/finish reason ({finish_reason_str})"), f"Attempt {current_attempt}/{max_retries}")
                    # Continue loop if retries remain

            except Exception as e:
                # Catch errors during the API call itself
                print(f"            RETRY: {current_attempt}/{max_retries} - API Call ERROR: {e}")
                task_step.log_error(e, f"API call failed on attempt {current_attempt}/{max_retries}")
                # Ensure response is None if API call failed, important for check after loop
                response = None
                # Continue loop if retries remain

        # --- After the while loop ---
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        # Check if the loop completed without getting a valid response
        if not valid_response_received:
            error_msg = f"ERROR: Failed to get a valid response after {task_step.attempts} retries."
            print(f"            {error_msg}")

            # Log the final response received (even if invalid or None) before raising
            # Pass the actual number of attempts made
            task_step.log_response(response, response_time, retries=task_step.attempts)

            # Log a final summary error indicating failure after all retries
            exc = Exception(error_msg)
            task_step.log_error(exc, "Final Generate Failure after all retries")
            raise exc # Raise the exception to be caught by the caller (_investigate or refine)

        # --- If we reach here, it means loop broke successfully with a valid response ---
        # Log the successful response, including the number of attempts it took
        task_step.log_response(response, response_time, retries=task_step.attempts)

        # Process the valid response
        reponse_parts = task_step.process_response(response)
        return task_step
        # --- End of improved retry logic ---

    def refine(
        self,
        session_task: SessionTask,
        task: Task,
        code,
        code_trial,
        current_iteration,
        history: list, # Accept history from caller (_investigate)
    ):
        """
        Refines the generated code based on test results, handling exceptions.
        Returns the final task_step of this refinement iteration (coder step).
        Raises Exception if a sub-step (_generate) fails critically.
        """

        # Make a copy of history to avoid modifying the caller's list directly within this scope.
        # The history for this refinement iteration starts with the state *before* this iteration.
        current_history = list(history)
        task_step = None # Initialize task_step

        # STEP: refine dreamer *****************************
        title = f"refine • {current_iteration} • dreamer" # Define title for except block
        try:
            content = []
            # Access instruction content directly
            instruction_content = self.instructions.get("refine_dreamer")
            if not instruction_content:
                raise ValueError("Missing instruction: 'refine_dreamer'")
            instructions = [instruction_content]

            content.append("\nPrevious Code:\n")
            content.append(f"```python\n{code}\n```\n")
            content.append(code_trial.generate_report())

            task_step = self._generate(
                session_task,
                "dreamer",
                title,
                current_history, # Pass the history up to this point
                content,
                instructions,
                tools="code_execution",
            )
            # Update history *within this refinement iteration*
            current_history.extend(content)
            current_history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()

            # Check for immediate success after dreamer refinement
            if task_step.any_trials_successful("train"):
                print("            train passed")
                if task_step.any_trials_successful("test"):
                    print("            test passed")
                # Return the successful dreamer step. The caller (_investigate)
                # will handle history update based on this returned step.
                return task_step

        except Exception as e:
            print(f"        ERROR: Step '{title}' failed critically during refinement.")
            # Log the error context before re-raising
            session_task.log_error(e, f"Critical failure in step: {title} during refinement iteration {current_iteration}.")
            # Let the exception propagate up to the caller (_investigate)
            raise e # Re-raise the exception


        # STEP: refine coder *****************************
        # This step only runs if the dreamer step didn't succeed but also didn't fail critically.
        title = f"refine • {current_iteration} • coder" # Define title for except block
        try:
            content = [""]  # Coder prompt might be minimal, relies on history
            # Access instruction content directly
            instruction_content = self.instructions.get("refine_coder")
            if not instruction_content:
                raise ValueError("Missing instruction: 'refine_coder'")
            instructions = [instruction_content]

            # Use the updated current_history (including dreamer output)
            task_step = self._generate(
                session_task,
                "coder",
                title,
                current_history, # Pass history including dreamer's output
                content,
                instructions,
                #  tools="code_execution" # Coder might not need tools
            )

            # History update for the *caller* (_investigate) happens based on the
            # task_step returned from this function. We don't need to extend
            # current_history further here unless a subsequent step within refine needed it.

            # Run trials and summarize the coder step
            task_step.run_trials()
            task_step.summarize()

            # Return the final task_step (coder's step) regardless of trial success here.
            # The caller (_investigate) will check its success and update its history.
            return task_step

        except Exception as e:
            print(f"        ERROR: Step '{title}' failed critically during refinement.")
            # Log the error context before re-raising
            session_task.log_error(e, f"Critical failure in step: {title} during refinement iteration {current_iteration}.")
            # Let the exception propagate up to the caller (_investigate)
            raise e # Re-raise the exception
