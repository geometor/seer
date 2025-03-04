"""
A Textual app that displays ARC-style colored grids with grid lines separating the cells.
It demonstrates several rendering methods (image-based, Unicode block, and half-block) with grid lines.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid  # Import Grid
from textual.widgets import Static, Button, ListView, ListItem, Label, Footer
from geometor.seer.navigator.base_grid import BaseGrid
from geometor.seer.tasks.tasks import Task  # Import Task
import numpy as np

# Global constants for grid lines in text modes and image mode.
GRID_LINE_COLOR = "black"
GRID_LINE_WIDTH = (
    1  # For text modes: in number of characters; for image mode: in pixels.
)

# Define a color palette mapping for grid values (0-9) to colors.
COLOR_PALETTE = {
    0: "white",
    1: "red",
    2: "green",
    3: "yellow",
    4: "blue",
    5: "magenta",
    6: "cyan",
    7: "gold",
    8: "#ff8800",  # orange
    9: "#00ffff",  # cyan variant
}

# Example ARC-style grid data (each number corresponds to a color in COLOR_PALETTE)
GRID_DATA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 1, 1, 4, 3, 2, 1],
    [1, 2, 3, 4, 1, 1, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class SplitBlockGrid(BaseGrid):
    """
    first row cells are made of 3 characters - half vertical and full
    next row made of top and bottom half - 1 space, 1 half block
    " ██"
    " ▄▄"
    " ▀▀"
    """

    def render(self):
        from rich.text import Text

        text = Text()
        # For each row in the grid
        for row_num, row in enumerate(self.grid):
            if row_num % 2:
                for cell in row:
                    fill_color = COLOR_PALETTE.get(cell, "black")
                    text.append(" ██", style=fill_color)
                text.append("\n")
            else:
                top_half = Text()
                bottom_half = Text()
                for cell in row:
                    fill_color = COLOR_PALETTE.get(cell, "black")
                    top_half.append(" ▄▄", style=fill_color)
                    bottom_half.append(" ▀▀", style=fill_color)
                text.append(top_half)
                text.append("\n")
                text.append(bottom_half)
                text.append("\n")
        return text



class SquareCharGrid(BaseGrid):
    """
    Renders each grid cell as a single Unicode square character (default: '■'),
    styled with the cell's fill color.

    You can switch the character to something else (e.g. '⬛', '◼', '▣') if desired.
    """

    SQUARE_CHAR = "■" # &#11200; black square centred
    SQUARE_CHAR = "■" # &#9632; black square
    SQUARE_CHAR = "▀ " # &#9632; black square
    #  SQUARE_CHAR = "█" # &#9632; black square
    #  SQUARE_CHAR = "●" # &#9632; black square

    # ◼"  # Change this to another square if you like.

    def render(self):
        from rich.text import Text
        text = Text()

        # Loop over each row in the grid
        for row in self.grid:
            line = Text()
            # For each cell, append the chosen square character, styled in the cell's color
            for cell_value in row:
                fill_color = COLOR_PALETTE.get(cell_value, "black")
                # Append the square character with the fill color
                line.append(self.SQUARE_CHAR, style=fill_color)
            # Add a newline after finishing a row
            line.append("\n")
            text.append(line)
        return text




class Navigator(App):
    CSS_PATH = "navigator.tcss"  # Use a separate CSS file
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, tasks: list, **kwargs):
        super().__init__(**kwargs)
        self.tasks = tasks

    def compose(self) -> ComposeResult:
        """Create the UI layout."""
        with Horizontal():
            with Vertical(id="task-selection"):
                yield Static("Select a Task:", id="task_title")
                self.list_view = ListView()  # Create the ListView, but don't add items yet
                yield self.list_view
            with Vertical(id="grid-display"):
                self.grid_container = Grid(id="grid-container")
                yield self.grid_container  # Add the grid container here
            yield Footer()

    def on_mount(self) -> None:
        """Populate the list view after mounting."""
        if self.tasks:  # Check if tasks are available
            for task in self.tasks:
                self.list_view.append(ListItem(Label(str(task.id)), id=f"task_{task.id}"))
            self.display_task(self.tasks[0].id)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Event handler for list view selection."""
        task_id = event.item.id.removeprefix("task_")
        self.display_task(task_id)

    def display_task(self, task_id: str) -> None:
        """Display the selected task."""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            return

        # Clear previous grids
        for widget in list(self.grid_container.children):
            self.grid_container.remove_widget(widget)

        # Create and add new grids
        self._create_grid_widgets(task)


    def _create_grid_widgets(self, task: Task):
        """Creates the grid widgets for the given task."""

        # Determine max grid sizes for layout
        max_train_input_width = 0
        max_train_output_width = 0
        for task_pair in task.train:
            max_train_input_width = max(max_train_input_width, task_pair.input.grid.shape[1])
            if task_pair.output:
                max_train_output_width = max(max_train_output_width, task_pair.output.grid.shape[1])

        max_test_input_width = 0
        max_test_output_width = 0
        if task.test:
            for task_pair in task.test:
                max_test_input_width = max(max_test_input_width, task_pair.input.grid.shape[1])
                if task_pair.output:
                    max_test_output_width = max(max_test_output_width, task_pair.output.grid.shape[1])

        # Define areas *before* adding columns and rows
        areas = {
            f"train_in_{i}": f"col0,train-{i}"
            for i in range(len(task.train))
        }
        areas.update({
            f"train_out_{i}": f"col1,train-{i}"
            for i in range(len(task.train))
        })

        if task.test:
            num_test_input_cols = len(task.test)
            num_test_output_cols = sum(1 for tp in task.test if tp.output)
            areas.update({
                f"test_input_{i}": f"test_in-{i},test_input"
                for i in range(num_test_input_cols)
            })
            areas.update({
                f"test_output_{i}": f"test_out-{i},test_output"
                for i in range(num_test_output_cols)
            })


        # Add columns and rows *before* placing any widgets
        self.grid_container.add_column("col0", size=max_train_input_width + 1)  # +1 for spacing
        self.grid_container.add_column("col1", size=max_train_output_width + 1)
        self.grid_container.add_row("train", repeat=len(task.train))

        if task.test:
            self.grid_container.add_row("test_input")
            self.grid_container.add_row("test_output")
            self.grid_container.add_column("test_in", repeat=num_test_input_cols, size=max_test_input_width + 1)
            self.grid_container.add_column("test_out", repeat=num_test_output_cols, size=max_test_output_width + 1)

        self.grid_container.add_areas(**areas) # Add areas *after* rows/cols


        # Add train grids
        for i, task_pair in enumerate(task.train):
            input_grid = SquareCharGrid(task_pair.input.grid)  # Use SquareCharGrid
            output_grid = SquareCharGrid(task_pair.output.grid) if task_pair.output else Static("")

            self.grid_container.place(input_grid, area=f"train_in_{i}")
            self.grid_container.place(output_grid, area=f"train_out_{i}")

        # Add test grids, if they exist
        if task.test:
            j = 0 # counter for output grids
            for i, task_pair in enumerate(task.test):
                input_grid = SquareCharGrid(task_pair.input.grid)
                self.grid_container.place(input_grid, area=f"test_input_{i}")

                if task_pair.output:
                    output_grid = SquareCharGrid(task_pair.output.grid)
                    self.grid_container.place(output_grid, area=f"test_output_{j}")
                    j += 1

        self.grid_container.refresh()


def main():
    """
    Loads tasks from the specified directory and runs the Navigator to display them.
    """
    from pathlib import Path
    from geometor.seer.tasks.tasks import Tasks
    from geometor.seer.navigator.navigator import Navigator

    # --- Configuration ---
    TASKS_DIR = Path("/home/phi/PROJECTS/geometor/seer_sessions/run/tasks/ARC/training")

    # 1. Load tasks
    if not TASKS_DIR.exists():
        print(f"Error: Tasks directory '{TASKS_DIR}' not found.")
        print("Please create a 'tasks' directory and place your JSON task files in it.")
        return

    try:
        tasks = Tasks(TASKS_DIR)
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return

    if not tasks:
        print("No tasks found in the 'tasks' directory.")
        return

    # 2. Create and run the Navigator app
    app = Navigator(tasks[:5])  # Limit to 5 tasks for demonstration
    app.run()

if __name__ == "__main__":
    main()
