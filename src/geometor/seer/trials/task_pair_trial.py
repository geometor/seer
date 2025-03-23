from __future__ import annotations
from typing import TYPE_CHECKING

import numpy as np
from geometor.seer.tasks.grid import Grid

if TYPE_CHECKING:
    from geometor.seer.tasks.tasks import TaskPair

class TaskPairTrial:
    def __init__(
        self,
        task_pair: TaskPair,
        transformed_output: np.ndarray | None = None,
        error: str | None = None,
        function_output: str | None = None,
    ):
        self.task_pair = task_pair
        self.transformed_output = transformed_output
        self.error = error
        self.function_output = function_output

    @property
    def input_string(self) -> str:
        return self.task_pair.input.to_string()

    @property
    def expected_output_string(self) -> str:
        return self.task_pair.output.to_string()

    @property
    def transformed_output_string(self) -> str | None:
        if self.transformed_output is None:
            return None
        return Grid(self.transformed_output, "", "", "", "").to_string()

    @property
    def match(self) -> bool:
        if self.transformed_output is None or self.error is not None:
            return False
        return np.array_equal(self.transformed_output, self.task_pair.output.grid)

    @property
    def size_correct(self) -> bool:
        if self.transformed_output is None:
            return False
        return self.transformed_output.shape == self.task_pair.output.grid.shape

    @property
    def color_palette_correct(self) -> bool:
        if self.transformed_output is None:
            return False
        transformed_colors = set(np.unique(self.transformed_output))
        expected_colors = set(np.unique(self.task_pair.output.grid))
        return transformed_colors.issubset(expected_colors)

    @property
    def color_count_correct(self) -> bool:
        if self.transformed_output is None:
            return False
        transformed_counts = dict(
            zip(*np.unique(self.transformed_output, return_counts=True))
        )
        expected_counts = dict(
            zip(*np.unique(self.task_pair.output.grid, return_counts=True))
        )
        return transformed_counts == expected_counts

    @property
    def pixels_off(self) -> int | None:
        if self.transformed_output is None or not self.size_correct:
            return None
        return int(np.sum(self.transformed_output != self.task_pair.output.grid))

    @property
    def percent_correct(self) -> float | None:
        if self.pixels_off is None:
            return None
        return 100 * (
            (self.task_pair.output.grid.size - self.pixels_off)
            / self.task_pair.output.grid.size
        )

    @property
    def score(self) -> float | None:
        """Calculates a score representing the difference between transformed and expected output."""
        if self.match:
            return 0

        if self.transformed_output is None or self.error is not None:
            return None  # No score if no transformation or error

        if self.pixels_off is None:  # Should not happen, but handle for safety
            return None

        score = 100 - self.percent_correct

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
            "expected_output": self.expected_output_string,
        }
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
