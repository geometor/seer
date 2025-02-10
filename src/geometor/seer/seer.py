"""Dialogue-Based ARC task Solver

Implements a structured workflow for solving ARC tasks through conversation
with LLMs, focusing on building understanding before attempting solutions.

The solver follows a systematic process:

1.  Examine training examples individually
2.  Build comprehensive observations
3.  Validate understanding through pre-testing
4.  Implement solution through standard operations

Key Features:

- Progressive observation building
- Code-validated pattern discovery
- Natural language program development
- Iterative refinement through dialogue
- Comprehensive session logging

The solver maintains a conversation history and working grid state, allowing
for cumulative understanding and step-by-step solution development.
"""

from rich import print
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os

from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid

from geometor.seer.gemini_client import GeminiClient as Client


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks to input/output pairs of training examples - and test inputs
    """

    examples_summary_prompt = "Summarize the examples."  # Placeholder
    examples_summary_instructions = "Provide a summary of the observations."  # Placeholder

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

    def solve_task(
        self,
        task: Puzzle,
    ):
        """
        Main method to orchestrate the task solving workflow.
        Returns the working grid if solution is found, None otherwise.
        """
        self.prompt_count = 0  # Reset prompt count for each task
        history = [""]

        self._investigate_examples(task.train)
        #  self._review_programs()
        #  self._show_test_input()
        #  self._initialize_working_grid()
        #  self._run_solution_loop()

        #  except Exception as e:
        #      print(f"Solve failed: {str(e)}")
        #      self.session.log_error(f"Solve failed: {str(e)}")
        #      raise

    def _convert_grid_to_python(self, grid: Grid) -> str:
        """
        Converts a Grid object to a Python list representation string.
        """
        grid_str = "[\n"
        for row in grid.grid:
            grid_str += "    [" + ", ".join(map(str, row)) + "],\n"
        grid_str += "]"
        return grid_str

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        instructions = [""]
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = self._convert_grid_to_python(pair.input)
            output_grid_str = self._convert_grid_to_python(pair.output)

            prompt = [
                f"""
```python
example_{i}_input = {input_grid_str}

example_{i}_output = {output_grid_str}
```
"""
            ]
            if include_images:
                self.session.save_grid_image(
                    pair.input.to_image(), self.prompt_count, f"example_{i}_input"
                )
                self.session.save_grid_image(
                    pair.output.to_image(), self.prompt_count, f"example_{i}_output"
                )
                prompt.extend(
                    [
                        "\n**images**\n\ninput:\n",
                        pair.input.to_image(),
                        "\noutput:\n",
                        pair.output.to_image(),
                        "\n",
                    ]
                )

            # nlp prompt
            # TODO: instructions
            response = self._generate(
                history,
                prompt,
                instructions,
                tools="code_execution",
                description=f"example_{i}",
            )

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

    def _show_test_input(self):
        """
        step 3 - show test input for eval
        """
        test_pair = self.task.test[0]
        self.session.save_grid_image(
            test_pair.input.to_image(), self.prompt_count, f"test_input"
        )
        history = [""]
        instructions = [""]
        prompt = [
            f"""\
**test**

**input**

```
{str(test_pair.input.grid)}
```

**image**

""",
            test_pair.input.to_image(),
            "\n",
            "\n**observations**\n",
        ]

        self._generate(
            history,
            prompt,
            instructions,
            #  tools="code_execution",
            description=f"test input",
        )

    def _display_prompt(self, prompt, instructions):
        """Displays the prompt and instructions."""
        print(f"{self.prompt_count} • PROMPT")
        print("=" * 80)

        for part in prompt:
            print(part)

        for part in instructions:
            print(part)

    def _generate(
        self, history, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.prompt_count += 1

        self._display_prompt(prompt, instructions)

        self.session.log_prompt(
            prompt, instructions, self.prompt_count, description=description
        )

        total_prompt = history + prompt + ["\n\n====\n\n"] + instructions
        history = history + prompt

        for attempt in range(self.max_iterations):
            try:
                response = self.nlp_client.generate_content(
                    total_prompt,
                    tools=tools,
                )

                self.session.log_response(response, self.prompt_count)  # Pass raw response

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
                print(f"{self.prompt_count} • RESPONSE")
                print("-" * 80)
                for part in response_parts:
                    print(part)
                history = history + response_parts

                return last_result

            except Exception as e:
                print(f"\nERROR generating content: {str(e)}")
                self.session.log_error(str(e), total_prompt)
                raise

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.session.log_error(error_msg, total_prompt)
        raise MaxRetriesExceededError(error_msg)

    def _evaluate_accuracy(self, working_grid: Grid, expected_grid: Grid) -> dict:
        """
        Evaluate the accuracy of the working grid against the expected grid.

        Parameters
        ----------
        working_grid : Grid
            The grid created during the solution process.
        expected_grid : Grid
            The expected output grid from the training data.

        Returns
        -------
        dict
            A dictionary containing scores for each evaluated aspect.
        """
        # Size Correctness
        size_correct = (
            working_grid.height == expected_grid.height
            and working_grid.width == expected_grid.width
        )

        # Colors Correctness
        working_colors = working_grid.colors
        expected_colors = expected_grid.colors
        colors_correct = working_colors == expected_colors

        # Quantities of Unique Pixel Colors
        working_color_counts = working_grid.color_counts
        expected_color_counts = expected_grid.color_counts
        unique_color_difference = {
            color: abs(
                working_color_counts.get(color, 0) - expected_color_counts.get(color, 0)
            )
            for color in set(working_color_counts) | set(expected_color_counts)
        }

        # Per-Pixel Accuracy
        total_pixels = working_grid.size
        correct_pixels = np.sum(working_grid.grid == expected_grid.grid)
        pixel_accuracy = (
            (correct_pixels / total_pixels) * 100 if total_pixels > 0 else 0
        )

        # Return results as a dictionary
        return {
            "size_correct": size_correct,
            "colors_correct": colors_correct,
            "unique_color_difference": unique_color_difference,
            "pixel_accuracy": pixel_accuracy,
        }


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
