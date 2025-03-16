from datetime import datetime
from pathlib import Path
import json
import traceback
from PIL import Image

#  from geometor.seer.session.session_task import SessionTask


class TaskStep:
    def __init__(
        self,
        title: str,
        history: list,
        prompt: list,
        instructions: list,
        session_task,
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

    def log_error(self, e: Exception, context: str = ""):
        # TODO: refactor to generic function
        error_content = {
            "context": context,
            "datetime": datetime.now().isoformat(),
            "stack_trace": traceback.format_exc(),
            "exception": e,
        }
        error_index = len(self.errors) + 1

        error_log_file = self.dir / f"error_{error_index:03d}.json"

        self._write_to_json(error_log_file, error_content)

        self.errors[error_log_file.name] = error_content

    def summarize():
        # TODO: construct summary
        summary = {}
        self._write_to_json("step_summary.json", summary)

    def log_markdown(
        self,
        name: str,
        content: list,
    ):
        markdown_file = self.dir / f"{name}.md"
        try:
            with open(markdown_file, "w") as f:
                for i, part in enumerate(content):
                    if isinstance(part, Image):
                        image_filename = f"{description}.png"
                        image_path = self.dir / image_filename
                        image.to_image().save(image_path)
                        f.write(part)
                    else:
                        f.write(str(part))
        except Exception as e:
            # TODO: print not supported in textual
            print(f"Error writing prompt to file: {e}")
            self.log_error(f"Error writing prompt to file: {e}")

    def log_response(self, response, response_time):
        self.response = response
        self.response_time = response_time

        # gemini response object cannot be dumped directly
        response_dict = response.to_dict()
        response_dict["response_time"] = response_time

        self._write_to_json("response.json", response_dict)

    def process_response(self, response):
        """Processes the response from the Gemini model."""
        response_parts = []

        if not response.candidates:
            error_msg = "No candidates returned in response."
            #  print(f"\nERROR: {error_msg}")
            self.log_error(error_msg)
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts, extracted_code_list

        if not hasattr(response.candidates[0].content, "parts"):
            error_msg = "No content parts in response."
            #  print(f"\nERROR: {error_msg}")
            self.log_error(error_msg)
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts, extracted_code_list

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
                self.session._write_to_file(f"code_result.txt", output)

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

        matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)
        for file_type, content in matches:
            file_type = file_type.lower() if file_type else "txt"
            if file_type == "python":
                file_type = "py"

            index = get_code_file_count()
            file_name = f"code_{index:02d}.{file_type}"

            self._write_to_file(file_name, content)

            # add code to dict
            if not self.codes[file_type]:
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

    def _write_to_json(self, file_name: str, content):
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

        if function_name not in functions:
            raise UnknownFunctionError(f"Unknown function: {function_name}")

        try:
            result = functions[function_name](**function_args)
            return result
        except TypeError as e:
            raise FunctionArgumentError(
                f"Invalid arguments for {function_name}: {str(e)}"
            )
        except Exception as e:
            raise FunctionExecutionError(f"Error executing {function_name}: {str(e)}")

    def run_trial(self):
        # TODO: this function cannot call refine if we are already in a refine loop
        #  train_results = []
        #  test_results = []
        results = 

        # Iterate and test *all* code blocks
        if not self.codes["py"]:
            return

        for file_name, code in self.codes["py"]:
            current_train_results = verifier.test_code_with_timeout(
                code,
                task.train,
            )
            verifier.write_test_results(
                current_train_results,
                self.dir,
                base_filename + "-train",
            )
            if "trials" in current_train_results:
                train_image = task.to_image(
                    train_results=current_train_results, show_test=False
                )

                # TODO: save image
                train_image_filename = f"{base_filename}-train_results.png"
                train_image_path = self.dir / train_image_filename
                train_image.save(train_image_path)

                all_train_passed = all(
                    result.get("match") is True
                    for result in current_train_results["trials"]
                )

                if all_train_passed:
                    current_test_results = verifier.test_code_with_timeout(
                        code,
                        task.test,
                    )
                    verifier.write_test_results(
                        current_test_results,
                        self.dir,
                        base_filename + "-test",
                    )

                    if "trials" in current_test_results:
                        test_image = task.to_image(
                            train_results=current_train_results,
                            test_results=current_test_results,
                        )
                        # TODO: save image
                        test_image_filename = f"{base_filename}-test_results.png"
                        test_image_path = self.dir / test_image_filename
                        test_image.save(test_image_path)

                        all_test_passed = all(
                            result.get("match") is True
                            for result in current_test_results["examples"]
                        )  # Use current_test_results
                        if all_test_passed:
                            self.task_solved = True  # Set the flag
                            break  # Exit the loop *after* setting the flag
                else:
                    if self.current_iteration <= self.max_iterations:
                        #  if not self.task_solved:
                        self.refine(
                            task, train_results, test_results, code, base_filename
                        )
