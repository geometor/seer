import re
from pathlib import Path
from typing import List, Tuple, Any

from geometor.seer.exceptions import (
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)

class ResponseHandler:
    def __init__(self, session):
        self.session = session

    def process_response(
        self, response: Any, functions: dict, total_prompt: List[str], prompt_count: int, extracted_file_counts: dict
    ) -> Tuple[List[str], List[Tuple[str, str, str]]]:
        """Processes the response from the Gemini model."""
        response_parts = []
        extracted_code_list = []

        if not response.candidates:
            error_msg = "No candidates returned in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts, extracted_code_list

        if not hasattr(response.candidates[0].content, "parts"):
            error_msg = "No content parts in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")
            response_parts.append(error_msg + "\n")
            return response_parts, extracted_code_list

        for part in response.candidates[0].content.parts:
            if part.text:
                response_parts.append(part.text + "\n")
                extracted_code = self._parse_code_text(part.text, prompt_count, extracted_file_counts)
                extracted_code_list.extend(extracted_code)

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
                self.session._write_to_file(
                    f"{prompt_count:03d}-code_result.txt", output
                )

            if part.function_call:
                response_parts.append("\n*function_call:*\n")
                response_parts.append(part.function_call.name + "\n")

                try:
                    result, msg = self._call_function(
                        part.function_call, functions, total_prompt
                    )
                    response_parts.append("\nresult:\n")
                    response_parts.append(f"{result}\n")
                    response_parts.append(f"{msg}\n")

                except (UnknownFunctionError, FunctionArgumentError, FunctionExecutionError) as e:
                    print(f"\nERROR: {str(e)}")
                    self.session.log_error(str(e), "".join(total_prompt))
                    response_parts.append(f"\n*error:*\n{str(e)}\n")


        return response_parts, extracted_code_list

    def _parse_code_text(self, text: str, prompt_count:int, extracted_file_counts: dict) -> List[Tuple[str, str, str]]:
        """Extracts code blocks, writes them, and returns file info."""
        matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)
        extracted_code = []
        for file_type, content in matches:
            file_type = file_type.lower() if file_type else "txt"
            if file_type == "python":
                file_type = "py"

            # Write to file and get the *full path*
            file_path_str = self.session._write_code_text(
                [(file_type, content)],
                prompt_count,
                extracted_file_counts
            )

            file_path = Path(file_path_str)
            filename = file_path.name
            base_filename = file_path.stem
            extracted_code.append((file_type, content, base_filename))
        return extracted_code

    def _call_function(self, function_call: Any, functions: dict, total_prompt: List[str]):
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
