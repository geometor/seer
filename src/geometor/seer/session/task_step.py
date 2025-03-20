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
        self.trials = {}

        self.history = history
        self.log_markdown("history", history)
        self.prompt = prompt
        self.log_markdown("prompt", prompt)
        self.instructions = instructions
        self.log_markdown("instructions", instructions)

        #  self.current_iteration = 0

        print(f"        {self.index} • {self.title}")

    def summarize(self):
        # TODO: construct summary
        summary = {
                "title": self.title,
                "index": self.index,
                "prompt": self.response.usage_metadata.prompt_token_count,
                "candidates": self.response.usage_metadata.candidates_token_count,
                "total": self.response.usage_metadata.total_token_count,
                "errors": len(self.errors),
                "codes": len(self.codes),
                "trials": len(self.trials),
                
                "title": self.title,
                }
        self._write_to_json("step_summary.json", summary)

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

    def run_trials(self, task):
        # TODO: step_code_trials should be an object like code trials
        step_code_trials = {
                "any_train_passed": False, # overall
                "any_test_passed": False,  # overall
                "code_trials": {},
                }

        if "py" not in self.codes:
            #  self.log_error(Exception("No python code to run"), "run_trials")
            return step_code_trials

        for code_filename, code in self.codes["py"].items():
            code_trial = CodeTrial(self, code_filename, code, task)
            step_code_trials["code_trials"][code_filename] = code_trial

        any_train_passed = any(
            trial.train_passed for trial in step_code_trials["code_trials"].values()
        )
        any_test_passed = any(
            trial.test_passed for trial in step_code_trials["code_trials"].values()
        )
        step_code_trials["any_train_passed"] = any_train_passed
        step_code_trials["any_test_passed"] = any_test_passed

        return step_code_trials


