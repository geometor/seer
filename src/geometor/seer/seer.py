"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""
from rich import print
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os
import re
import ast
import contextlib
import io

from geometor.seer.tasks import Tasks, Task, Grid

from geometor.seer.gemini_client import GeminiClient as Client
from geometor.seer.exceptions import (
    MultipleFunctionCallsError,
    MaxRetriesExceededError,
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)
from geometor.seer.session import Session


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks with input/output pairs of training examples.
    """

    def __init__(
        self,
        config: dict,
        max_iterations: int = 5,
    ):
        self.config = config
        self.start_time = datetime.now()
        self.response_times = []

        self.nlp_model = config["nlp_model"]
        self.code_model = config["code_model"]

        with open(config["system_context_file"], "r") as f:
            self.system_context = f.read().strip()
        with open(config["task_context_file"], "r") as f:
            self.task_context = f.read().strip()

        with open("nlp_instructions.md", "r") as f:
            self.nlp_instructions = f.read().strip()
        with open("code_instructions.md", "r") as f:
            self.code_instructions = f.read().strip()

        self.max_iterations = config["max_iterations"]
        self.current_iteration = 0

        self.nlp_client = Client(
            self.nlp_model, f"{self.system_context}\n\n{self.task_context}"
        )
        self.code_client = Client(
            self.code_model, f"{self.system_context}\n\n{self.task_context}"
        )

        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

    def solve(
        self,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        self.prompt_count = 0
        self.task = task  # Store the task for use in _process_response and _test_code
        history = [""]

        self._investigate_examples(task.train)
        #  self._review_programs()
        #  self._run_solution_loop()

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = pair.input.to_string()
            output_grid_str = pair.output.to_string()

            prompt = [
                "\n**input**\n```\n",
                input_grid_str,
                "\n```\n\n",
            ]
            if include_images:
                prompt.append(pair.input.to_image())
                prompt.append("\n")
            prompt.append("\n**output**\n```\n")
            prompt.append(output_grid_str)
            prompt.append("\n```\n\n")
            if include_images:
                prompt.append(pair.output.to_image())
                prompt.append("\n")

            instructions = [self.nlp_instructions]
            response = self._generate(
                history,
                prompt,
                instructions,
                tools=None,
                description=f"example_{i} - NLP",
            )
            history.extend(prompt)
            history.extend(response)

            # Code Prompt
            instructions = [
                self.code_instructions.format(
                    input_grid_rows=pair.input.to_python_string(2),
                    expected_output_grid_rows=pair.output.to_python_string(2),
                )
            ]
            prompt = [""]
            response = self._generate(  # Use nlp_client, no tools
                history,
                prompt,
                instructions,
                tools="code_execution",
                description=f"example_{i} - CODE",
            )
            history.extend(prompt)
            history.extend(response)

    def _review_programs(self, instructions):
        """
        summarize observations on pairs
        """

        prompt = [""]
        instructions = [""]
        self._generate(
            prompt,
            instructions,
            #  tools="code_execution",
            description=f"example_summary",
        )

    def _generate(
        self, history, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.prompt_count += 1

        total_prompt = history + prompt + instructions

        self.session.logger.log_prompt(
            self.session.task_dir,
            prompt,
            instructions,
            self.prompt_count,
            description=description,
        )
        self.session.logger.log_total_prompt(
            self.session.task_dir,
            total_prompt,
            self.prompt_count,
            description=description,
        )

        #  history = history + prompt

        response = self.nlp_client.generate_content(
            total_prompt,
            tools=tools,
        )

        response_parts, function_call_found, last_result = self._process_response(
            response, functions, total_prompt
        )

        self.session.logger.log_response(
            self.session.task_dir,
            response,
            response_parts,
            self.prompt_count,
            self.token_counts,
            self.response_times,
            self.start_time,
        )

        #  history = history + response_parts

        return response_parts

    def _process_response(self, response, functions, total_prompt):
        """Processes the response from the Gemini model."""
        response_parts = []
        function_call_found = False
        last_result = None

        if hasattr(response.candidates[0].content, "parts"):
            for part in response.candidates[0].content.parts:
                if part.text:
                    response_parts.append("\n*text:*\n")
                    response_parts.append(part.text + "\n")
                    # Check for triple backticks and write to file
                    self._write_extracted_content(part.text)

                if part.executable_code:
                    response_parts.append("\n*code_execution:*\n")
                    code = part.executable_code.code
                    response_parts.append(f"```python\n{code}\n```\n")
                    code_file_path = self.session.task_dir / f"{self.prompt_count:03d}-code.py"
                    self._write_to_file(code_file_path, code)

                    # Call _test_code and extend response_parts
                    test_results = self._test_code(code, code_file_path)
                    response_parts.extend(test_results)  # Should now be an empty list


                if part.code_execution_result:
                    response_parts.append("\n*code_execution_result:*\n")
                    outcome = part.code_execution_result.outcome
                    output = part.code_execution_result.output
                    response_parts.append(f"outcome: {outcome}\n")
                    response_parts.append(f"```\n{output}\n```\n")
                    self._write_to_file(
                        f"{self.prompt_count:03d}-code_result.txt", output
                    )

                if part.function_call:
                    function_call_found = True
                    response_parts.append("\n*function_call:*\n")
                    response_parts.append(part.function_call.name + "\n")

                    result, msg = self._call_function(
                        part.function_call, functions, total_prompt
                    )
                    last_result = msg

                    response_parts.append("\nresult:\n")
                    response_parts.append(f"{result}\n")
                    response_parts.append(f"{msg}\n")

        return response_parts, function_call_found, last_result

    def _test_code(self, code, code_file_path):
        """Executes and validates the generated code, writing results to a file."""
        test_results_str = ""
        try:
            tree = ast.parse(code)
            namespace = {}
            # Capture stdout
            output_capture = io.StringIO()
            with contextlib.redirect_stdout(output_capture):
                exec(compile(tree, filename=str(code_file_path), mode="exec"), namespace)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == "transform":
                    test_results_str += "\n*validation:*\n"
                    for i, pair in enumerate(self.task.train):
                        input_grid = pair.input.grid
                        expected_output = pair.output.grid
                        try:
                            transformed_output = namespace["transform"](input_grid)
                            if not np.array_equal(transformed_output, expected_output):
                                test_results_str += (
                                    f"  Validation failed for example {i + 1}:\n"
                                )
                                test_results_str += f"    Input:\n{pair.input.to_string()}\n"
                                test_results_str += (
                                    f"    Expected Output:\n{pair.output.to_string()}\n"
                                )
                                test_results_str += (
                                    f"    Actual Output:\n{Grid(transformed_output).to_string()}\n"
                                )

                            else:
                                test_results_str += f"  Validation passed for example {i+1}\n"
                        except Exception as e:
                            test_results_str += (
                                f"  Error during validation for example {i + 1}: {e}\n"
                            )
                            self.session.logger.log_error(
                                self.session.task_dir,
                                f"Error during validation for example {i + 1}: {e}",
                            )
            captured_output = output_capture.getvalue()
            if captured_output:
                test_results_str += f"*captured output:*\n```\n{captured_output}\n```\n"

            # Write test results to file
            test_results_file = self.session.task_dir / f"{code_file_path.stem}.md"
            self._write_to_file(test_results_file, test_results_str)


        except SyntaxError as e:
            test_results_str += f"\n*code_execution_error:*\n```\n{e}\n```\n"
            self.session.logger.log_error(
                self.session.task_dir, f"SyntaxError in generated code: {e}"
            )
            # Write test results to file even on error
            test_results_file = self.session.task_dir / f"{code_file_path.stem}-test_results.txt"
            self._write_to_file(test_results_file, test_results_str)

        except Exception as e:
            test_results_str += f"\n*code_execution_error:*\n```\n{e}\n```\n"
            self.session.logger.log_error(
                self.session.task_dir, f"Error executing generated code: {e}"
            )
            # Write test results to file even on error
            test_results_file = self.session.task_dir / f"{code_file_path.stem}-test_results.txt"
            self._write_to_file(test_results_file, test_results_str)
        return []


    def _write_extracted_content(self, text):
        """Extracts content enclosed in triple backticks and writes it to files."""
        matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)
        for file_type, content in matches:
            file_type = file_type.lower() if file_type else "txt"
            if file_type == "python":
                file_type = "py"  # Correct extension
            if file_type not in self.extracted_file_counts:
                file_type = "txt"

            self.extracted_file_counts[file_type] += 1
            count = self.extracted_file_counts[file_type]
            file_name = f"{self.prompt_count:03d}-{file_type}_{count:02d}.{file_type}"
            self._write_to_file(file_name, content)

    def _write_to_file(self, file_name, content):
        """Writes content to a file in the task directory."""
        file_path = self.session.task_dir / file_name
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.session.logger.log_error(
                self.session.task_dir, f"Error writing to file {file_name}: {e}"
            )

    def _call_function(self, function_call, functions, total_prompt):
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

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.session.logger.log_error(
            self.session.task_dir, error_msg, "".join(total_prompt)
        )

    def run(self, tasks):
        """
        Runs the Seer over the set of tasks.
        """
        self.tasks = tasks  # Set tasks here
        self.prompt_count = 0
        self.session = Session(self.config, self.tasks)

        for task in self.tasks:
            self.session.task_dir = (
                self.session.session_dir / task.id
            )  # Set task_dir
            self.session.task_dir.mkdir(parents=True, exist_ok=True)

            self.solve(task)
