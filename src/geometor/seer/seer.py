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
from geometor.seer.session.summary import summarize_session, summarize_task
import geometor.seer.verifier as verifier
from geometor.seer.response_handler import ResponseHandler  # Import the new class

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

        #  self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
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

        def get_pair_prompt(title, task_pair):
            prompt = [
                f"\n## {title}\n",
                ]
            for key, grid in task_pair.items():
                prompt += [
                    f"\n**{key}:**\n```\n",
                    grid.to_string(),
                    "\n```\n\n",
                ]
                if include_images:
                    input_image_filename = self.session.log_prompt_image(
                        grid, self.prompt_count + 1, f"{title}_{key}"
                    )
                    #  prompt.append(f"![Image]({input_image_filename})\n")
                    prompt.append(grid.to_image())
                    prompt.append("\n")

            return prompt
        
        # TODO: show all training examples first
        history = []
        show_training_prompt = []
        for i, pair in enumerate(task.train, 1):
            show_training_prompt.extend(get_pair_prompt(f"train_{i}", pair))

        show_training_prompt.append(task.to_image(show_test=False))

        instructions = [self.instructions["investigate_dreamer"]]
        (
            response,
            response_parts,
            extracted_code_list,
        ) = self._generate(
            "dreamer",
            history,
            show_training_prompt,
            instructions,
            tools="code_execution",
            description=f"all training • investigate_dreamer",
        )
        history.extend(show_training_prompt)
        history.extend(response_parts)

        self._test_extracted_codelist(extracted_code_list, task)
        if self.task_solved:  # Check if solved
            return  # Exit the loop if solved

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
            return  # Exit loop

        for i, pair in enumerate(task.train, 1):
            # reset history for each pair
            history = [""]
            self.current_iteration = 0

            dreamer_prompt = get_pair_prompt(f"train_{i}", pair)
            instructions = [self.instructions["investigate_dreamer"]]
            (
                response,
                response_parts,
                extracted_code_list,
            ) = self._generate(
                "dreamer",
                history,
                dreamer_prompt,
                instructions,
                tools="code_execution",
                description=f"example_{i} • investigate_dreamer",
            )
            history.extend(dreamer_prompt)
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

        # --- USE THE RESPONSE HANDLER ---
        handler = ResponseHandler(self.session)
        response_parts, extracted_code_list = handler.process_response(
            response, functions, total_prompt, self.prompt_count, self.extracted_file_counts
        )
        # --- END OF RESPONSE HANDLER USAGE ---

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
