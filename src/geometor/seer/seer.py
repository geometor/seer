"""Dialogue-Based ARC task Solver

Implements a structured workflow for solving ARC tasks through conversation
with LLMs, focusing on building understanding before attempting solutions.

The solver follows a systematic process:

1. Examine training examples individually
2. Build comprehensive observations
3. Validate understanding through pre-testing
4. Implement solution through standard operations

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

#  from geometor.seer.session import Session


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks to input/output pairs of training examples - and test inputs
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

        # Initialize call count
        self.call_count = 0

    def solve_task(
        self,
        task: Puzzle,
    ):
        """
        Main method to orchestrate the task solving workflow.
        Returns the working grid if solution is found, None otherwise.
        """
        self.call_count = 0  # Reset call count for each task
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

    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        instructions = [""]
        history = [""]

        for i, pair in enumerate(examples, 1):
            prompt = [
                f"""
```python
example_{i}_input = {str(pair.input.grid)}

example_{i}_output = {str(pair.output.grid)}
```
"""
            ]
            if include_images:
                self.session.save_grid_image(
                    pair.input.to_image(), self.call_count, f"example_{i}_input"
                )
                self.session.save_grid_image(
                    pair.output.to_image(), self.call_count, f"example_{i}_output"
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

        prompt = [INST.examples_summary_prompt]
        instructions = [INST.examples_summary_instructions]
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
            test_pair.input.to_image(), self.call_count, f"test_input"
        )
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

    def _generate(
        self, history, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.call_count += 1

        print(f"{self.call_count} • PROMPT")
        print("=" * 80)

        for part in prompt:
            print(part)

        #  instructions.insert(0, "\nINSTRUCTIONS:\n\n")
        for part in instructions:
            print(part)

        # write the prompt file
        self.session.log_task_prompt(
            prompt, history, self.call_count, description=description
        )

        # write history file
        total_prompt = []
        total_prompt = history + prompt + ["\n\n====\n\n"] + instructions
        history = history + prompt
        #  self.session.log_task_history(
        #      total_prompt, "history", self.call_count, description=description
        #  )

        for attempt in range(self.max_iterations):
            try:
                response_start = datetime.now()
                response = self.nlp_client.generate_content(
                    total_prompt,
                    tools=tools,
                )
                response_end = datetime.now()
                response_time = (response_end - response_start).total_seconds()

                # Update timing metadata
                self.response_times.append(response_time)
                total_elapsed = (response_end - self.start_time).total_seconds()

                # Update token counts immediately
                metadata = response.to_dict().get("usage_metadata", {})
                self.token_counts["prompt"] += metadata.get("prompt_token_count", 0)
                self.token_counts["candidates"] += metadata.get(
                    "candidates_token_count", 0
                )
                self.token_counts["total"] += metadata.get("total_token_count", 0)
                self.token_counts["cached"] += metadata.get(
                    "cached_content_token_count", 0
                )

                # Save response with current totals
                response_data = response.to_dict()
                response_data["token_totals"] = self.token_counts.copy()
                response_data["timing"] = {
                    "response_time": response_time,
                    "total_elapsed": total_elapsed,
                    "response_times": self.response_times.copy(),
                }

                self.session.log_response(response_data, self.call_count)
                #  print(response_data)

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
                print(f"{self.call_count} • RESPONSE")
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
