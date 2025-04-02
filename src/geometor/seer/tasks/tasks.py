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
            return None # No size change if there's no output grid
        return {
            "width": self.output.width - self.input.width,
            "height": self.output.height - self.input.height,
            "total": self.output.size - self.input.size,
        }

    @property
    def colors(self):
        # Returns colors from input and output (if output exists)
        if self.output:
            return self.input.colors.union(self.output.colors)
        return self.input.colors # Only input colors if no output

    @property
    def color_changes(self):
        if self.output is None:
            return None # No color changes if there's no output grid
        input_counts = self.input.color_counts
        output_counts = self.output.color_counts
        all_colors = self.input.colors.union(self.output.colors) # Use combined colors
        return {
            color: output_counts.get(color, 0) - input_counts.get(color, 0)
            for color in all_colors
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
                # Handle cases where output might be None (e.g., test pairs)
                output_image = pair.output.to_image(add_text=False) if pair.output else None
                output_row.append(output_image)
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
                    if img: # Check if img is not None before pasting
                        # Center the image within its allocated cell space if needed
                        # For simplicity, we'll just paste at the top-left for now.
                        # Adjust paste position if centering or alignment is desired.
                        paste_x = x_offset
                        paste_y = y_offset
                        table_image.paste(img, (paste_x, paste_y))
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


# --- Standalone Utility Functions ---

def load_tasks_from_kaggle_json(file_path: Path) -> 'Tasks':
    """
    Loads tasks from a single JSON file where the top level is a dictionary
    mapping task IDs to task data (containing 'train' and 'test' lists).

    Args:
        file_path: The path to the JSON file.

    Returns:
        A Tasks object containing the loaded tasks. Returns an empty Tasks
        object if the file is not found, is invalid JSON, or has an
        unexpected structure.
    """
    tasks_list = []
    # Create an empty Tasks object upfront for potential error returns and final result
    tasks_obj = Tasks.__new__(Tasks)
    tasks_obj.clear()

    try:
        if not file_path.is_file():
            print(f"Error: Kaggle JSON file not found: {file_path}")
            return tasks_obj # Return empty Tasks

        with file_path.open("r") as f:
            all_task_data = json.load(f)

        if not isinstance(all_task_data, dict):
            print(f"Error: Expected top-level JSON structure to be a dictionary (task_id: task_data), but got {type(all_task_data)} in {file_path}")
            return tasks_obj # Return empty Tasks

        for task_id, task_data in all_task_data.items():
            try:
                # Basic validation of task_data structure
                if isinstance(task_data, dict) and "train" in task_data and "test" in task_data:
                    task_obj = Task(task_id, task_data)
                    tasks_list.append(task_obj)
                else:
                     print(f"Warning: Skipping task '{task_id}' due to unexpected data structure: {task_data}")
            except Exception as e:
                print(f"Warning: Error processing task '{task_id}' from {file_path}: {e}")
                # Optionally continue to process other tasks

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in file {file_path}: {e}")
        return tasks_obj # Return empty Tasks
    except Exception as e:
        print(f"Error reading or processing Kaggle JSON file {file_path}: {e}")
        return tasks_obj # Return empty Tasks

    # Populate the final Tasks object
    tasks_obj.extend(tasks_list)
    print(f"Successfully loaded {len(tasks_obj)} tasks from {file_path}")
    return tasks_obj


def get_unsolved_tasks(sessions_root: Path) -> Tasks:
    """
    Scans session summaries to find all unique tasks present across sessions
    that have never passed the test phase. Loads these tasks from their
    task.json files.

    Args:
        sessions_root: The root directory containing session folders.

    Returns:
        A new Tasks object containing only the unsolved tasks found across all
        sessions. Returns an empty Tasks object if sessions_root is invalid,
        no tasks are found, or scanning fails.
    """
    solved_task_ids = set()
    tasks_in_sessions = {} # Store task_id -> path to a task.json

    # Create an empty Tasks object upfront for potential error returns and final result
    unsolved_tasks_obj = Tasks.__new__(Tasks)
    unsolved_tasks_obj.clear()

    try:
        if not sessions_root.is_dir():
            print(f"Error: Sessions root directory not found: {sessions_root}")
            return unsolved_tasks_obj # Return empty Tasks

        # First pass: Identify all tasks and check solved status
        for session_dir in sessions_root.iterdir():
            if session_dir.is_dir():
                for task_dir in session_dir.iterdir():
                    if task_dir.is_dir():
                        task_id = task_dir.name
                        # Store a path to task.json if we haven't seen this task yet
                        # or if the current one exists (prefer existing ones)
                        task_json_path = task_dir / "task.json"
                        if task_id not in tasks_in_sessions or task_json_path.exists():
                             if task_json_path.exists(): # Only store if task.json actually exists
                                tasks_in_sessions[task_id] = task_json_path

                        # Check solved status from index.json
                        summary_path = task_dir / "index.json"
                        if summary_path.exists():
                            try:
                                with open(summary_path, "r") as f:
                                    summary = json.load(f)
                                if summary.get("test_passed") is True:
                                    solved_task_ids.add(task_id)
                            except (json.JSONDecodeError, Exception) as e:
                                print(f"Warning: Could not read/parse summary for {task_dir}: {e}")

    except Exception as e:
        print(f"Error scanning sessions directory {sessions_root}: {e}")
        return unsolved_tasks_obj # Return empty Tasks

    # Determine unsolved task IDs
    unsolved_task_ids = set(tasks_in_sessions.keys()) - solved_task_ids

    # Load Task objects for unsolved tasks
    unsolved_tasks_list = []
    for task_id in sorted(list(unsolved_task_ids)): # Sort for consistent order
        task_json_path = tasks_in_sessions.get(task_id)
        if task_json_path and task_json_path.exists():
            try:
                with open(task_json_path, "r") as f:
                    task_data = json.load(f)
                task_obj = Task(task_id, task_data)
                unsolved_tasks_list.append(task_obj)
            except (json.JSONDecodeError, Exception) as e:
                print(f"Error loading task.json for unsolved task {task_id} from {task_json_path}: {e}")
        else:
             print(f"Warning: Could not find or access task.json for unsolved task {task_id} (expected at {task_json_path})")


    # Populate the final Tasks object
    unsolved_tasks_obj.extend(unsolved_tasks_list)

    return unsolved_tasks_obj
