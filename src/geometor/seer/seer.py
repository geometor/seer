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

from geometor.arcprize.solvers.gemini_client import GeminiClient as Client
from geometor.seer.logger import Logger
#  import geometor.seer.gemini_solver_instructions as INST

#  DEFAULT_MODEL = "models/gemini-1.5-flash"
#  DEFAULT_MODEL = "models/gemini-1.5-flash-002"
#  DEFAULT_MODEL = "models/gemini-1.5-pro-002"
#  DEFAULT_INSTRUCTIONS_FILE = "gemini_instructions.md"


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks to input/output pairs of training examples - and test inputs


    """

    def __init__(
        self,
        nlp_model: str,
        code_model: str,
        system_context: str,
        task_context: str,
        output_dir: str = ".",
        max_iterations: int = 5,
        timestamp: str = None,
    ):
        self.start_time = datetime.now()
        self.response_times = []  # Track individual response times

        self.nlp_model = nlp_model
        self.code_model = code_model

        self.system_context = system_context
        self.task_context = task_context

        self.max_iterations = max_iterations
        self.call_count = 0
        self.current_iteration = 0

        # Initialize GeminiClient
        self.nlp_client = Client(nlp_model, instructions_file)
        self.code_client = Client(code_model, instructions_file)

        # Initialize timestamp
        self.timestamp = timestamp or datetime.now().strftime("%y.%j.%H%M%S")

        # Initialize Logger
        self.logger = Logger(
            output_dir,
            self
        )

        self.history = []

        # Initialize metadata for logging
        #  self.metadata = {
            #  "task_id": task.id,
            #  "model": model_name,
            #  "timestamp": self.timestamp,
            #  "max_iterations": max_iterations,
            #  "history": [],
            #  "grid_states": [],
            #  "function_calls": [],
            #  "start_time": self.start_time.isoformat(),
            #  "response_times": [],
            #  "total_elapsed": None,
        #  }

        # Initialize token tracking
        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}

        
    def solve_task(self, task: Puzzle,):
        """
        Main method to orchestrate the task solving workflow.
        Returns the working grid if solution is found, None otherwise.
        """
        try:
            # Initialize solving state
            self.history = [f"Begin task: {self.task.id}\n\n"]

            #  instructions = [INST.example_instructions]
            self._investigate_examples()
            #  self._review_programs()
            #  self._show_test_input()
            #  self._initialize_working_grid()
            #  self._run_solution_loop()

        except Exception as e:
            print(f"Solve failed: {str(e)}")
            self.logger.log_error(f"Solve failed: {str(e)}", self.history)
            raise

    def _investigate_examples(self, instructions, include_images=True):
        """
        investigate all training pairs
        """
        for i, pair in enumerate(self.task.train, 1):
            prompt = [
                f"""
```python
example_{i}_input = {str(pair.input.grid)}

example_{i}_output = {str(pair.output.grid)}
```
"""]
            if include_images:
                self.logger.save_grid_image(
                    pair.input.to_image(), self.call_count, f"example_{i}_input"
                )
                self.logger.save_grid_image(
                    pair.output.to_image(), self.call_count, f"example_{i}_output"
                )
                prompt.extend(
                    [
                        "\nimages\n\ninput\n",
                        pair.input.to_image(),
                        "\noutput\n",
                        pair.output.to_image(),
                        "\n",
                    ]
                )

            # nlp prompt
            self._generate_content(
                prompt,
                instructions,
                #  tools="code_execution",
                description=f"example_{i}",
            )

    def _review_programs(self, instructions):
        """
        summarize observations on pairs
        """

        prompt = [INST.examples_summary_prompt]
        instructions = [INST.examples_summary_instructions]
        self._generate_content(
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
        self.logger.save_grid_image(
            test_pair.input.to_image(), self.call_count, f"test_input"
        )
        prompt = [
            f"""\
**test**

**input**

```
{ str(test_pair.input.grid) }
```

**image**

