"""Represents the result of executing generated code against a single task input/output pair."""
from __future__ import annotations
from typing import TYPE_CHECKING, Any

import numpy as np
from geometor.seer.tasks.grid import Grid

if TYPE_CHECKING:
    from geometor.seer.tasks.tasks import TaskPair


class TaskPairTrial:
    def __init__(
        self,
        task_pair: TaskPair,
        transformed_output: Any = None,  # More permissive type
        error: str | None = None,
        function_output: str | None = None,
    ):
        self.task_pair = task_pair
        # Always create a Grid object
        self.transformed_output = (
            Grid(transformed_output) if transformed_output is not None else None
        )
        self.error = error
        self.function_output = function_output

    @property
    def input_string(self) -> str:
        return self.task_pair.input.to_string()

    @property
    def expected_output_string(self) -> str | None:
        # Return None if there is no expected output
        if self.task_pair.output is None:
            return None
        return self.task_pair.output.to_string()

    @property
    def transformed_output_string(self) -> str | None:
        if self.transformed_output is None:
            return None
        return self.transformed_output.to_string()  # Use Grid's to_string

    @property
    def match(self) -> bool:
        # Cannot match if there is no expected output, no transformed output, or an error occurred
        if self.task_pair.output is None or self.transformed_output is None or self.error is not None:
            return False
        # Check shape first for efficiency and to avoid errors with array_equal on different shapes
        if self.transformed_output.grid.shape != self.task_pair.output.grid.shape:
            return False
        return np.array_equal(self.transformed_output.grid, self.task_pair.output.grid) # Compare NumPy arrays

    @property
    def size_correct(self) -> bool | None:
        # Cannot compare size if expected or transformed output is missing
        if self.task_pair.output is None or self.transformed_output is None:
            return None
        return self.transformed_output.grid.shape == self.task_pair.output.grid.shape # Use Grid's shape

    @property
    def color_palette_correct(self) -> bool | None:
        # Cannot compare palettes if expected or transformed output is missing
        if self.task_pair.output is None or self.transformed_output is None:
            return None
        transformed_colors = set(np.unique(self.transformed_output.grid)) # Use Grid's grid
        expected_colors = set(np.unique(self.task_pair.output.grid))
        return transformed_colors.issubset(expected_colors)

    @property
    def color_count_correct(self) -> bool | None:
        # Cannot compare counts if expected or transformed output is missing
        if self.task_pair.output is None or self.transformed_output is None:
            return None
        transformed_counts = dict(
            zip(*np.unique(self.transformed_output.grid, return_counts=True)) # Use Grid's grid
        )
        expected_counts = dict(
            zip(*np.unique(self.task_pair.output.grid, return_counts=True))
        )
        return transformed_counts == expected_counts

    @property
    def pixels_off(self) -> int | None:
        # Cannot calculate pixels off if expected output is missing,
        # transformed output is missing, or sizes don't match
        if self.task_pair.output is None or self.transformed_output is None or not self.size_correct:
            return None
        return int(np.sum(self.transformed_output.grid != self.task_pair.output.grid)) # Use Grid's grid

    @property
    def percent_correct(self) -> float | None:
        # Cannot calculate percent correct if pixels_off is None (due to missing grids or size mismatch)
        # or if expected output grid size is zero.
        if self.pixels_off is None or self.task_pair.output is None or self.task_pair.output.grid.size == 0:
            return None
        return 100.0 * ( # Use float division
            (self.task_pair.output.grid.size - self.pixels_off)
            / self.task_pair.output.grid.size
        )

    @property
    def score(self) -> float | None:
        """Calculates a score representing the difference between
        transformed and expected output."""
        # No score if there's no expected output to compare against
        if self.task_pair.output is None:
            return None

        if self.match:
            return 0.0 # Return float

        # No score if no transformation, error occurred, or basic metrics are unavailable
        if self.transformed_output is None or self.error is not None or self.pixels_off is None or self.percent_correct is None:
            return None

        score = 100.0 - self.percent_correct # Start with float

        if not self.color_count_correct:
            score *= 2

        if not self.color_palette_correct:
            score *= 2

        if not self.size_correct:
            score *= 2

        return float(score)

    def to_dict(self) -> dict:
        """Converts the trial results to a dictionary."""
        data = {
            #  "id": self.task_pair.index + 1,
            "match": self.match,
            "score": self.score,
            "input": self.input_string,
            # Only include expected_output if it exists
            # "expected_output": self.expected_output_string,
        }
        if self.expected_output_string is not None:
             data["expected_output"] = self.expected_output_string
        if self.transformed_output_string is not None:
            data["transformed_output"] = self.transformed_output_string
        if self.error is not None:
            data["error"] = self.error
        if self.function_output is not None:
            data["function_output"] = self.function_output
        if self.size_correct is not None:
            data["size_correct"] = self.size_correct
        if self.color_palette_correct is not None:
            data["color_palette_correct"] = self.color_palette_correct
        if self.color_count_correct is not None:
            data["color_count_correct"] = self.color_count_correct
        if self.pixels_off is not None:
            data["pixels_off"] = self.pixels_off
        if self.percent_correct is not None:
            data["percent_correct"] = self.percent_correct
        return data

    def generate_report(self) -> str:
        """Generates a report for this specific task pair trial."""
        report = ""
        if self.error:
            report += f"Error: {self.error}\n"
            if self.function_output:
                report += f"Function Output:\n```\n{self.function_output}\n```\n"
        else:
            report += f"Input:\n```\n{self.input_string}\n```\n"
            if self.expected_output_string is not None:
                report += f"Expected Output:\n```\n{self.expected_output_string}\n```\n"
            else:
                report += "Expected Output: None\n" # Indicate no expected output

            if self.transformed_output_string is not None:
                report += f"Transformed Output:\n```\n{self.transformed_output_string}\n```\n"
            else:
                report += "Transformed Output: None\n" # Indicate no transformed output

            # Only show comparison metrics if expected output exists
            if self.task_pair.output is not None:
                report += f"Match: {self.match}\n"
                report += f"Pixels Off: {self.pixels_off}\n"
                report += f"Size Correct: {self.size_correct}\n"
                report += f"Color Palette Correct: {self.color_palette_correct}\n"
                report += f"Color Count Correct: {self.color_count_correct}\n"
                report += f"Score: {self.score}\n"
            else:
                report += "Comparison Metrics: N/A (No Expected Output)\n"
        return report
