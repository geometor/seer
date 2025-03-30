"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
import time  # Added for retry delay

from geometor.seer.session import Session, SessionTask

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client

from geometor.seer.trials.code_trial import CodeTrial


class Seer:
    def __init__(self, config: dict):
        self.config = config

        self.roles = {}
        for role_name, role_config in config["roles"].items():
            self.roles[role_name] = Client(self.config, role_name)

        self.instructions = {}
        for key, instruction_file in config["instructions"].items():
            with open(instruction_file, "r") as f:
                self.instructions[key] = f.read().strip()

        self.max_iterations = config["max_iterations"]
        self.use_images = config.get("use_images", False)

    def run(self, tasks: Tasks, description: str): # ADD description parameter
        session = Session(self.config, description) # PASS description to Session

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
            prompt = []
            for i, pair in enumerate(task.train, 1):
                prompt.extend(get_pair_prompt(f"train_{i}", pair, self.use_images))

            if self.use_images:
                #  show full task image
                prompt.append(task.to_image(show_test=False))

            instructions = [self.instructions["investigate_dreamer"]]

            task_step = self._generate(
                session_task,
                "dreamer",
                title,
                history,
                prompt,
                instructions,
                tools="code_execution",
            )

            history.extend(prompt)
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
            print(f"        ERROR: Step '{title}' failed critically. Stopping investigation for task {task.id}.")
            # Error is already logged within _generate or by the exception handler in SessionTask/Level
            # We log the context of the failure here.
            session_task.log_error(e, f"Critical failure in step: {title}. Stopping investigation.")
            return # Stop investigation for this task

        # STEP: coder *********************************
        title = "investigate • coder • all training" # Define title here for except block
        try:
            instructions = [self.instructions["investigate_coder"]]
            prompt = [""] # Minimal prompt for coder based on history
            task_step = self._generate(
                session_task,
                "coder",
                title,
                history, # History includes dreamer prompt and response
                prompt,
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
            print(f"        ERROR: Step '{title}' failed critically. Stopping investigation for task {task.id}.")
            session_task.log_error(e, f"Critical failure in step: {title}. Stopping investigation.")
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
                print(f"        ERROR: Refinement iteration {current_iteration} failed critically. Stopping investigation for task {task.id}.")
                # Error is already logged within refine's exception handler before re-raising
                # We log the context of the failure during refinement here.
                session_task.log_error(e, f"Critical failure during refinement iteration {current_iteration}. Stopping investigation.")
                return # Stop investigation

            current_iteration += 1

        print(f"        INFO: Reached max iterations ({self.max_iterations}) without solving task {task.id}.")


    def _generate(
        self,
        session_task: SessionTask,
        role_name: str,
        title: str,
        history: list,
        prompt: list,
        instructions: list,
        tools=None,
        functions=None,
    ):
        """
        Generate content from the model, handling logging and retries.
        """

        # init step
        task_step = session_task.add_step(title, history, prompt, instructions)

        # --- Start of changes ---
        client = self.roles[role_name]
        max_retries = 1
        response = None
        start_time = datetime.now()  # Start timer before loop

        while task_step.attempts < max_retries:
            total_prompt = history + prompt + instructions

            # If not successful, wait a bit before retrying
            if task_step.attempts > 0:
                #  timeout = 10 * task_step.attempts
                timeout = 10
                print( f"        ...waiting  {timeout} seconds before retry ")
                time.sleep(timeout)  

            task_step.attempts += 1

            try:
                response = client.generate_content(total_prompt, tools=tools)

                # Check for valid response
                # FinishReason(1) is STOP
                if response.candidates and response.candidates[0].finish_reason == 1:
                    # Check if text is accessible (might still fail for safety/other reasons even with STOP)
                    try:
                        _ = response.text  # Attempt access
                        # Valid response received
                        break
                    except ValueError as ve:
                        # Finish reason is STOP, but text is not accessible
                        finish_reason = (
                            response.candidates[0].finish_reason
                            if response.candidates
                            else "UNKNOWN"
                        )
                        finish_reason_str = getattr(
                            finish_reason, "name", str(finish_reason)
                        )  # Get enum name
                        print(
                            f"        Attempt {task_step.attempts}/{max_retries} - Response finished (Reason: {finish_reason_str}), but text not accessible: {ve}"
                        )

                        if task_step.attempts == max_retries:
                            exc = Exception("Could not complete step - exit task")
                            raise exc


                else:
                    # Handle cases with no candidates or non-STOP finish reasons
                    finish_reason = (
                        response.candidates[0].finish_reason
                        if response.candidates
                        else "NO_CANDIDATES"
                    )
                    finish_reason_str = getattr(
                        finish_reason, "name", str(finish_reason)
                    )  # Get enum name
                    print(
                        f"        Attempt {task_step.attempts}/{max_retries} - Invalid response or finish reason: {finish_reason_str}"
                    )
                    if task_step.attempts == max_retries:
                        exc = Exception("Could not complete step - exit task")
                        raise exc

            except Exception as e:
                print(
                    f"        Attempt {task_step.attempts}/{max_retries} - ERROR: {e}"
                )
                # Log the exception potentially? For now, just print and retry.


        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        if response is None:
            # Handle case where all retries failed to even get a response object
            error_msg = (
                f"ERROR: Failed to get response from API after {max_retries} attempts."
            )
            print(f"        {error_msg}")
            # You might want to raise an exception here or log it more formally
            # For now, we'll create a placeholder response or skip logging
            # Let's skip logging response if it's None, but log the step error
            exc = Exception(error_msg)
            task_step.log_error(exc, "API Call Failure") # Use exc instead of e
            #  return task_step  # Or raise an exception depending on desired flow
            raise exc

        # Proceed with logging the (potentially invalid) response if one was received
        task_step.log_response(response, response_time)
        # --- End of changes ---

        # The rest of the function remains the same:
        reponse_parts = task_step.process_response(response)

        return task_step

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
            prompt = []
            instructions = [self.instructions["refine_dreamer"]]

            prompt.append("\nPrevious Code:\n")
            prompt.append(f"```python\n{code}\n```\n")
            prompt.append(code_trial.generate_report())

            task_step = self._generate(
                session_task,
                "dreamer",
                title,
                current_history, # Pass the history up to this point
                prompt,
                instructions,
                tools="code_execution",
            )
            # Update history *within this refinement iteration*
            current_history.extend(prompt)
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
            prompt = [""]  # Coder prompt might be minimal, relies on history
            instructions = [self.instructions["refine_coder"]]

            # Use the updated current_history (including dreamer output)
            task_step = self._generate(
                session_task,
                "coder",
                title,
                current_history, # Pass history including dreamer's output
                prompt,
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
