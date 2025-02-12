"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""
from rich import print
from rich.markdown import Markdown
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os

#  from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid  # Removed ARC-specific imports

from geometor.seer.gemini_client import GeminiClient as Client


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks with input/output pairs of training examples.
    """

    def __init__(
        self,
        session: object,
        config: dict,
        max_iterations: int = 5,
    ):
        self.start_time = datetime.now()
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
        self.timestamp = session.timestamp

        self.session = session

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

        self._investigate_examples(task.train) # Pass in the examples
        #  self._review_programs()
        #  self._run_solution_loop()

        #  except Exception as e:
        #      print(f"Solve failed: {str(e)}")
        #      self.session.log_error(f"Solve failed: {str(e)}")
        #      raise

    def _investigate_examples(self, examples, include_images=False): # Removed include_images
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            #  input_grid_str = self._convert_grid_to_python(pair.input) # Removed grid conversion
            #  output_grid_str = self._convert_grid_to_python(pair.output)

            prompt_base = [
                f"""
```
example_{i}_input = {str(pair.input)}

example_{i}_output = {str(pair.output)}
```
"""
            ]
            # Removed image handling

            # NLP Prompt
            nlp_prompt = prompt_base + ["\n**Generate NLP**\n"]
            nlp_instructions = [self.nlp_instructions]

            nlp_response = self._generate(
                history,
                nlp_prompt,
                nlp_instructions,
                tools=None,
                description=f"example_{i}_nlp",
            )
            history.extend(nlp_response)


            # Code Prompt
            code_prompt = prompt_base + [
                f"\n**Generate Code**\n\n**NLP:**\n{nlp_response}\n"
            ]
            code_instructions = [self.code_instructions]
            code_response = self._generate(  # Use nlp_client, no tools
                history,
                code_prompt,
                code_instructions,
                tools="code_execution",
                description=f"example_{i}_code",
            )
            history.extend(code_response)

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

    def _display_prompt(self, prompt, instructions):
        """Displays the prompt and instructions using rich.markdown.Markdown."""
        markdown_text = f"# PROMPT {self.prompt_count}\n\n"
        markdown_text += "## Prompt\n\n"
        for part in prompt:
            markdown_text += str(part) + "\n"

        markdown_text += "\n## Instructions\n\n"
        for part in instructions:
            markdown_text += str(part) + "\n"

        markdown = Markdown(markdown_text)
        print(markdown)

    def _display_response(self, response_parts):
        """Displays the response using rich.markdown.Markdown."""
        markdown_text = f"# RESPONSE {self.prompt_count}\n\n"
        for part in response_parts:
            markdown_text += str(part) + "\n"

        markdown = Markdown(markdown_text)
        print(markdown)

    def _generate(
        self, history, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.prompt_count += 1

        self._display_prompt(prompt, instructions)

        total_prompt = history + prompt + ["\n\n====\n\n"] + instructions

        self.session.logger.log_prompt(
            self.session.task_dir, prompt, instructions, self.prompt_count, description=description
        )
        self.session.logger.log_total_prompt(
            self.session.task_dir, "".join(total_prompt), self.prompt_count, description=description  # Join total_prompt into a string
        )


        history = history + prompt

        for attempt in range(self.max_iterations):
            try:
                response = self.nlp_client.generate_content(
                    total_prompt,
                    tools=tools,
                )

                self.session.logger.log_response(
                    self.session.task_dir, response, self.prompt_count, self.token_counts, self.response_times, self.start_time
                )  # Pass raw response

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
                if functions and not function_call_found and attempt < self.max_iterations - 1:
                    retry_prompt = total_prompt + [
                        "\nNo function call found in your response. Please provide exactly one function call using the available functions.\n"
                    ]
                    total_prompt = retry_prompt
                    print(
                        f"\nRetrying function call request (attempt {attempt + 2}/{self.max_iterations})"
                    )
                    continue

                # Log the response
                self._display_response(response_parts)

                history = history + response_parts

                return response_parts

            except Exception as e:
                print(f"\nERROR generating content: {str(e)}")
                self.session.logger.log_error(self.session.task_dir, str(e), "".join(total_prompt)) # Also join here for consistency
                raise

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.session.logger.log_error(self.session.task_dir, error_msg, "".join(total_prompt))
        raise MaxRetriesExceededError(error_msg)

# Custom exceptions for better error handling
class MultipleFunctionCallsError(Exception):
    """Raised when multiple function calls are detected in a single response."""

    pass


class MaxRetriesExceededError(Exception):
    """Raised when maximum retry attempts are exhausted."""

    pass


class UnknownFunctionError(Exception):
    """Raised when an unknown function is called."""

    pass


class FunctionArgumentError(Exception):
    """Raised when invalid arguments are provided to a function."""

    pass


class FunctionExecutionError(Exception):
    """Raised when a function fails during execution."""

    pass
