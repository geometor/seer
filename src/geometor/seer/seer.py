"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

#  if TYPE_CHECKING:

from geometor.seer.session import Session, SessionTask

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client
import geometor.seer.verifier as verifier

#  from geometor.seer.response_handler import ResponseHandler


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
        session = Session(self.config)

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

        # TODO: set config for `code_execution`
        task_step = self._generate(
            session_task,
            "dreamer",
            title,
            history,
            prompt,
            instructions,
            tools="code_execution",
        )

        history.extend(prompt)
        history.extend(task_step.response_parts)

        # TODO: results can be for more than one file
        task_results = task_step.run_trials(task)

        task_step.summarize()

        if task_results.get("train_solved"):
            return

        # STEP: coder prompt *********************************
        title = (f"all training • investigate_coder",)
        instructions = [self.instructions["investigate_coder"]]
        prompt = [""]
        task_step = self._generate(
            session_task,
            "coder",
            title,
            history,
            prompt,
            instructions,
            #  tools="code_execution",
        )
        history.extend(prompt)
        history.extend(task_step.response_parts)

        # TODO: results can be for more than one file
        task_results = task_step.run_trials(task)

        if task_results.get("train_solved"):
            return

        task_step.summarize()

        current_iteration = 0
        while current_iteration < self.max_iterations:

            # TODO: refine must create a complete task step
            task_results = self.refine(
                task,
                task_results,
            )
            current_iteration += 1

    def _generate(
        self,
        session_task: SessionTask,
        role_name: str,
        title: str,
        history: list,
        prompt: list,
        instructions: list,
        tools=None,
        functions=None,
    ):
        """
        Generate content from the model, handling logging.
        """

        # init step
        task_step = session_task.add_step(title, history, prompt, instructions)

        client = self.roles[role_name]
        start_time = datetime.now()
        total_prompt = history + prompt + instructions
        response = client.generate_content(total_prompt, tools=tools)
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        task_step.log_response(response, response_time)
        reponse_parts = task_step.process_response(response)

        return task_step

    def refine(
        self,
        session_task: SessionTask,
        task,
        trial_results,
        code,
    ):
        """
        Refines the generated code based on test results, using the dreamer/coder pattern.
        """
        history = [""]

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
