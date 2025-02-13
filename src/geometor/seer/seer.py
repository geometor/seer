"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""
from rich import print
#  from rich.markdown import Markdown # Removed
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os

#  from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid  # Added ARC imports
from geometor.seer.tasks import Tasks, Task, Grid

from geometor.seer.gemini_client import GeminiClient as Client
from geometor.seer.exceptions import (
    MultipleFunctionCallsError,
    MaxRetriesExceededError,
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)
from geometor.seer.session import Session  # Import Session


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks with input/output pairs of training examples.
    """

    def __init__(
        self,
        config: dict,
        max_iterations: int = 5,
        tasks: object = None,  # Add tasks
    ):
        self.start_time = datetime.now()
        self.tasks = tasks
        self.response_times = []  # Track individual response times

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

        # Initialize GeminiClient
        self.nlp_client = Client(
            self.nlp_model, f"{self.system_context}\n\n{self.task_context}"
        )
        self.code_client = Client(
            self.code_model, f"{self.system_context}\n\n{self.task_context}"
        )

        # Initialize timestamp
        # self.timestamp = session.timestamp  <- Removed. Session will handle

        # Initialize Session *internally*
        self.session = Session(config, tasks)

        # Initialize token tracking
        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}

        # Initialize prompt count
        self.prompt_count = 0

    def solve(
        self,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        self.prompt_count = 0  # Reset prompt count for each task
        history = [""]

        try:
            self._investigate_examples(task.train)  # Pass in the examples
            #  self._review_programs()
            #  self._run_solution_loop()
        except Exception as e:
            print(f"Solve failed: {str(e)}")
            self.session.logger.log_error(
                self.session.task_dir, f"Solve failed: {str(e)}"
            )
            # Removed: raise

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = self._convert_grid_to_python(pair.input)
            output_grid_str = self._convert_grid_to_python(pair.output)

            #NLP_Prompt
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

    def _convert_grid_to_python(self, grid):
        """
        Converts a grid (represented as a nested list or numpy array)
        into a Python list of lists string representation, with each row
        on a new line.
        """
        if isinstance(grid, np.ndarray):
            grid_list = grid.tolist()
        elif isinstance(grid, Grid):  # Check if it's a Grid object
            grid_list = grid.grid.tolist()  # Access the .grid attribute
        else:
            grid_list = grid

        rows = [str(row) for row in grid_list]
        output = "[\n"
        for row in rows:
            output += f"    {row},\n"
        output += "]"
        return output

    # Removed _display_prompt and _display_response

    def _generate(
        self, history, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.prompt_count += 1

        # Removed: Call display_prompt on logger

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
            description=description,  # Join total_prompt into a string
        )

        history = history + prompt

        for attempt in range(self.max_iterations):
            try:
                response = self.nlp_client.generate_content(
                    total_prompt,
                    tools=tools,
                )

                # Moved: log_response and display_response are called within log_response
                self.session.logger.log_response(
                    self.session.task_dir,
                    response,
                    self.prompt_count,
                    self.token_counts,
                    self.response_times,
                    self.start_time,
                )

                response_parts = []
                function_call_found = False
                last_result = None

                if hasattr(response.candidates[0].content, "parts"):
                    for part in response.candidates[0].content.parts:
                        if part.text:
                            response_parts.append(part.text + "\n")
                        if part.executable_code:
                            response_parts.append("code_execution:\n")
                            response_parts.append(
                                f"```python\n{part.executable_code.code}\n```\n"
                            )
                        if part.code_execution_result:
                            response_parts.append(
                                f"code_execution_result: {part.code_execution_result.outcome}\n"
                            )
                            response_parts.append(
                                f"```\n{part.code_execution_result.output}\n```\n"
                            )
                        if part.function_call:
                            function_call_found = True
                            response_parts.append("function_call:\n")
                            response_parts.append(part.function_call.name + "\n")

                            result, msg = self._call_function(
                                part.function_call, functions
                            )
                            last_result = msg

                            response_parts.append("\nresult:\n")
                            response_parts.append(f"{result}\n")
                            response_parts.append(f"{msg}\n")

                            if msg == "submit":
                                break

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

                # Removed: Call display_response on logger

                history = history + response_parts

                return response_parts

            except Exception as e:
                print(f"\nERROR generating content: {str(e)}")
                self.session.logger.log_error(
                    self.session.task_dir, str(e), "".join(total_prompt)
                )  # Also join here for consistency
                # Removed: raise

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.session.logger.log_error(
            self.session.task_dir, error_msg, "".join(total_prompt)
        )
        # Removed: raise MaxRetriesExceededError(error_msg)

    def run(self):
        """
        Runs the Seer over the set of tasks.  This replaces Session.run().
        """
        for task in self.tasks:  # Access tasks through self.session
            self.session.task_dir = (
                self.session.session_dir / task.id
            )  # Set task_dir on session
            self.session.task_dir.mkdir(parents=True, exist_ok=True)
            try:
                self.solve(task)  # Call solve on Seer instance
            except Exception as e:
                print(f"Error during task processing {task.id}: {e}")
                self.session.logger.log_error(
                    self.session.task_dir, f"Error during task processing: {e}"
                )
