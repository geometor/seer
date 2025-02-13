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


    def solve(
        self,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        self.prompt_count = 0  
        history = [""]

        try:
            self._investigate_examples(task.train)  
            #  self._review_programs()
            #  self._run_solution_loop()
        except Exception as e:
            print(f"Solve failed: {str(e)}")
            self.session.logger.log_error(
                self.session.task_dir, f"Solve failed: {str(e)}"
            )

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = pair.input.to_python_string()
            output_grid_str = pair.output.to_python_string()

            # NLP_Prompt
            prompt = [
                f"""
```
example_{i}_input = {input_grid_str}

example_{i}_output = {output_grid_str}
```
"""
            ]
            if include_images:
                prompt.append("\ninput\n")
                prompt.append(pair.input.to_image())
                prompt.append("\noutput\n")
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
            history.extend(response)

            # Code Prompt
            instructions = [self.code_instructions]
            prompt = [""]
            response = self._generate(  # Use nlp_client, no tools
                history,
                prompt,
                instructions,
                tools="code_execution",
                description=f"example_{i} - CODE",
            )
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

        history = history + prompt

        for attempt in range(self.max_iterations):
            try:
                response = self.nlp_client.generate_content(
                    total_prompt,
                    tools=tools,
                )

                self.session.logger.log_response(
                    self.session.task_dir,
                    response,
                    self.prompt_count,
                    self.token_counts,
                    self.response_times,
                    self.start_time,
                )

                response_parts, function_call_found, last_result = self._process_response(
                    response, functions, attempt
                )

                # If functions were provided but no function call was found
                if (
                    functions
                    and not function_call_found
                    and attempt < self.max_iterations - 1
                ):
                    retry_prompt = total_prompt + [
                        "\nNo function call found in your response. Please provide exactly one function call using the available functions.\n"
                    ]
                    total_prompt = retry_prompt
                    print(
                        f"\nRetrying function call request (attempt {attempt + 2}/{self.max_iterations})"
                    )
                    continue

                history = history + response_parts

                return response_parts

            except Exception as e:
                print(f"\nERROR generating content: {str(e)}")
                self.session.logger.log_error(
                    self.session.task_dir, str(e), "".join(total_prompt)
                )

    def _process_response(self, response, functions, attempt):
        """Processes the response from the Gemini model."""
        response_parts = []
        function_call_found = False
        last_result = None

        if hasattr(response.candidates[0].content, "parts"):
            for part in response.candidates[0].content.parts:
                if part.text:
                    response_parts.append("\n*text:*\n")
                    response_parts.append(part.text + "\n")
                if part.executable_code:
                    response_parts.append("\n*code_execution:*\n")
                    response_parts.append(
                        f"```python\n{part.executable_code.code}\n```\n"
                    )
                if part.code_execution_result:
                    response_parts.append("\n*code_execution_result:*\n")
                    response_parts.append(
                        f"outcome: {part.code_execution_result.outcome}\n"
                    )
                    response_parts.append(
                        f"```\n{part.code_execution_result.output}\n```\n"
                    )
                if part.function_call:
                    function_call_found = True
                    response_parts.append("\n*function_call:*\n")
                    response_parts.append(part.function_call.name + "\n")

                    result, msg = self._call_function(
                        part.function_call, functions
                    )
                    last_result = msg

                    response_parts.append("\nresult:\n")
                    response_parts.append(f"{result}\n")
                    response_parts.append(f"{msg}\n")

        return response_parts, function_call_found, last_result


    def _call_function(self, function_call, functions):
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
            try:
                self.solve(task)
            except Exception as e:
                print(f"Error during task processing {task.id}: {e}")
                self.session.logger.log_error(
                    self.session.task_dir, f"Error during task processing: {e}"
                )
