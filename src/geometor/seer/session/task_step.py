from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from pathlib import Path
import json
import re
import traceback
from PIL import Image

from google.generativeai.types import GenerateContentResponse

if TYPE_CHECKING:
    from geometor.seer.session.session_task import SessionTask


from geometor.seer import verifier
from geometor.seer.trial_result import CodeTrial
from geometor.seer.step_code_trials import StepCodeTrials  # Import


class TaskStep:
    def __init__(
        self,
        title: str,
        history: list,
        prompt: list,
        instructions: list,
        session_task: SessionTask,
    ):
        self.session_task = session_task  # parent
        self.title = title
        self.index = f"{len(session_task.steps):03d}"

        self.dir = session_task.dir / self.index
        self.dir.mkdir(parents=True, exist_ok=True)

        self.response = {}
        self.response_parts = []
        self.response_time = None
        self.errors = {}
        self.codes = {}
        self.function_calls = {}
        # self.trials = {}  # Initialize trials -- REMOVE, replaced by step_code_trials
        self.step_code_trials = StepCodeTrials() # Use StepCodeTrials

        self.history = history
        self.log_markdown("history", history)
        self.prompt = prompt
        self.log_markdown("prompt", prompt)
        self.instructions = instructions
        self.log_markdown("instructions", instructions)

        #  self.current_iteration = 0

        print(f"        {self.index} • {self.title}")

    def summarize(self):
        summary = {
            "title": self.title,
            "index": self.index,
            "response": {
                "response_time": self.response_time,
            },
            "errors": {},
            "trials": {},
            "codes": {},
        }

        if hasattr(self.response, 'usage_metadata'):
            summary["response"]["prompt_tokens"] = self.response.usage_metadata.prompt_token_count
            summary["response"]["candidates_tokens"] = self.response.usage_metadata.candidates_token_count
            summary["response"]["total_tokens"] = self.response.usage_metadata.total_token_count
        else:
            summary["response"]["prompt_tokens"] = None
            summary["response"]["candidates_tokens"] = None
            summary["response"]["total_tokens"] = None

        summary["errors"]["count"] = len(self.errors)
        summary["errors"]["types"] = list(self.errors.keys())  # List of error file names

        summary["codes"]["count"] = len(self.codes)
        summary["codes"]["types"] = list(self.codes.keys())

        # --- Trial Summary ---
        all_train_results = []
        all_test_results = []
        # Iterate through CodeTrial objects in StepCodeTrials
        for code_trial in self.step_code_trials.get_all_trials():
            if code_trial.train_results:
                all_train_results.extend(code_trial.train_results.get("trials", []))
            if code_trial.test_results:
                all_test_results.extend(code_trial.test_results.get("trials", []))

        if all_train_results:
            summary["trials"]["train"] = self._summarize_trial_results(all_train_results)
        if all_test_results:
            summary["trials"]["test"] = self._summarize_trial_results(all_test_results)

        self._write_to_json("step_summary.json", summary)

    def _summarize_trial_results(self, results):
        """Helper function to summarize trial results."""
        num_trials = len(results)
        num_passed = sum(1 for r in results if r.get("match", False))
        num_failed = num_trials - num_passed

        summary = {
            "total": num_trials,
            "passed": num_passed,
            "failed": num_failed,
        }

        pixels_off_values = [r.get("pixels_off") for r in results if "pixels_off" in r]
        if pixels_off_values:
            summary["pixels_off"] = {
                "min": min(pixels_off_values),
                "max": max(pixels_off_values),
                "avg": sum(pixels_off_values) / len(pixels_off_values),
            }

        percent_correct_values = [
            r.get("percent_correct") for r in results if "percent_correct" in r
        ]
        if percent_correct_values:
            summary["percent_correct"] = {
                "min": min(percent_correct_values),
                "max": max(percent_correct_values),
                "avg": sum(percent_correct_values) / len(percent_correct_values),
            }
        return summary


    def log_error(self, e: Exception, context: str = ""):
        # TODO: refactor to generic function
        error_content = {
            "context": context,
            "datetime": datetime.now().isoformat(),
            "stack_trace": traceback.format_exc(),
            "exception": str(e),
        }
        error_index = len(self.errors) + 1

        error_log_file = f"error_{error_index:03d}.json"

        print("ERROR")
        print(context)
        print(str(e))
        print(error_content["stack_trace"])

        self._write_to_json(error_log_file, error_content)

        self.errors[error_log_file] = error_content

    def log_markdown(
        self,
        name: str,
        content: list,
    ):
        markdown_file = self.dir / f"{name}.md"
        try:
            with open(markdown_file, "w") as f:
                for i, part in enumerate(content):
                    if isinstance(part, Image.Image):
                        #  image_filename = f"{name}_{i}.png"  # Use name and index
                        image_filename = f"{name}_{i:03d}.png"  # Use name and index
                        image_path = self.dir / image_filename
                        part.save(image_path)
                        f.write(f"!\\[image {i}]({image_filename})\n")  # Correct markdown
                    else:
                        f.write(str(part))
        except Exception as e:
            # TODO: print not supported in textual
            print(f"Error writing prompt to file: {e}")
            self.log_error(f"Error writing prompt to file: {e}")

    def log_response(self, response: GenerateContentResponse, response_time: float):
        self.response = response
        self.response_time = response_time  # seconds

        # gemini response object cannot be dumped directly
        response_dict = response.to_dict()
        response_dict["response_time"] = response_time

        self._write_to_json("response.json", response_dict)
        self.log_markdown("response", response.text)

    def process_response(self, response: GenerateContentResponse):
        """Processes the response from the Gemini model."""
        response_parts = []

        if not response.candidates:
            error_msg = "No candidates returned in response."
            #  print(f"\nERROR: {error_msg}")
            self.log_error(error_msg)
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts

        if not hasattr(response.candidates[0].content, "parts"):
            error_msg = "No content parts in response."
            #  print(f"\nERROR: {error_msg}")
            self.log_error(error_msg)
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts

        for part in response.candidates[0].content.parts:
            if part.text:
                response_parts.append(part.text + "\n")

                self._parse_code_text(part.text)

            if part.executable_code:
                response_parts.append("\n*code_execution:*\n")
                code = part.executable_code.code
                response_parts.append(f"```python\n{code}\n```\n")

            if part.code_execution_result:
                response_parts.append("\n*code_execution_result:*\n")
                outcome = part.code_execution_result.outcome
                output = part.code_execution_result.output
                response_parts.append(f"outcome: {outcome}\n")
                response_parts.append(f"```\n{output}\n```\n")
                #  self.session._write_to_file(f"code_result.txt", output)

            if part.function_call:
                response_parts.append("\n*function_call:*\n")
                response_parts.append(part.function_call.name + "\n")

                self.function_calls[part.function_call.name] = part.function_call

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

    def _write_to_file(self, file_name: str, content: str):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except Exception as e:
            self.log_error(e, f"Error writing to file: {file_path}")

    def _write_to_json(self, file_name: str, content: object):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            with open(file_path, "w") as f:
                json.dump(content, f, indent=2)
        except Exception as e:
            self.log_error(e, f"Error writing to json: {file_path}")

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

        #  if function_name not in functions:
            #  raise UnknownFunctionError(f"Unknown function: {function_name}")

        #  # TODO: log errors
        #  try:
            #  result = functions[function_name](**function_args)
            #  return result
        #  except TypeError as e:
            #  raise FunctionArgumentError(
                #  f"Invalid arguments for {function_name}: {str(e)}"
            #  )
        #  except Exception as e:
            #  raise FunctionExecutionError(f"Error executing {function_name}: {str(e)}")

    def execute_trials(self, task):
        """Executes trials for all available code."""
        if "py" not in self.codes:
            return  # Nothing to do

        for code_filename, code in self.codes["py"].items():
            code_trial = CodeTrial(self, code_filename, code, task)
            code_trial.execute_and_save_results()
            # self.trials[code_filename] = code_trial  # No longer storing directly in TaskStep
            self.step_code_trials.add_code_trial(code_filename, code_trial) # Add to StepCodeTrials

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