""",
            test_pair.input.to_image(),
            "\n",
            "\n**observations**\n",
        ]
        instructions = [INST.test_input_instructions]
        self._generate_content(
            prompt,
            instructions,
            #  tools="code_execution",
            description=f"test input",
        )


    def _generate_content(
        self, prompt, instructions, tools=None, functions=None, description=""
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        MAX_RETRIES = 3
        self.call_count += 1

        print(f"{self.call_count} • PROMPT")
        print("=" * 80)

        for part in prompt:
            print(part)

        instructions.insert(0, "\nINSTRUCTIONS:\n\n")
        for part in instructions:
            print(part)

        # write the prompt file
        self.logger.write_rst_log(
            prompt + instructions, "prompt", self.call_count, description=description
        )

        # write history file
        total_prompt = self.history + prompt + ["\n\n====\n\n"] + instructions
        self.history = self.history + prompt
        self.logger.write_rst_log(
            total_prompt, "history", self.call_count, description=description
        )

        for attempt in range(MAX_RETRIES):
            try:
                response_start = datetime.now()
                response = self.client.generate_content(
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

                self.logger.save_response(response_data, self.call_count)

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
                            #  if function_call_found:
                            #  # More than one function call found - this should trigger a retry
                            #  raise MultipleFunctionCallsError(
                            #  "Multiple function calls detected"
                            #  )

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
                if functions and not function_call_found and attempt < MAX_RETRIES - 1:
                    retry_prompt = total_prompt + [
                        "\nNo function call found in your response. Please provide exactly one function call using the available functions.\n"
                    ]
                    total_prompt = retry_prompt
                    print(
                        f"\nRetrying function call request (attempt {attempt + 2}/{MAX_RETRIES})"
                    )
                    continue

                # Log the response
                print(f"{self.call_count} • RESPONSE")
                print("-" * 80)
                for part in response_parts:
                    print(part)
                self.history = self.history + response_parts

                self.logger.write_rst_log(
                    response_parts,
                    "response",
                    self.call_count,
                    {
                        "current": metadata,
                        "totals": self.token_counts,
                        "timing": {
                            "response_time": response_time,
                            "total_elapsed": total_elapsed,
                        },
                        "model": self.model_name,
                    },
                    description=description,
                )

                return last_result

            except MultipleFunctionCallsError as e:
                if attempt < MAX_RETRIES - 1:
                    retry_prompt = total_prompt + [
                        "\nPlease provide exactly one function call in your response.\n"
                    ]
                    total_prompt = retry_prompt
                    print(
                        f"\nRetrying due to multiple function calls (attempt {attempt + 2}/{MAX_RETRIES})"
                    )
                    continue
                else:
                    print(f"\nERROR: {str(e)} - Max retries exceeded")
                    self.logger.log_error(str(e), prompt)
                    raise

            except Exception as e:
                print(f"\nERROR generating content: {str(e)}")
                self.logger.log_error(str(e), prompt)
                raise

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.logger.log_error(error_msg, prompt)
        raise MaxRetriesExceededError(error_msg)

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

    # TEST FUNCTIONS to call from model #################################
    def initialize_output_from_input(self) -> str:
        """
        Initialize the test output grid with a copy of the input grid.
        """
        from copy import deepcopy

        self.working_grid = deepcopy(self.task.test[0].input)
        print(str(self.working_grid.grid))

        return True, "initialize_output_from_input()"

    def initialize_output_by_size(self, width: int, height: int, color: int = 0) -> str:
        """
        Initialize the test output grid with specific dimensions.
        """
        width, height, color = int(width), int(height), int(color)
        new_grid = np.full((height, width), color)
        self.working_grid = Grid(new_grid, self.task.id, "test", 0, "output")
        print(str(self.working_grid.grid))

        return True, f"initialize_output_by_size({width=}, {height=}, {color=})"

    def set_pixel(self, row: int, column: int, color: int) -> str:
        """
        Set grid value at a specific coordinate.
        """
        return self.working_grid.set_pixel(row, column, color)

    def set_range(
        self, row1: int, column1: int, row2: int, column2: int, color: int
    ) -> str:
        """
        Set grid values for a range of pixels.
        """
        return self.working_grid.set_range(row1, column1, row2, column2, color)

    def submit(self) -> str:
        """
        Submit the working grid and check for correctness against the expected output.
        """
        if self.working_grid is None:
            raise ValueError("No working grid to submit")

        expected_output = self.task.test[0].output

        # Perform the comparison and score each part
        score = self._evaluate_accuracy(self.working_grid, expected_output)

        # Create a log entry for the result
        final_log = [ f"""
**Final Submission Results**

:Size Correct: {score['size_correct']}
:Colors Correct: {score['colors_correct']}
:Unique Color Count Diff: {score['unique_color_difference']}
:Pixel Accuracy: {score['pixel_accuracy']}%

"""
        ]

        description = "final"
        self.logger.write_rst_log(
            final_log, "submission", self.call_count, description=description
        )

        return True, "submit"

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
