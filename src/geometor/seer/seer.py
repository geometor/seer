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


# Add this class definition near the top of seer.py, after the imports
class TrialResult:
    def __init__(self, code_filename: str, train_results: dict, test_results: dict = None):
        self.code_filename = code_filename
        self.train_results = train_results
        self.test_results = test_results

    @property
    def train_passed(self) -> bool:
        return (
            self.train_results
            and all(r.get("match", False) for r in self.train_results.get("trials", []))
        )

    @property
    def test_passed(self) -> bool:
        return (
            self.test_results
            and all(r.get("match", False) for r in self.test_results.get("trials", []))
        )

    def generate_report(self, task: Task) -> str:
        report = f"Results for {self.code_filename}:\n"

        if self.train_results:
            report += "\nTrain Set Results:\n"
            for i, result in enumerate(self.train_results.get("trials", [])):
                report += f"\n## Example {i+1}:\n"
                report += f"Input:\n```\n{result.get('input')}\n```\n"
                report += f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"
                if "transformed_output" in result:
                    report += f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    # Add images - construct filename based on task and step
                    image_filename = f"{task.id}-{i+1}.png" # simplified name
                    report += f"![Transformed Image]({image_filename})\n"

                report += f"match: {result.get('match')}\n"
                report += f"pixels_off: {result.get('pixels_off')}\n"
                report += f"size_correct: {result.get('size_correct')}\n"
                report += f"color_palette_correct: {result.get('color_palette_correct')}\n"
                report += f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"

        if self.test_results:
            report += "\nTest Set Results:\n"
            # ... (Similar formatting for test results, if available) ...
            for i, result in enumerate(self.test_results.get("trials", [])):
                report += f"\n## Example {i+1}:\n"
                report += f"Input:\n```\n{result.get('input')}\n```\n"
                if "transformed_output" in result:
                    report += f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    # Add images - construct filename based on task and step
                    image_filename = f"{task.id}-{i+1}.png" # simplified name
                    report += f"![Transformed Image]({image_filename})\n"
                if result.get('expected_output'):
                    report += f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"

                report += f"match: {result.get('match')}\n"
                report += f"pixels_off: {result.get('pixels_off')}\n"
                report += f"size_correct: {result.get('size_correct')}\n"
                report += f"color_palette_correct: {result.get('color_palette_correct')}\n"
                report += f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"

        return report



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
                session_task,
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
        task: Task,
        trial_results, # This argument might not be needed anymore
        #  code,  # Remove code as an argument, get it from task_step
    ):
        """
        Refines the generated code based on test results, using the dreamer/coder pattern.
        """

        # get previous step
        previous_step = session_task.steps[-1]

        current_iteration = 0
        while current_iteration < self.max_iterations:
            current_iteration += 1

            history = previous_step.response_parts.copy()

            # --- Dreamer ---
            dreamer_prompt = []
            instructions = [self.instructions["refine_dreamer"]]

            # Gather reports from ALL code files in the previous step
            all_reports = ""
            for file_name, code in previous_step.codes.get("py", {}).items():
                trial_result = TrialResult(
                    file_name,
                    previous_step.trials.get(file_name, {}).get("train"),
                    previous_step.trials.get(file_name, {}).get("test"),
                )
                all_reports += trial_result.generate_report(task)
                dreamer_prompt.extend(["\nPrevious Code:\n", f"```python\n{code}\n```\n"])

            dreamer_prompt.append(all_reports)

            task_step_dreamer = self._generate(
                session_task,
                "dreamer",
                f"refine_dreamer • iteration {current_iteration}",
                history,
                dreamer_prompt,
                instructions,
                # tools="code_execution" # Consider if tools are needed
            )
            history.extend(dreamer_prompt)
            history.extend(task_step_dreamer.response_parts)

            # --- Coder ---
            coder_prompt = [""]  # Coder prompt might be minimal
            instructions = [self.instructions["refine_coder"]]

            task_step_coder = self._generate(
                session_task,
                "coder",
                f"refine_coder • iteration {current_iteration}",
                history,
                coder_prompt,
                instructions,
                tools="code_execution"
            )

            history.extend(coder_prompt)
            history.extend(task_step_coder.response_parts)

            # Run trials and check for success
            task_results = task_step_coder.run_trials(task)
            task_step_coder.summarize()

            # Check if all train and test cases passed for ANY code file
            success = False
            for code_file_results in task_results["code"].values():
                if code_file_results.get("train_passed") and code_file_results.get("test_passed"):
                    success = True
                    break  # Exit loop if any code file succeeds

            if success:
                return  # Exit refinement loop if successful

            previous_step = task_step_coder # prepare for next loop
