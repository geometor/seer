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
import contextlib
import traceback

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.gemini_client import GeminiClient as Client
from geometor.seer.exceptions import (
    MultipleFunctionCallsError,
    MaxRetriesExceededError,
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)
from geometor.seer.session import Session
import geometor.seer.verifier as verifier
from geometor.seer.session.summary import summarize_session, summarize_task


class Seer:
    def __init__(
        self,
        config: dict,
    ):
        self.config = config

        self.roles = {}
        for role_name, role_config in config["roles"].items():
            self.roles[role_name] = Client(self.config, role_name)

        self.instructions = {}
        for key, instruction_file in config["instructions"].items():
            with open(instruction_file, "r") as f:
                self.instructions[key] = f.read().strip()

        self.max_iterations = config["max_iterations"]
        self.current_iteration = 0
        self.use_images = config.get("use_images", False)

        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}
        self.task_solved = False  # Initialize task_solved flag

    def run(self, tasks):
        """
        Runs the Seer over the set of tasks.
        """
        self.tasks = tasks
        self.session = Session(self.config, self.tasks)

        for task in self.tasks:
            self.solve(self.session, task)

        summarize_session(self.session)

    def solve(
        self,
        session,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        session.set_task_dir(task.id)

        self.prompt_count = 0
        self.task = task

        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

        try:
            task_image = task.to_image()

            image_path = self.session.task_dir / "task.png"
            task_image.save(image_path)

            task_json_str = task.nice_json_layout()
            task_json_file = session.task_dir / "task.json"
            task_json_file.write_text(task_json_str)

            self._investigate(task)
        except Exception as e:
            self.session.log_error(e)

        summarize_task(session.task_dir, session.log_error)

    def _investigate(self, task, include_images=True):
        """
        investigate all training pairs
        """
        self.task_solved = False  # Reset at the start of each task

        for i, pair in enumerate(task.train, 1):
            # reset history for each pair
            history = [""]
            self.current_iteration = 0

            input_grid_str = pair.input.to_string()
            output_grid_str = pair.output.to_string()

            # dreamer prompt
            prompt = [
                f"\n## Example {i}\n",
                "\n**input:**\n```\n",
                input_grid_str,
                "\n```\n\n",
            ]
            if include_images:
                input_image_filename = self.session.log_prompt_image(
                    pair.input, self.prompt_count + 1, f"example_{i}_input"
                )
                #  prompt.append(f"![Image]({input_image_filename})\n")
                prompt.append(pair.input.to_image())
                prompt.append("\n")
            prompt.append("\n**output:**\n```\n")
            prompt.append(output_grid_str)
            prompt.append("\n```\n\n")
            if include_images:
                output_image_filename = self.session.log_prompt_image(
                    pair.output, self.prompt_count + 1, f"example_{i}_output"
                )
                #  prompt.append(f"![Image]({output_image_filename})\n")
                prompt.append(pair.output.to_image())
                prompt.append("\n")

            instructions = [self.instructions["investigate_dreamer"]]
            (
                response,
                response_parts,
                extracted_code_list,
            ) = self._generate(
                "dreamer",
                history,
                prompt,
                instructions,
                tools="code_execution",
                description=f"example_{i} • investigate_dreamer",
            )
            history.extend(prompt)
            history.extend(response_parts)

            self._test_extracted_codelist(extracted_code_list, task)
            if self.task_solved:  # Check if solved
                break  # Exit the loop if solved

            # coder prompt
            instructions = [self.instructions["investigate_coder"]]
            prompt = [""]
            (
                response,
                response_parts,
                extracted_code_list,
            ) = self._generate(
                "coder",
                history,
                prompt,
                instructions,
                #  tools="code_execution",
                description=f"example_{i} • investigate_coder",
            )
            history.extend(prompt)
            history.extend(response_parts)

            self._test_extracted_codelist(extracted_code_list, task)
            if self.task_solved:  # Check if solved
                break  # Exit loop

    def _test_extracted_codelist(self, extracted_code_list, task):
        # TODO: this function cannot call refine if we are already in a refine loop
        train_results = []
        test_results = []

        # Iterate and test *all* code blocks
        for code_type, code, base_filename in extracted_code_list:
            if code_type == "py":
                current_train_results = verifier.test_code_with_timeout(
                    code,
                    self.session.task_dir,
                    task.train,
                )
                verifier.write_test_results(
                    current_train_results,
                    self.session.task_dir,
                    base_filename + "-train",
                )
                if "examples" in current_train_results:
                    train_image = task.to_image(
                        train_results=current_train_results, show_test=False
                    )
                    train_image_filename = f"{base_filename}-train_results.png"
                    train_image_path = self.session.task_dir / train_image_filename
                    train_image.save(train_image_path)

                    all_train_passed = all(
                        result.get("match") is True
                        for result in current_train_results["examples"]
                    )
                    if all_train_passed:
                        current_test_results = verifier.test_code_with_timeout(
                            code,
                            self.session.task_dir,
                            task.test,
                        )
                        verifier.write_test_results(
                            current_test_results,
                            self.session.task_dir,
                            base_filename + "-test",
                        )

                        if "examples" in current_test_results:
                            test_image = task.to_image(
                                train_results=current_train_results,
                                test_results=current_test_results,
                            )
                            test_image_filename = f"{base_filename}-test_results.png"
                            test_image_path = (
                                self.session.task_dir / test_image_filename
                            )
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
        Generate content from the model, handling logging.
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

        client = self.roles[role_name]
        start_time = datetime.now()
        response = client.generate_content(
            total_prompt,
            tools=tools,
        )
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()

        self.session.log_response_json(
            response,
            self.prompt_count,
            elapsed_time,
        )

        (
            response_parts,
            extracted_code_list,
        ) = self._process_response(response, functions, total_prompt)

        self.session.log_response_md(
            response,
            response_parts,
            self.prompt_count,
            description=description,
            elapsed_time=elapsed_time,
        )

        return (
            response,
            response_parts,
            extracted_code_list,
        )

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
            )
            file_path = Path(file_path_str)
            # Get just the filename from the Path object.
            filename = file_path.name
            # Return filename (without extension)
            base_filename = file_path.stem

            extracted_code.append((file_type, content, base_filename))
        return extracted_code

    def refine(self, task, train_results, test_results, code, base_filename):
        """
        Refines the generated code based on test results, using the dreamer/coder pattern.
        """
        history = [""]

        self.current_iteration += 1

        # Construct the dreamer prompt
        dreamer_prompt = ["\nPrevious Code:\n", f"```python\n{code}\n```\n"]

        dreamer_prompt.append("\nTrain Set Results:\n")
        if train_results and 'examples' in train_results:
            for i, result in enumerate(train_results["examples"]):
                dreamer_prompt.append(f"\n## Example {i+1}:\n")
                dreamer_prompt.append(f"\nInput:\n```\n{result.get('input')}\n```\n")
                dreamer_prompt.append(
                    f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"
                )
                if "transformed_output" in result:
                    dreamer_prompt.append(
                        f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    )
                    # Add images
                    image_filename = f"{base_filename}-train-example_{i+1}.png"
                    dreamer_prompt.append(f"![Transformed Image]({image_filename})\n")

                dreamer_prompt.append(f"match: {result.get('match')}\n")
                dreamer_prompt.append(f"pixels_off: {result.get('pixels_off')}\n")
                dreamer_prompt.append(f"size_correct: {result.get('size_correct')}\n")
                dreamer_prompt.append(
                    f"color_palette_correct: {result.get('color_palette_correct')}\n"
                )
                dreamer_prompt.append(
                    f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"
                )

        if test_results and "examples" in test_results:  
            dreamer_prompt.append("\nTest Set Results (if applicable):\n")
            for i, result in enumerate(test_results["examples"]):
                dreamer_prompt.append(f"\n**Test {i+1}:**\n")
                dreamer_prompt.append(f"Input:\n```\n{result.get('input')}\n```\n")
                dreamer_prompt.append(
                    f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"
                )
                if "transformed_output" in result:
                    dreamer_prompt.append(
                        f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    )
                    # Add images
                    image_filename = f"{base_filename}-test-example_{i+1}.png"
                    dreamer_prompt.append(
                        f"!.get(Transformed Image)({image_filename})\n"
                    )
                dreamer_prompt.append(f"match: {result.get('match')}\n")
                dreamer_prompt.append(f"pixels_off: {result.get('pixels_off')}\n")
                dreamer_prompt.append(f"size_correct: {result.get('size_correct')}\n")
                dreamer_prompt.append(
                    f"color_palette_correct: {result.get('color_palette_correct')}\n"
                )
                dreamer_prompt.append(
                    f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"
                )

        instructions = [self.instructions["refine_dreamer"]]
        (
            response,
            response_parts,
            extracted_code_list,
        ) = self._generate(
            "dreamer",
            history,
            dreamer_prompt,
            instructions,
            description=f"refine_dreamer",
        )
        history.extend(dreamer_prompt)
        history.extend(response_parts)

        # there should not generally be code from dreamer but just in case
        self._test_extracted_codelist(extracted_code_list, task)

        # Construct the coder prompt
        coder_prompt = [""]
        instructions = [self.instructions["refine_coder"]]

        (
            response,
            response_parts,
            extracted_code_list,
        ) = self._generate(
            "coder",
            history,
            coder_prompt,
            instructions,
            description=f"refine_coder",
        )
        history.extend(coder_prompt)
        history.extend(response_parts)

        self._test_extracted_codelist(extracted_code_list, task)

    def _process_response(self, response, functions, total_prompt):
        """Processes the response from the Gemini model."""
        response_parts = []
        #  code = None           # REMOVE
        #  base_filename = None  # REMOVE
        extracted_code_list = []  # Store extracted code blocks

        if not response.candidates:  # Check if candidates is not empty
            # Handle the case where response.candidates is empty
            error_msg = "No candidates returned in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")  # Add an error indicator to response
            response_parts.append(error_msg + "\n")

            return (
                response_parts,
                extracted_code_list,  # Return extracted code
            )

        if not hasattr(response.candidates[0].content, "parts"):
            # Handle the case where response.candidates is empty
            error_msg = "No content parts in response."
            print(f"\nERROR: {error_msg}")
            self.session.log_error(error_msg, "".join(total_prompt))
            response_parts.append("\n*error:*\n")  # Add an error indicator to response
            response_parts.append(error_msg + "\n")

            return (
                response_parts,
                extracted_code_list,  # Return extracted code
            )

        for part in response.candidates[0].content.parts:
            if part.text:
                response_parts.append(part.text + "\n")
                extracted_code = self._parse_code_text(part.text)
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
                    f"{self.prompt_count:03d}-code_result.txt", output
                )

            if part.function_call:
                function_call_found = True
                response_parts.append("\n*function_call:*\n")
                response_parts.append(part.function_call.name + "\n")

                result, msg = self._call_function(
                    part.function_call, functions, total_prompt
                )

                response_parts.append("\nresult:\n")
                response_parts.append(f"{result}\n")
                response_parts.append(f"{msg}\n")

        return (
            response_parts,
            extracted_code_list,
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
        self.session.log_error(error_msg, "".join(total_prompt))
