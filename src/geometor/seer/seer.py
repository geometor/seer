"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""

from datetime import datetime

from geometor.seer.tasks.tasks import Tasks, Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.prompts import get_pair_prompt

from geometor.seer.gemini_client import GeminiClient as Client

from geometor.seer.session.session import Session
from geometor.seer.session.session_task import SessionTask

import geometor.seer.verifier as verifier
from geometor.seer.response_handler import ResponseHandler  # Import the new class


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
        self.current_iteration = 0
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

        task_step = session_task.add_step(title, history, prompt, instructions)
        total_prompt = history + prompt + instructions

        # TODO: set conditional `code_execution`
        (
            response,
            response_parts,
            extracted_code_list,
        ) = self._generate(
            "dreamer",
            history, prompt, instructions,
            tools="code_execution",
            description=title,
        )
        history.extend(prompt)
        history.extend(response_parts)

        self._test_extracted_codelist(extracted_code_list, task)
        if self.task_solved:  # Check if solved
            return  # Exit the loop if solved

        task_step.add_response(response, response_parts, extracted_code_list)

        # STEP: coder prompt *********************************
        title = f"all training • investigate_coder",
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

        self.session.log_response_json(
            response,
            self.prompt_count,
            elapsed_time,
        )

        # --- USE THE RESPONSE HANDLER ---
        handler = ResponseHandler(self.session)
        response_parts, extracted_code_list = handler.process_response(
            response,
            functions,
            total_prompt,
            self.prompt_count,
            self.extracted_file_counts,
        )
        # --- END OF RESPONSE HANDLER USAGE ---

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
