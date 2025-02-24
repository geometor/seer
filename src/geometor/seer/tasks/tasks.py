"""
tools to parse and render tasks json files

task has two sets of data for training and testing
"""

import json
from pathlib import Path
from collections import Counter
from .grid import Grid
from PIL import Image, ImageDraw
from geometor.seer import verifier


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

    def to_image(self, cell_spacing=10, train_results=None, test_results=None, show_test=True):
        """
        Creates a combined image for all train and test pairs in the task.
        Adds spacing between grids.
        Optionally includes result grids.
        """
        cell_spacing *= 2  # Double the cell spacing
        outer_border = cell_spacing  # Use doubled cell spacing as outer border

        train_images = []
        for i, pair in enumerate(self.train):
            train_images.append(pair.input.to_image(add_text=False))
            train_images.append(pair.output.to_image(add_text=False))
            if train_results and "transformed_output" in train_results[i]:
                try:
                    result_grid_str = train_results[i]["transformed_output"]
                    result_grid = verifier.string_to_grid(result_grid_str)
                    train_images.append(result_grid.to_image(add_text=False))
                except Exception as e:
                    print(f"Error processing train result image: {e}")

        test_images = []
        if show_test:  # Only process test images if show_test is True
            for i, pair in enumerate(self.test):
                test_images.append(pair.input.to_image(add_text=False))
                if pair.output:  # Handle cases where test output might be None
                    test_images.append(pair.output.to_image(add_text=False))
                if test_results and "transformed_output" in test_results[i]:
                    try:
                        result_grid_str = test_results[i]["transformed_output"]
                        result_grid = verifier.string_to_grid(result_grid_str)
                        test_images.append(result_grid.to_image(add_text=False))
                    except Exception as e:
                        print(f"Error processing test result image: {e}")


        def calculate_dimensions(images, num_cols, num_rows):
            col_widths = [0] * num_cols
            row_heights = [0] * num_rows

            for i, img in enumerate(images):
                row = i // num_cols
                col = i % num_cols
                col_widths[col] = max(col_widths[col], img.width)
                row_heights[row] = max(row_heights[row], img.height)
            return col_widths, row_heights

        # --- Train Table ---
        num_train_cols = max(len(self.train), len(train_results) if train_results else 0 ) # Input, Output, (Result)
        num_train_rows = 2 + (1 if train_results else 0)
        train_col_widths, train_row_heights = calculate_dimensions(train_images, num_train_cols, num_train_rows)

        train_table_width = sum(train_col_widths) + (num_train_cols -1) * cell_spacing + 2 * outer_border
        train_table_height = sum(train_row_heights) + (num_train_rows - 1) * cell_spacing + 2 * outer_border

        train_table = Image.new("RGB", (train_table_width, train_table_height), color="black")

        x_offset = outer_border
        y_offset = outer_border

        # Input Row
        for i, pair in enumerate(self.train):
            train_table.paste(pair.input.to_image(add_text=False), (x_offset, y_offset))
            x_offset += train_col_widths[i] + cell_spacing

        # Output Row
        x_offset = outer_border
        y_offset += train_row_heights[0] + cell_spacing
        for i, pair in enumerate(self.train):
            train_table.paste(pair.output.to_image(add_text=False), (x_offset, y_offset))
            x_offset += train_col_widths[i] + cell_spacing

        # Result Row
        if train_results:
            x_offset = outer_border
            y_offset += train_row_heights[1] + cell_spacing
            for i, result in enumerate(train_results):
                if "transformed_output" in result:
                    try:
                        result_grid_str = result["transformed_output"]
                        result_grid = verifier.string_to_grid(result_grid_str)
                        result_image = result_grid.to_image(add_text=False)
                        train_table.paste(result_image, (x_offset, y_offset))
                        x_offset += train_col_widths[i] + cell_spacing
                    except Exception as e:
                        print(f"Error processing train result image: {e}")

        # --- Test Table ---
        if show_test:
            num_test_cols = max(len(self.test), len(test_results) if test_results else 0)
            num_test_rows = 1 + (1 if any(pair.output for pair in self.test) else 0) + (1 if test_results else 0)  # Input, Output, Result
            test_col_widths, test_row_heights = calculate_dimensions(test_images, num_test_cols, num_test_rows)

            test_table_width = sum(test_col_widths) + (num_test_cols - 1) * cell_spacing + 2 * outer_border
            test_table_height = sum(test_row_heights) + (num_test_rows - 1) * cell_spacing + 2 * outer_border

            test_table = Image.new("RGB", (test_table_width, test_table_height), color="black")

            x_offset = outer_border
            y_offset = outer_border

            # Input Row
            for i, pair in enumerate(self.test):
                test_table.paste(pair.input.to_image(add_text=False), (x_offset, y_offset))
                x_offset += test_col_widths[i] + cell_spacing

            # Output Row
            if any(pair.output for pair in self.test):
                x_offset = outer_border
                y_offset += test_row_heights[0] + cell_spacing
                for i, pair in enumerate(self.test):
                    if pair.output:
                        test_table.paste(pair.output.to_image(add_text=False), (x_offset, y_offset))
                        x_offset += test_col_widths[i] + cell_spacing

            # Result Row
            if test_results:
                x_offset = outer_border
                y_offset += test_row_heights[1 if any(pair.output for pair in self.test) else 0] + cell_spacing
                for i, result in enumerate(test_results):
                    if "transformed_output" in result:
                        try:
                            result_grid_str = result["transformed_output"]
                            result_grid = verifier.string_to_grid(result_grid_str)
                            result_image = result_grid.to_image(add_text=False)
                            test_table.paste(result_image, (x_offset, y_offset))
                            x_offset += test_col_widths[i] + cell_spacing
                        except Exception as e:
                            print(f"Error processing test result image: {e}")

            # --- Combine Train and Test Tables ---
            total_width = max(train_table_width, test_table_width)
            total_height = train_table_height + test_table_height + outer_border # Add spacing between tables
            final_image = Image.new("RGB", (total_width, total_height), color="black")

            # Center the train and test tables
            train_x_offset = (total_width - train_table_width) // 2
            test_x_offset = (total_width - test_table_width) // 2

            final_image.paste(train_table, (train_x_offset, outer_border))
            final_image.paste(test_table, (test_x_offset, train_table_height + outer_border)) # Add spacing

        else:  # --- Only Train Table ---
            final_image = Image.new("RGB", (train_table_width, train_table_height), color="black")
            final_image.paste(train_table, (outer_border, outer_border))  # Center train table

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
