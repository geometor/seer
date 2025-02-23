"""
tools to parse and render tasks json files

task has two sets of data for training and testing
"""

import json
from pathlib import Path
from collections import Counter
from .grid import Grid
from PIL import Image, ImageDraw


class TaskPair:
    def __init__(self, puzzle_id, set_type, index, input_grid, output_grid=None):
        self.input = Grid(input_grid, puzzle_id, set_type, index, "input")
        self.output = (
            Grid(output_grid, puzzle_id, set_type, index, "output")
            if output_grid is not None
            else None
        )

    @property
    def weight(self):
        return self.input.size + (self.output.size if self.output else 0)

    @property
    def size_change(self):
        if self.output is None:
            return None
        return {
            "width": self.output.width - self.input.width,
            "height": self.output.height - self.input.height,
            "total": self.output.size - self.input.size,
        }

    @property
    def colors(self):
        return self.input.colors.union(self.output.colors if self.output else set())

    @property
    def color_changes(self):
        if self.output is None:
            return None
        input_counts = self.input.color_counts
        output_counts = self.output.color_counts
        return {
            color: output_counts.get(color, 0) - input_counts.get(color, 0)
            for color in self.colors
        }


class Task:
    def __init__(self, id, data):
        self.id = id
        self.train = [
            TaskPair(id, "train", i, pair["input"], pair["output"])
            for i, pair in enumerate(data["train"])
        ]
        self.test = [
            TaskPair(id, "test", i, test_input["input"], test_input.get("output"))
            for i, test_input in enumerate(data["test"])
        ]

    @property
    def all_pairs(self):
        return self.train + self.test

    @property
    def weight(self):
        return sum(pair.weight for pair in self.all_pairs)

    @property
    def colors(self):
        return set.union(*(pair.colors for pair in self.all_pairs))

    def nice_json_layout(self):
        def matrix_to_json_string(matrix):
            return (
                "[\n"
                + ",\n".join(f"          {row}" for row in matrix.tolist())
                + "\n        ]"
            )

        json_str = "{\n"
        json_str += f'  "id": "{self.id}",\n'
        json_str += '  "train": [\n'
        for pair in self.train:
            json_str += "    {\n"
            json_str += (
                '      "input": ' + matrix_to_json_string(pair.input.grid) + ",\n"
            )
            json_str += (
                '      "output": ' + matrix_to_json_string(pair.output.grid) + "\n"
            )
            json_str += "    },\n"
        json_str = json_str.rstrip(",\n") + "\n"
        json_str += "  ],\n"
        json_str += '  "test": [\n'
        for pair in self.test:
            json_str += "    {\n"
            json_str += (
                '      "input": ' + matrix_to_json_string(pair.input.grid) + ",\n"
            )
            if pair.output:
                json_str += (
                    '      "output": '
                    + matrix_to_json_string(pair.output.grid)
                    + "\n"
                )
            else:
                json_str += '      "output": null\n'
            json_str += "    },\n"
        json_str = json_str.rstrip(",\n") + "\n"
        json_str += "  ]\n"
        json_str += "}"

        return json_str

    def to_image(self, cell_spacing=10):
        """
        Creates a combined image for all train and test pairs in the task.
        Adds spacing between grids.
        """
        train_images = []
        for pair in self.train:
            train_images.append(pair.input.to_image(add_text=False))
            train_images.append(pair.output.to_image(add_text=False))

        test_images = []
        for pair in self.test:
            test_images.append(pair.input.to_image(add_text=False))
            if pair.output:  # Handle cases where test output might be None
                test_images.append(pair.output.to_image(add_text=False))

        # Find max width and height for consistent cell sizes
        max_width = 0
        max_height = 0
        for img in train_images + test_images:
            max_width = max(max_width, img.width)
            max_height = max(max_height, img.height)

        # Create combined image for train pairs
        train_table_width = len(self.train) * (max_width + cell_spacing) + cell_spacing
        train_table_height = 2 * (max_height + cell_spacing) + cell_spacing
        train_table = Image.new("RGB", (train_table_width, train_table_height), color="black")
        x_offset = cell_spacing
        for i in range(0, len(train_images), 2):
            train_table.paste(train_images[i], (x_offset, cell_spacing))
            train_table.paste(train_images[i + 1], (x_offset, max_height + 2 * cell_spacing))
            x_offset += max_width + cell_spacing

        # Create combined image for test pairs
        test_table_width = len(self.test) * (max_width + cell_spacing) + cell_spacing
        test_table_height = (
            2 * (max_height + cell_spacing) + cell_spacing
            if any(pair.output for pair in self.test)
            else max_height + 2 * cell_spacing  # Corrected height
        )
        test_table = Image.new("RGB", (test_table_width, test_table_height), color="black")
        x_offset = cell_spacing
        for i in range(0, len(test_images), 2):
            test_table.paste(test_images[i], (x_offset, cell_spacing))
            # Handle potential missing test outputs
            if i + 1 < len(test_images):
                test_table.paste(test_images[i + 1], (x_offset, max_height + 2 * cell_spacing))
            x_offset += max_width + cell_spacing

        # Combine train and test tables vertically
        total_width = max(train_table_width, test_table_width)
        total_height = train_table_height + test_table_height
        final_image = Image.new("RGB", (total_width, total_height), color="black")

        # Center the train and test tables
        train_x_offset = (total_width - train_table_width) // 2
        test_x_offset = (total_width - test_table_width) // 2

        final_image.paste(train_table, (train_x_offset, 0))
        final_image.paste(test_table, (test_x_offset, train_table_height))

        return final_image


class Tasks(list):
    def __init__(self, folder_path="."):
        self.extend(self._load_tasks(Path(folder_path)))

    def _load_tasks(self, folder_path):
        tasks = []
        for file_path in sorted(folder_path.glob("*.json")):
            task_id = file_path.stem  # Get filename without extension
            with file_path.open("r") as f:
                data = json.load(f)
                tasks.append(Task(task_id, data))
        return tasks

    def get_ordered_tasks(self, key="weight", reverse=False):
        return sorted(self, key=lambda p: getattr(p, key), reverse=reverse)

    def get_tasks_by_color_count(self, count):
        return [p for p in self if len(p.colors) == count]

    def get_tasks_by_size_change(self, change_type="total", value=0):
        return [
            p
            for p in self
            if any(
                pair.size_change and pair.size_change[change_type] == value
                for pair in p.all_pairs
            )
        ]
