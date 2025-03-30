"""
tools to parse and render tasks json files

task has two sets of data for training and testing
"""

import json
from pathlib import Path
from collections import Counter
from PIL import Image, ImageDraw

from geometor.seer.tasks.grid import Grid, string_to_grid
#  from geometor.seer.trials import verifier



class TaskPair(dict):
    def __init__(self, puzzle_id, set_type, index, input_grid, output_grid=None):
        self.input = Grid(input_grid, puzzle_id, set_type, index, "input")
        self["input"] = self.input
        self.output = (
            Grid(output_grid, puzzle_id, set_type, index, "output")
            if output_grid is not None
            else None
        )
        self["output"] = self.output

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
                    '      "output": ' + matrix_to_json_string(pair.output.grid) + "\n"
                )
            else:
                json_str += '      "output": null\n'
            json_str += "    },\n"
        json_str = json_str.rstrip(",\n") + "\n"
        json_str += "  ]\n"
        json_str += "}"

        return json_str

    # TODO: let's have separate parameters for outer_border, column_space, and row_space AI!
    # remove cell spacing
    def to_image(
        self,
        train_results: list = None,
        test_results: list = None,
        show_test=True,
        outer_border=32,
        col_spacing=32,
        row_spacing=16,
    ):
        """
        Creates a combined image for all train and test pairs in the task.
        Adds spacing between grids.
        Optionally includes result grids.
        """


        def get_table_images(task_set, result_set):
            images = []
            input_row = []
            for i, pair in enumerate(task_set):
                input_row.append(pair.input.to_image(add_text=False))
            images.append(input_row)

            output_row = []
            for i, pair in enumerate(task_set):
                output_row.append(pair.output.to_image(add_text=False))
            images.append(output_row)


            if result_set and "trials" in result_set:
                result_row = []
                for result in result_set["trials"]:
                    #  result_grid_str = result["transformed_output"]
                    # result_grid = Grid(result.transformed_output) # NO! already a Grid
                    result_row.append(result.transformed_output.to_image(add_text=False))
                images.append(result_row)

            return images

        train_images = get_table_images(self.train, train_results)

        test_images = []

        if show_test:  # Only process test images if show_test is True
            test_images = get_table_images(self.test, test_results)

        def calculate_dimensions(images, num_cols, num_rows):
            col_widths = [0] * num_cols
            row_heights = [0] * num_rows

            for i, img in enumerate(images):
                row = i // num_cols
                col = i % num_cols
                col_widths[col] = max(col_widths[col], img.width)
                row_heights[row] = max(row_heights[row], img.height)
            return col_widths, row_heights

        def get_table(images):
            row_heights = []
            for row in images:
                max_row_height = 0
                for img in row:
                    if img and img.height > max_row_height:
                        max_row_height = img.height 
                row_heights.append(max_row_height)

            col_widths = [0] * len(images[0])
            #  for row in images[0]:
                #  col_widths.append(0)
            for row in images:
                for i, img in enumerate(row):
                    if img and img.width > col_widths[i]:
                        col_widths[i] = img.width 

            table_width = sum(col_widths) + (len(col_widths) - 1) * col_spacing
            table_height = sum(row_heights) + (len(row_heights) - 1) * row_spacing

            table_image = Image.new(
                "RGB",
                (
                    table_width,
                    table_height,
                ),
                color="black",
            )

            y_offset = 0

            for row_id, row in enumerate(images):
                x_offset = 0
                for col_id, img in enumerate(row):
                    if img:
                        table_image.paste(img, (x_offset, y_offset))
                    x_offset += col_widths[col_id] + col_spacing
                y_offset += row_heights[row_id] + row_spacing

            return table_image

        train_table = get_table(train_images)
        if show_test:
            test_table = get_table(test_images)

        total_width = train_table.width + (2 * outer_border)
        if show_test:
            if train_table.width < test_table.width:
                total_width = test_table.width + (2 * outer_border)

        total_height = train_table.height + (2 * outer_border)
        if show_test:
            total_height += test_table.height + outer_border

        final_image = Image.new("RGB", (total_width, total_height), color="black")

        final_image.paste(train_table, (outer_border, outer_border))
        if show_test:
            final_image.paste(
                test_table, (outer_border, train_table.height + 2 * outer_border)
            )  

        return final_image

    def rotate(self, k=1):
        """
        Rotates all grids in the task by 90 degrees clockwise k times.
        Returns a new Task object with the rotated grids.
        """
        rotated_train = [
            TaskPair(
                self.id,
                "train",
                i,
                pair.input.rotate(k).grid,
                pair.output.rotate(k).grid,
            )
            for i, pair in enumerate(self.train)
        ]
        rotated_test = [
            TaskPair(
                self.id,
                "test",
                i,
                pair.input.rotate(k).grid,
                pair.output.rotate(k).grid if pair.output else None,
            )
            for i, pair in enumerate(self.test)
        ]
        rotated_data = {"train": [], "test": []}
        for pair in rotated_train:
            rotated_data["train"].append(
                {"input": pair.input.grid.tolist(), "output": pair.output.grid.tolist()}
            )
        for pair in rotated_test:
            rotated_data["test"].append(
                {
                    "input": pair.input.grid.tolist(),
                    "output": pair.output.grid.tolist() if pair.output else None,
                }
            )

        return Task(self.id, rotated_data)


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

    def get_ordered_by_train_count(self, reverse=False):
        return sorted(self, key=lambda task: len(task.train), reverse=reverse)

    def get_unsolved_tasks(self, sessions_root: Path) -> 'Tasks':
        """
        Scans all sessions to find tasks that have never passed the test phase.

        Args:
            sessions_root: The root directory containing session folders.

        Returns:
            A new Tasks object containing only the unsolved tasks found in the
            original Tasks list that also exist in the sessions.
        """
        solved_task_ids = set()
        tasks_in_sessions = set()

        try:
            if not sessions_root.is_dir():
                print(f"Error: Sessions root directory not found: {sessions_root}")
                # Return an empty Tasks object or raise an error? Returning empty for now.
                empty_tasks = Tasks.__new__(Tasks) # Create instance without calling __init__
                empty_tasks.clear() # Ensure it's empty
                return empty_tasks


            for session_dir in sessions_root.iterdir():
                if session_dir.is_dir():
                    for task_dir in session_dir.iterdir():
                        if task_dir.is_dir():
                            task_id = task_dir.name
                            tasks_in_sessions.add(task_id)
                            summary_path = task_dir / "index.json"
                            if summary_path.exists():
                                try:
                                    with open(summary_path, "r") as f:
                                        summary = json.load(f)
                                    if summary.get("test_passed") is True:
                                        solved_task_ids.add(task_id)
                                except (json.JSONDecodeError, Exception) as e:
                                    # Log or print warning about corrupted summary?
                                    print(f"Warning: Could not read/parse summary for {task_dir}: {e}")
        except Exception as e:
            print(f"Error scanning sessions directory {sessions_root}: {e}")
            # Return an empty Tasks object or raise an error? Returning empty for now.
            empty_tasks = Tasks.__new__(Tasks) # Create instance without calling __init__
            empty_tasks.clear() # Ensure it's empty
            return empty_tasks


        # Filter the current Tasks list based on the findings
        unsolved_tasks_list = [
            task for task in self
            if task.id in tasks_in_sessions and task.id not in solved_task_ids
        ]

        # Create a new Tasks object to hold the result
        # Use __new__ and manually extend to avoid re-running __init__ which loads from disk
        unsolved_tasks_obj = Tasks.__new__(Tasks)
        unsolved_tasks_obj.clear() # Ensure it starts empty
        unsolved_tasks_obj.extend(unsolved_tasks_list)

        return unsolved_tasks_obj
