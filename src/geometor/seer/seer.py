"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

if TYPE_CHECKING:
    from geometor.seer.session.session import Session
    from geometor.seer.session.session_task import SessionTask

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client
import geometor.seer.verifier as verifier
from geometor.seer.response_handler import ResponseHandler  


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

    def run(self, tasks: Tasks):
        session = Session(self.config, self.tasks)

        for task in tasks:
            self.solve(session, task)

        session.summarize()

    def solve(self, session: Session, task: Task):
        session_task = session.add_task(task)

        try:
            self._investigate(task, session_task)
        except Exception as e:
            # TODO: make sure log error is implemented
            session_task.log_error(e)

        session_task.summarize()

    def _investigate(self, task: Task, session_task: SessionTask):
        """
        investigate all training pairs
        """

        # STEP: dream review all train *****************************
        title = f"all training • investigate_dreamer"
        history = []
        prompt = []
        for i, pair in enumerate(task.train, 1):
            prompt.extend(get_pair_prompt(f"train_{i}", pair, self.use_images))

        if self.use_images:
            #  show full task image
            prompt.append(task.to_image(show_test=False))

        instructions = [self.instructions["investigate_dreamer"]]

        # init step
        task_step = session_task.add_step(title, history, prompt, instructions)

        # TODO: set config fo `code_execution`
        (
            response,
            response_time,
        ) = self._generate(
            "dreamer",
            history, prompt, instructions,
            tools="code_execution",
            description=title,
        )

        task_step.log_response(response, response_time)
        reponse_parts = task_step.process_response(response)

        history.extend(prompt)
        history.extend(response_parts)

        # TODO: results can be for more than one file
        task_results = task_step.run_trials(task)

        if task_results.train_solved:
            return  # done solving

            # TODO: fix - decision to refine should come from the caller
            if self.current_iteration <= self.max_iterations:
                #  if not self.task_solved:
                self.refine(
                    task, train_results, test_results, code, base_filename
                )
        if self.task_solved:  # Check if solved
            return  # Exit the loop if solved

        # STEP: coder prompt *********************************
        title = f"all training • investigate_coder",
        instructions = [self.instructions["investigate_coder"]]
        prompt = [""]
        (
            response,
            response_time,
        ) = self._generate(
            "coder",
            history,
            prompt,
            instructions,
            #  tools="code_execution",
            description=title,
        )
        history.extend(prompt)
        history.extend(response_parts)

        self._test_extracted_codelist(extracted_code_list, task)
        if self.task_solved:  # Check if solved
            return  # Exit loop


    def _generate(
        self,
        role_name,
        history,
        prompt,
        instructions,
        tools=None,
        functions=None,
    ):
        """
        Generate content from the model, handling logging.
        """

        client = self.roles[role_name]
        start_time = datetime.now()
        response = client.generate_content(
            total_prompt,
            tools=tools,
        )
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()

        return (
            response,
            elapsed_time,
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
        if train_results and "examples" in train_results:
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
