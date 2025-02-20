# src/geometor/seer/seer.py
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

from geometor.seer.tasks import Tasks, Task, Grid

#  from geometor.seer.oracle import Oracle  # Removed

from geometor.seer.gemini_client import GeminiClient as Client
from geometor.seer.exceptions import (
    MultipleFunctionCallsError,
    MaxRetriesExceededError,
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)
from geometor.seer.session import Session
from geometor.seer.verifier import Verifier  # Added
from geometor.seer.session.summary import summarize_session, summarize_task


class Seer:
    def __init__(
        self,
        config: dict,
        max_iterations: int = 5,
    ):
        self.config = config
        self.start_time = datetime.now()
        self.response_times = []

        self.roles = {}
        for role_name, role_config in config["roles"].items():
            self.roles[role_name] = Client(self.config, role_name)

        self.verifier = Verifier()  # Simplified instantiation
        with open(config["investigate_nlp"], "r") as f:
            self.nlp_instructions = f.read().strip()
        with open(config["investigate_code"], "r") as f:
            self.code_instructions = f.read().strip()

        self.max_iterations = config["max_iterations"]
        self.current_iteration = 0

        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

    def solve(
        self,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        self.session.task_dir = self.session.session_dir / task.id
        self.session.task_dir.mkdir(parents=True, exist_ok=True)

        self.prompt_count = 0
        self.task = task
        history = [""]

        # Reset extracted file counts for each task
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

        self._investigate_examples(task.train)
        #  self._review_programs()
        #  self._run_solution_loop()

        summarize_task(self.session.task_dir, self.session.log_error)

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = pair.input.to_string()
            output_grid_str = pair.output.to_string()

            # dreamer prompt
            prompt = [
                "\n**input**\n```\n",
                input_grid_str,
                "\n```\n\n",
            ]
            if include_images:
                # Get image filename from log_prompt
                input_image_filename = self.session.log_prompt_image(
                    pair.input, self.prompt_count + 1, f"example_{i}_input"
                )
                prompt.append(f"![Image]({input_image_filename})\n")
                #  prompt.append(pair.input.to_image()) # OLD
                prompt.append("\n")
            prompt.append("\n**output**\n```\n")
            prompt.append(output_grid_str)
            prompt.append("\n```\n\n")
            if include_images:
                # Get image filename from log_prompt
                output_image_filename = self.session.log_prompt_image(
                    pair.output, self.prompt_count + 1, f"example_{i}_output"
                )
                prompt.append(f"![Image]({output_image_filename})\n")
                #  prompt.append(pair.output.to_image()) # OLD
                prompt.append("\n")

            instructions = [self.nlp_instructions]
            response_parts, elapsed_time = self._generate(
                "dreamer",
                history,
                prompt,
                instructions,
                #  tools=None,
                description=f"example_{i} - NLP",
            )
            history.extend(prompt)
            history.extend(response_parts)

            # coder prompt
            instructions = [
                self.code_instructions.format(
                    input_grid_rows=pair.input.to_python_string(),
                    expected_output_grid_rows=pair.output.to_python_string(),
                )
            ]
            prompt = [""]
            response_parts, elapsed_time = self._generate(
                "coder",
                history,
                prompt,
                instructions,
                #  tools="code_execution",
                description=f"example_{i} - CODE",
            )
            history.extend(prompt)
            history.extend(response_parts)

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
        self,
        role_name,
        history,
        prompt,
        instructions,
        tools=None,
        functions=None,
        description="",
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        Now accepts role_name instead of client object.
        Returns elapsed time.
        """
        self.prompt_count += 1

        total_prompt = history + prompt + instructions

        self.session.log_prompt(
            prompt,
            instructions,
            self.prompt_count,
            description=description,
        )
        self.session.log_total_prompt(
            total_prompt,
            self.prompt_count,
            description=description,
        )

        client = self.roles[role_name]  # Look up the client
        start_time = datetime.now()  # Record start time
        response = client.generate_content(
            total_prompt,
            tools=tools,
        )
        end_time = datetime.now()  # Record end time
        elapsed_time = (end_time - start_time).total_seconds()

        self.session.log_response_json(
            response,
            self.prompt_count,
            elapsed_time,
        )

        response_parts = self._process_response(response, functions, total_prompt)

        self.session.log_response_md(
            response,
            response_parts,
            self.prompt_count,
            self.token_counts,
            description=description,
            elapsed_time=elapsed_time,  # Pass elapsed time
        )

        return response_parts, elapsed_time

    def _parse_code_text(self, text):
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
                self.prompt_count,
                self.extracted_file_counts,
                self.task,
                self.verifier,
            )
            file_path = Path(file_path_str)
            # Get just the filename from the Path object.
            filename = file_path.name
            # Return filename (without extension)
            base_filename = file_path.stem

            extracted_code.append((file_type, content, base_filename))
        return extracted_code

    def refine_code(self, train_results, test_results, code, base_filename):
        """
        Refines the generated code based on test results, using the dreamer/coder pattern.
        """
        history = [""]

        # Construct the dreamer prompt
        dreamer_prompt = ["\nPrevious Code:\n", f"```python\n{code}\n```\n"]
        dreamer_prompt.append("\nTrain Set Results:\n")

        for i, result in enumerate(train_results):
            dreamer_prompt.append(f"\n**Example {i+1}:**\n")
            dreamer_prompt.append(f"Input:\n```\n{result['input']}\n```\n")
            dreamer_prompt.append(f"Expected Output:\n```\n{result['expected_output']}\n```\n")
            if 'transformed_output' in result:
                dreamer_prompt.append(f"Transformed Output:\n```\n{result['transformed_output']}\n```\n")
                # Add images
                image_filename = f"{base_filename}-train-example_{i+1}.png"
                dreamer_prompt.append(f"![Transformed Image]({image_filename})\n")

            dreamer_prompt.append(f"Status: {result['status']}\n")

        if test_results:  # Only include if there are test results
           dreamer_prompt.append("\nTest Set Results (if applicable):\n")
           for i, result in enumerate(test_results):
                dreamer_prompt.append(f"\n**Test Example {i+1}:**\n")
                dreamer_prompt.append(f"Input:\n```\n{result['input']}\n```\n")
                dreamer_prompt.append(f"Expected Output:\n```\n{result['expected_output']}\n```\n")
                if 'transformed_output' in result:
                    dreamer_prompt.append(f"Transformed Output:\n```\n{result['transformed_output']}\n```\n")
                    # Add images
                    image_filename = f"{base_filename}-test-example_{i+1}.png"
                    dreamer_prompt.append(f"![Transformed Image]({image_filename})\n")
                dreamer_prompt.append(f"Status: {result['status']}\n")

        instructions = [self.nlp_instructions]  # Use existing nlp_instructions
        response_parts, elapsed_time = self._generate(
            "dreamer",
            history,
            dreamer_prompt,
            instructions,
            description=f"refine_code - NLP",
        )
        history.extend(dreamer_prompt)
        history.extend(response_parts)

        # Construct the coder prompt
        coder_prompt = [""]  # Start with an empty prompt for coder
        instructions = [self.code_instructions] # Use existing code instructions.  May need adjustment later.
        response_parts, elapsed_time = self._generate(
            "coder",
            history,
            coder_prompt,
            instructions,
            description=f"refine_code - CODE",
        )
        history.extend(coder_prompt)
        history.extend(response_parts)

    def _process_response(self, response, functions, total_prompt):
        """Processes the response from the Gemini model."""
        response_parts = []
        #  function_call_found = False
        #  last_result = None

        if not response.candidates:  # Check if candidates is not empty
            # Handle the case where response.candidates is empty
            error_msg = "No candidates returned in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")  # Add an error indicator to response
            response_parts.append(error_msg + "\n")

            return response_parts  # , function_call_found, last_result

        if not hasattr(response.candidates[0].content, "parts"):
            # Handle the case where response.candidates is empty
            error_msg = "No content parts in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")  # Add an error indicator to response
            response_parts.append(error_msg + "\n")

            return response_parts  # , function_call_found, last_result

        for part in response.candidates[0].content.parts:
            if part.text:
                #  response_parts.append("\n*text:*\n")
                response_parts.append(part.text + "\n")
                # Extract code blocks and write to files
                extracted_code = self._parse_code_text(part.text)
                for file_type, code, base_filename in extracted_code:
                    if file_type == "py":
                        # Pass base_filename to test_code
                        train_results = self.verifier.test_code(
                            "example",
                            code,
                            self.session.task_dir,
                            self.task.train,
                            base_filename,
                        )
                        self.verifier.write_test_results(
                            train_results,
                            self.session.task_dir,
                            self.task,
                            base_filename + "-train",
                        )

                        # Check results
                        all_train_passed = all(
                            result.get("status") is True for result in train_results
                        )
                        if all_train_passed:
                            test_results = self.verifier.test_code(
                                "example",
                                code,
                                self.session.task_dir,
                                self.task.test,
                                base_filename,
                            )
                            self.verifier.write_test_results(
                                test_results,
                                self.session.task_dir,
                                self.task,
                                base_filename + "-test",
                            )

                        else:
                            #  # Construct a new prompt for dreamer and coder
                            #  new_prompt = ["\nPrevious Test Results:\n"] + test_results + ["\nPlease fix the errors.\n"]
                            #  # Call _generate recursively.  Need to track history.
                            #  response_parts, _ = self._generate("dreamer", [], new_prompt, [self.nlp_instructions], description="test_failure_dreamer")
                            #  response_parts, _ = self._generate("coder", [], ["\nPrevious Test Results:\n"] + test_results, [self.code_instructions], description="test_failure_coder")
                            #  pass  # we will handle this in a future turn
                            # Call refine_code if training failed
                            self.refine_code(train_results, None, code, base_filename) # Note: No test_results if train failed

            if part.executable_code:
                response_parts.append("\n*code_execution:*\n")
                code = part.executable_code.code
                response_parts.append(f"```python\n{code}\n```\n")

                # Call _test_code and extend response_parts
                test_results = self.verifier.test_code(
                    code, self.session.task_dir, self.task
                )
                response_parts.extend(test_results)

            if part.code_execution_result:
                response_parts.append("\n*code_execution_result:*\n")
                outcome = part.code_execution_result.outcome
                output = part.code_execution_result.output
                response_parts.append(f"outcome: {outcome}\n")
                response_parts.append(f"```\n{output}\n```\n")
                self.session._write_to_file(
                    f"{self.prompt_count:03d}-code_result.txt", output
                )  # Use session method

            if part.function_call:
                function_call_found = True
                response_parts.append("\n*function_call:*\n")
                response_parts.append(part.function_call.name + "\n")

                result, msg = self._call_function(
                    part.function_call, functions, total_prompt
                )
                #  last_result = msg

                response_parts.append("\nresult:\n")
                response_parts.append(f"{result}\n")
                response_parts.append(f"{msg}\n")

        return response_parts  # , function_call_found, last_result

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
        self.session.log_error(error_msg, "".join(total_prompt))

    def run(self, tasks):
        """
        Runs the Seer over the set of tasks.
        """
        self.tasks = tasks
        self.prompt_count = 0
        self.session = Session(self.config, self.tasks)

        for task in self.tasks:
            self.solve(task)

        summarize_session(
            self.session.session_dir,
            self.session.log_error,
            self.session.display_response,
        )
