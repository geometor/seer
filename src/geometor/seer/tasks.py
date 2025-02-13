"""
Defines the data structures for representing tasks, including input/output grids and task configurations.

This module provides classes for handling ARC tasks, enabling easy loading, manipulation, and saving of task data.
It includes functionalities for converting grids to and from JSON, ensuring compatibility with the ARC dataset format.
"""

from pathlib import Path
import json
from PIL import Image
import numpy as np


class Tasks:
    """Represents a collection of ARC tasks, providing methods to load and manage them."""

    def __init__(self, task_dir: str = "data/training"):
        self.task_dir = Path(task_dir)
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> list:
        """Loads tasks from the specified directory."""
        tasks = []
        for task_file in self.task_dir.glob("*.json"):
            try:
                with open(task_file, "r") as f:
                    task_data = json.load(f)
                task = Task(task_data, task_file.stem)
                tasks.append(task)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading task {task_file}: {e}")
        return tasks

    def __iter__(self):
        """Iterator for the list of tasks."""
        return iter(self.tasks)


class Task:
    """Represents a single ARC task, including training and test examples."""

    def __init__(self, task_json: dict, task_id: str):
        self.id = task_id
        self.train = [
            Pair(pair["input"], pair["output"]) for pair in task_json["train"]
        ]
        self.test = [Pair(pair["input"], pair["output"]) for pair in task_json["test"]]


class Pair:
    """Represents an input/output pair of grids within a task."""

    def __init__(self, input_grid: list, output_grid: list):
        self.input = Grid(input_grid)
        self.output = Grid(output_grid)


class Grid:
    """Represents a single grid, either input or output, within an ARC task."""

    COLOR_MAP = {
        0: (238, 238, 238),  # white
        1: (30, 147, 255),  # blue
        2: (220, 50, 40),  # red
        3: (79, 204, 48),  # green
        4: (230, 200, 0),  # yellow
        5: (85, 85, 85),  # gray
        6: (229, 58, 163),  # magenta
        7: (230, 120, 20),  # orange
        8: (135, 216, 241),  # azure
        9: (146, 18, 49),  # maroon
    }
    def __init__(self, grid: list):
        self.grid = np.array(grid)
        self.height, self.width = self.grid.shape

    def to_image(self, cell_size: int = 16) -> Image.Image:
        """Converts the grid to a PIL Image."""
        img = Image.new(
            "RGB", (self.width * cell_size, self.height * cell_size), "white"
        )
        for y in range(self.height):
            for x in range(self.width):
                color = self.COLOR_MAP.get(self.grid[y, x], (0, 0, 0))  # Default to black
                self._draw_cell(img, x, y, cell_size, color)
        return img

    def _draw_cell(self, img: Image.Image, x: int, y: int, size: int, color: tuple):
        """Draws a single cell on the image."""
        for i in range(size):
            for j in range(size):
                px, py = x * size + i, y * size + j
                if px < img.width and py < img.height:
                    img.putpixel((px, py), color)

    def to_python_string(self):
        """
        Converts a grid (represented as a nested list or numpy array)
        into a Python list of lists string representation, with each row
        on a new line.
        """
        if isinstance(self.grid, np.ndarray):
            grid_list = self.grid.tolist()
        else:
            grid_list = self.grid

        rows = [str(row) for row in grid_list]
        output = "[\n"
        for row in rows:
            output += f"    {row},\n"
        output += "]"
        return output
