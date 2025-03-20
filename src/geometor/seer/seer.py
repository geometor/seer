"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

from geometor.seer.session import Session, SessionTask

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client
import geometor.seer.verifier as verifier

#  from geometor.seer.response_handler import ResponseHandler


from geometor.seer.trial_result import CodeTrial



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

        if task_results.get("any_train_passed"):
            return

        # STEP: coder prompt *********************************
        title = f"all training • investigate_coder"
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

        task_step.summarize()

        # TODO: task results should be an object
        if task_results.get("any_train_passed"):
            # this means a test was run as well
            return

        current_iteration = 0
        while current_iteration < self.max_iterations:

            code_filename = next(iter(task_results["code_trials"]))
            code_trial = task_results["code_trials"][code_filename]
            code = code_trial.code

            task_results = self.refine(
                session_task,
                task,
                code,
                code_trial,
                current_iteration,
            )

            if task_results.get("any_train_passed"):
                return

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
        code,
        code_trial, 
        current_iteration,
    ):
        """
        Refines the generated code based on test results, using the dreamer/coder pattern.
        """

        # TODO: compare results from previous tests
        #  previous_step = session_task.steps[-1]

        history = []

        # --- Dreamer ---
        dreamer_prompt = []
        instructions = [self.instructions["refine_dreamer"]]

        # Gather reports from ALL code files in the previous step
        #  all_reports = ""
        #  for file_name, code in previous_step.codes.get("py", {}).items():
            #  trial_result = TrialResult(
                #  file_name,
                #  previous_step.trials.get(file_name, {}).get("train"),
                #  previous_step.trials.get(file_name, {}).get("test"),
            #  )
            #  all_reports += trial_result.generate_report(task)

        dreamer_prompt.append("\nPrevious Code:\n")
        dreamer_prompt.append(f"```python\n{code}\n```\n")
        dreamer_prompt.append(code_trial.generate_report())

        task_step = self._generate(
            session_task,
            "dreamer",
            f"refine_dreamer • iteration {current_iteration}",
            history,
            dreamer_prompt,
            instructions,
            tools="code_execution" # Consider if tools are needed
        )
        task_results = task_step.run_trials(task)

        task_step.summarize()

        if task_results["any_train_passed"]:
            return

        history.extend(dreamer_prompt)
        history.extend(task_step.response_parts)


        # --- Coder ---
        coder_prompt = [""]  # Coder prompt might be minimal
        instructions = [self.instructions["refine_coder"]]

        task_step = self._generate(
            session_task,
            "coder",
            f"refine_coder • iteration {current_iteration}",
            history,
            coder_prompt,
            instructions,
            #  tools="code_execution"
        )

        history.extend(coder_prompt)
        history.extend(task_step.response_parts)

        # Run trials and check for success
        task_results = task_step.run_trials(task)
        task_step.summarize()

        return task_results
