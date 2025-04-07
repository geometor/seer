"""Defines the TaskStep class, representing a single step within a SessionTask."""
from __future__ import annotations
from typing import TYPE_CHECKING

import re
from datetime import datetime # Keep for log_warning
from geometor.seer.session.level import Level

from google.generativeai.types import GenerateContentResponse
# Removed commented-out FinishReason import
# Import FinishReason enum if needed for direct comparison, or rely on integer values
# from google.generativeai.types import FinishReason

if TYPE_CHECKING:
    from geometor.seer.session.session_task import SessionTask

from geometor.seer.trials.code_trial import CodeTrial
from geometor.seer.trials.step_code_trials import StepCodeTrials


class TaskStep(Level):
    def __init__(
        self,
        title: str,
        history: list,
        content: list, # Renamed from prompt in SessionTask.add_step call
        instructions: list,
        session_task: SessionTask,
        model_name: str | None = None, # Add model_name parameter
    ):
        index = f"{len(session_task.steps):03d}"
        super().__init__(session_task, index)

        self.session_task = session_task  # parent
        self.model_name = model_name # Store the model name
        self.title = title
        self.index = index

        self.attempts = 0
        self.response = {}
        self.response_parts = []
        self.response_time = None
        self.codes = {}
        self.function_calls = {}
        self.step_code_trials = StepCodeTrials(self)  # Use StepCodeTrials

        self.history = history
        self.log_markdown("prompt_history", history)
        self.content = content
        self.log_markdown("prompt_content", content)
        self.instructions = instructions
        self.log_markdown("prompt_instructions", instructions)

        print(f"        {self.index} • {self.title}")

    # --- Start of added method ---
    def log_warning(self, message: str, context: str = ""):
        """Logs a warning message to warnings.txt."""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}]"
        if context:
            log_entry += f" Context: {context}"
        log_entry += f"\nWarning: {message}\n---\n"

        try:
            # Append warning to the file
            self._write_to_file("warnings.txt", log_entry, mode="a")
            # Also print the warning for immediate visibility
            print(f"        WARNING: {message}" + (f" (Context: {context})" if context else ""))
        except Exception as e:
            # Fallback if logging fails
            print(f"        CRITICAL: Failed to log warning: {message}. Error: {e}")
    # --- End of added method ---

    def summarize(self):
        try:
            # Get base summary (now includes 'has_errors' and 'duration_seconds')
            summary = super().summarize()
            # has_errors is now directly obtained from super().summarize()

            # Initialize summary structure, incorporating base summary values
            step_summary = {
                "index": self.index,
                "title": self.title,
                "duration_seconds": summary.get("duration_seconds"),
                "has_errors": summary.get("has_errors", False), # Use value from super()
                "attempts": self.attempts,
                "response": {
                    "response_time": self.response_time,
                    # Token counts added later
                },
                "py": "py" in self.codes, # Add 'py' boolean key
                # "codes": {}, # Replaced by 'py' key
                # "errors" key removed
            }

            # --- Analyze Trial Data only if trials exist ---
            all_trials = self.step_code_trials.get_all_trials()
            if all_trials: # Check if there are any CodeTrial objects
                # Convert CodeTrial objects to dictionaries
                # Note: Keeping the hasattr check as a safeguard for now.
                trial_data_list = [
                    ct.to_dict()
                    for ct in all_trials
                    if hasattr(ct, 'to_dict') # Check if the object has the method
                ]
                if not trial_data_list and all_trials:
                     # Log a warning if trials exist but none have to_dict
                     self.log_warning("Found CodeTrial objects missing the 'to_dict' method during summarization.", "TaskStep Summarize")

                # Only analyze and add trial results if we have data dictionaries
                if trial_data_list:
                    # Analyze the data
                    trial_analysis = StepCodeTrials.analyze_trial_data(trial_data_list)

                    # Add analysis results to the step_summary
                    # Only add keys if they have meaningful values from the analysis
                    if trial_analysis["best_score"] is not None:
                        step_summary["best_score"] = trial_analysis["best_score"]
                    if trial_analysis["any_train_passed"] is not None:
                        step_summary["train_passed"] = trial_analysis["any_train_passed"]
                    if trial_analysis["any_test_passed"] is not None:
                        step_summary["test_passed"] = trial_analysis["any_test_passed"]

                    # Add best trial metrics directly only if they are not all None
                    best_metrics = trial_analysis["best_trial_metrics"]
                    if any(v is not None for v in best_metrics.values()):
                        step_summary.update(best_metrics)

            # --- End Conditional Trial Analysis Integration ---

            # Add token counts to the response dict within step_summary
            if hasattr(self.response, "usage_metadata"):
                step_summary["response"]["prompt_tokens"] = (
                    self.response.usage_metadata.prompt_token_count
                )
                step_summary["response"]["candidates_tokens"] = (
                    self.response.usage_metadata.candidates_token_count
                )
                step_summary["response"]["total_tokens"] = (
                    self.response.usage_metadata.total_token_count
                )
            else:
                step_summary["response"]["prompt_tokens"] = None
                step_summary["response"]["candidates_tokens"] = None
                step_summary["response"]["total_tokens"] = None

            # Removed "codes" summary section (replaced by "py" key earlier)

            # --- START: Add Best Trial Metrics Directly to Summary ---
            # This section was already correctly handled by trial_analysis result above
            # best_trial = self.step_code_trials.get_best_trial()
            # # Initialize keys expected by TaskScreen with default None
            # summary["size_correct"] = None
            # summary["palette_correct"] = None
            # summary["colors_correct"] = None
            # summary["pixels_off"] = None
            # summary["percent_correct"] = None
            #
            # if (
            #     best_trial
            #     and best_trial.train_results # Check if train_results exist
            #     and best_trial.train_results.get("trials") # Check if 'trials' key exists within train_results
            # ):
            #     train_trials = best_trial.train_results["trials"]
            #     if train_trials: # Ensure there are trials to process
            #         # Calculate metrics based on train_trials (list of TaskPairTrial)
            #         size_correct_list = [t.size_correct for t in train_trials]
            #         palette_correct_list = [t.color_palette_correct for t in train_trials]
            #         color_count_correct_list = [t.color_count_correct for t in train_trials]
            #         pixels_off_list = [t.pixels_off for t in train_trials if t.pixels_off is not None]
            #         percent_correct_list = [t.percent_correct for t in train_trials if t.percent_correct is not None]
            #         total_pixels_off = sum(pixels_off_list) if pixels_off_list else None
            #
            #         # Add calculated metrics directly to summary using expected keys
            #         # Note: The keys here ('size_correct', 'palette_correct', etc.) should match
            #         # the keys expected by the TaskScreen DataTable.
            #         summary["size_correct"] = all(size_correct_list)
            #         summary["palette_correct"] = all(palette_correct_list)
            #         summary["colors_correct"] = all(color_count_correct_list)
            #         summary["pixels_off"] = total_pixels_off # Use total pixels off for the PIXELS column
            #         summary["percent_correct"] = sum(percent_correct_list) / len(percent_correct_list) if percent_correct_list else None # Use average for % column

            # Note: best_score, train_passed, test_passed, attempts, has_errors, response_time, tokens are already added to step_summary above

            # --- END: Add Best Trial Metrics Directly to Summary ---

            self._write_to_json("index.json", step_summary) # Write the final step_summary
            return step_summary  # Ensure summary is returned

        except Exception as e:
            self.log_error(e, f"Error during summarization of TaskStep: {self.title}")
            # Ensure has_errors is set even if summarization fails later
            summary = super().summarize() # Get base summary again (contains has_errors=True now)
            minimal_summary = {
                 "index": self.index,
                 "title": self.title,
                 "duration_seconds": summary.get("duration_seconds"),
                 "has_errors": True, # Mark as having errors explicitly
            }
            self._write_to_json("index.json", minimal_summary) # Try to save minimal summary
            return None  # Return None on error

    def _summarize_trial_results(self, results):
        """Helper function to summarize trial results."""
        num_trials = len(results)
        num_passed = sum(1 for r in results if r.match)  # Use .match directly
        num_failed = num_trials - num_passed

        summary = {
            "total": num_trials,
            "passed": num_passed,
            "failed": num_failed,
        }

        pixels_off_values = [r.pixels_off for r in results if r.pixels_off is not None]  # Use .pixels_off
        if pixels_off_values:
            summary["pixels_off"] = {
                "min": min(pixels_off_values),
                "max": max(pixels_off_values),
                "avg": sum(pixels_off_values) / len(pixels_off_values),
            }

        percent_correct_values = [r.percent_correct for r in results if r.percent_correct is not None]  # Use .percent_correct
        if percent_correct_values:
            summary["percent_correct"] = {
                "min": min(percent_correct_values),
                "max": max(percent_correct_values),
                "avg": sum(percent_correct_values) / len(percent_correct_values),
            }
        return summary

    def log_response(self, response: GenerateContentResponse, response_time: float, retries: int | None = None):
        self.response = response
        self.response_time = response_time  # seconds

        # gemini response object cannot be dumped directly
        response_dict = response.to_dict() if response else {} # Handle None response
        response_dict["response_time"] = response_time
        response_dict["retries"] = retries # ADDED retries count

        self._write_to_json("response.json", response_dict)

        # --- Start of changes ---
        # Robustly log response text or reason for absence
        response_log_content = []
        if response is None:
            response_log_content.append("Error: Response object is None (likely due to failed retries).")
        else:
            try:
                if response.candidates:
                    candidate = response.candidates[0]
                    finish_reason = candidate.finish_reason
                    # Use the enum value name if possible, otherwise the raw value
                    # FinishReason(1) is STOP
                    finish_reason_str = getattr(finish_reason, 'name', str(finish_reason))

                    if finish_reason == 1: # STOP
                        try:
                            # Attempt to access text, might raise ValueError if blocked (e.g., safety)
                            response_log_content.append(response.text)
                        except ValueError as e:
                            response_log_content.append(f"Error: Response finished normally (STOP) but text could not be accessed. Detail: {e}")
                            # Optionally log safety ratings if available
                            if hasattr(candidate, 'safety_ratings') and candidate.safety_ratings:
                                 response_log_content.append(f"Safety Ratings: {candidate.safety_ratings}")
                    else:
                        response_log_content.append(f"Warning: Response generation stopped. Finish Reason: {finish_reason_str} ({finish_reason})")
                        # Optionally include safety ratings if available and relevant
                        if hasattr(candidate, 'safety_ratings') and candidate.safety_ratings:
                             response_log_content.append(f"Safety Ratings: {candidate.safety_ratings}")
                        # Log text if available even if finish reason != STOP (e.g. MAX_TOKENS might have partial text)
                        try:
                            partial_text = response.text
                            if partial_text:
                                response_log_content.append("\nPartial text available:\n---\n")
                                response_log_content.append(partial_text)
                                response_log_content.append("\n---\n")
                        except ValueError:
                             response_log_content.append("(No text available to log)")


                else:
                    response_log_content.append("Error: No candidates found in the response.")
                    # Check for prompt feedback if available
                    if hasattr(response, 'prompt_feedback') and response.prompt_feedback:
                        response_log_content.append(f"Prompt Feedback: {response.prompt_feedback}")


            except Exception as e:
                # Catch any unexpected errors during response analysis
                response_log_content.append(f"Error: Unexpected issue processing response for logging: {e}")

        self.log_markdown("response", response_log_content)
        # --- End of changes ---


    def process_response(self, response: GenerateContentResponse):
        """Processes the response from the Gemini model."""
        response_parts = []

        # Check if response is None (could happen if _generate failed all retries)
        if response is None:
            error_msg = "Cannot process response: Response object is None."
            self.log_error(Exception(error_msg), "Process Response") # Log as error
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts

        # Check for prompt feedback first (indicates blocking before generation)
        if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
            block_reason = response.prompt_feedback.block_reason
            block_reason_str = getattr(block_reason, 'name', str(block_reason))
            error_msg = f"Prompt blocked. Reason: {block_reason_str}"
            self.log_error(Exception(error_msg), "Prompt Blocked") # Log the blocking reason as error
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            # Optionally log safety ratings associated with the prompt feedback
            if response.prompt_feedback.safety_ratings:
                response_parts.append(f"Prompt Safety Ratings: {response.prompt_feedback.safety_ratings}\n")
            return response_parts # Stop processing if prompt was blocked


        if not response.candidates:
            error_msg = "No candidates returned in response."
            self.log_error(Exception(error_msg), "Process Response - No Candidates") # Log as error
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts

        # Check finish reason and safety ratings of the first candidate
        candidate = response.candidates[0]
        finish_reason = candidate.finish_reason
        finish_reason_str = getattr(finish_reason, 'name', str(finish_reason))

        # Log a warning if finish reason is not STOP, but still attempt to process parts
        if finish_reason != 1: # Not STOP
             # Use the newly added log_warning method
             self.log_warning(f"Response generation finished with reason: {finish_reason_str}. Processing available parts.")
             if candidate.safety_ratings:
                 # Log safety ratings as part of the warning context or separately
                 self.log_warning(f"Safety Ratings: {candidate.safety_ratings}", context=f"Finish Reason: {finish_reason_str}")


        # Attempt to access content parts, handling potential errors
        try:
            if not hasattr(candidate.content, "parts"):
                # This might happen if finish_reason is e.g., SAFETY
                error_msg = f"No content parts in response candidate. Finish Reason: {finish_reason_str}."
                self.log_error(Exception(error_msg), f"Process Response - No Parts (Finish Reason: {finish_reason_str})") # Log as error
                response_parts.append("\n*error:*\n")
                response_parts.append(error_msg + "\n")
                if candidate.safety_ratings:
                    response_parts.append(f"Safety Ratings: {candidate.safety_ratings}\n")
                return response_parts

            for part in candidate.content.parts:
                if hasattr(part, 'text') and part.text:
                    response_parts.append(part.text + "\n")
                    self._parse_code_text(part.text)

                if hasattr(part, 'executable_code') and part.executable_code:
                    response_parts.append("\n*code_execution:*\n")
                    code = part.executable_code.code
                    response_parts.append(f"```python\n{code}\n```\n")

                if hasattr(part, 'code_execution_result') and part.code_execution_result:
                    response_parts.append("\n*code_execution_result:*\n")
                    outcome = part.code_execution_result.outcome
                    outcome_str = getattr(outcome, 'name', str(outcome)) # Get enum name
                    output = part.code_execution_result.output
                    response_parts.append(f"outcome: {outcome_str}\n")
                    response_parts.append(f"```\n{output}\n```\n")

                if hasattr(part, 'function_call') and part.function_call:
                    response_parts.append("\n*function_call:*\n")
                    response_parts.append(part.function_call.name + "\n")
                    self.function_calls[part.function_call.name] = part.function_call

        except ValueError as ve:
            # Catch errors accessing parts, often due to safety blocks after generation started
            error_msg = f"Error accessing response parts, potentially due to safety settings or other issues. Finish Reason: {finish_reason_str}. Detail: {ve}"
            self.log_error(ve, f"Process Response - Access Error (Finish Reason: {finish_reason_str})") # Log as error
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            if candidate.safety_ratings:
                response_parts.append(f"Safety Ratings: {candidate.safety_ratings}\n")
        except Exception as e:
            # Catch any other unexpected errors during part processing
            error_msg = f"Unexpected error processing response parts: {e}"
            self.log_error(e, "Process Response - Unexpected Error") # Log as error
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")


        self.response_parts = response_parts
        return response_parts


    def _parse_code_text(self, text: str):
        """Extracts code blocks, writes them, and returns file info."""

        def get_code_file_count():
            return len(list(self.dir.glob("code*")))

        matches = re.findall(r"```(\w+)\n(.*?)\n```", text, re.DOTALL)
        for file_type, content in matches:
            file_type = file_type.lower() if file_type else "txt"
            if file_type == "python":
                file_type = "py"

            index = get_code_file_count()
            file_name = f"code_{index:02d}.{file_type}"

            self._write_to_file(file_name, content)

            # add code to dict
            if file_type not in self.codes:
                self.codes[file_type] = {}

            self.codes[file_type][file_name] = content

    def run_functions(self, functions):
        # TODO: complete implementation
        for func_name, func_call in self.function_calls.items():
            try:
                result, msg = self._call_function(
                    func_call,
                    functions,
                )
                # TODO: store results

            except Exception as e:
                #  print(f"\nERROR: {str(e)}")
                self.log_error(e, func_name)

    def _call_function(
        self,
        function_call,
        functions: dict,
    ):
        """Execute a function call with improved error handling."""
        if not functions:
            raise ValueError("No functions provided")

        function_name = function_call.name
        function_args = function_call.args

        # TODO: Complete implementation or remove placeholder logic
        pass

    def run_trials(self):
        """Executes trials for all available code."""
        self.step_code_trials.run_trials()

    def get_first_code_trial(self) -> CodeTrial | None:
        """Retrieves the first CodeTrial object, if any."""
        return self.step_code_trials.get_first_code_trial()

    def any_trials_successful(self, set_type="train"):
        """Checks if any trials of the given type were successful."""
        if set_type == "train":
            return self.step_code_trials.any_train_passed
        elif set_type == "test":
            return self.step_code_trials.any_test_passed
        return False

    @property
    def train_passed(self):
        return self.step_code_trials.any_train_passed  # Consistent with summarize

    @property
    def test_passed(self):
        return self.step_code_trials.any_test_passed  # Consistent with summarize


    def log_warning(self, message: str, context: str = ""):
        """Logs a warning message to the step's warnings.txt."""
        # Delegate to parent (SessionTask) or implement directly if Level gets log_warning
        # For now, let's delegate to SessionTask which has the method
        if hasattr(self.session_task, 'log_warning'):
             # Prepend step context
             full_context = f"Step {self.index} ({self.title})"
             if context:
                 full_context += f" - {context}"
             self.session_task.log_warning(message, full_context)
        else:
             # Fallback if parent doesn't have it (should not happen with current code)
             print(f"        WARNING (Step {self.index}): {message}" + (f" (Context: {context})" if context else ""))


    @property
    def get_python(self) -> dict:
        """Safely returns the Python code dictionary or an empty dictionary."""
        return self.codes.get("py", {})
