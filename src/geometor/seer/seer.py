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

from geometor.seer.trials.code_trial import CodeTrial



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

        # STEP: dreamer *****************************
        title = f"investigate • dreamer • all training"
        history = []
        prompt = []
        for i, pair in enumerate(task.train, 1):
            prompt.extend(get_pair_prompt(f"train_{i}", pair, self.use_images))

        if self.use_images:
            #  show full task image
            prompt.append(task.to_image(show_test=False))

        instructions = [self.instructions["investigate_dreamer"]]

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

        task_step.run_trials()
        task_step.summarize()

        if task_step.any_trials_successful("train"):
            print("            train passed")
            if task_step.any_trials_successful("test"):
                print("            test passed")
            return

        # STEP: coder *********************************
        title = f"investigate • coder • all training"
        #  title = f"all training • investigate_coder"
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

        task_step.run_trials()
        task_step.summarize()

        if task_step.any_trials_successful("train"):
            print("            train passed")
            if task_step.any_trials_successful("test"):
                print("            test passed")
            return

        current_iteration = 0
        while current_iteration < self.max_iterations:
            # Get the first (and presumably only) CodeTrial
            code_trial = task_step.get_first_code_trial()
            if not code_trial:
                # Handle the case where there's no code trial (shouldn't normally happen)
                session_task.log_error(Exception("No code trial found in refine step."))
                return

            code = code_trial.code

            task_step = self.refine(
                session_task,
                task,
                code,
                code_trial,
                current_iteration,
            )

            if task_step.any_trials_successful("train"):
                print("            train passed")
                if task_step.any_trials_successful("test"):
                    print("            test passed")
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

        history = []

        # STEP: refine dreamer *****************************
        prompt = []
        instructions = [self.instructions["refine_dreamer"]]

        prompt.append("\nPrevious Code:\n")
        prompt.append(f"```python\n{code}\n```\n")
        prompt.append(code_trial.generate_report())

        task_step = self._generate(
            session_task,
            "dreamer",
            f"refine • {current_iteration} • dreamer",
            history,
            prompt,
            instructions,
            tools="code_execution"  # Consider if tools are needed
        )
        task_step.run_trials()
        task_step.summarize()

        if task_step.any_trials_successful("train"):
            print("            train passed")
            if task_step.any_trials_successful("test"):
                print("            test passed")
            return task_step

        history.extend(prompt)
        history.extend(task_step.response_parts)


        # STEP: refine coder *****************************
        prompt = [""]  # Coder prompt might be minimal
        instructions = [self.instructions["refine_coder"]]

        task_step = self._generate(
            session_task,
            "coder",
            f"refine • {current_iteration} • coder",
            history,
            prompt,
            instructions,
            #  tools="code_execution"
        )

        #  history.extend(prompt)
        #  history.extend(task_step.response_parts)

        # Run trials and check for success
        task_step.run_trials()
        task_step.summarize()

        return task_step
