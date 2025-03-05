"""
A Textual app that displays ARC-style colored grids with grid lines separating the cells.
It demonstrates several rendering methods (image-based, Unicode block, and half-block) with grid lines.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid, ScrollableContainer # Import Grid
from textual.widgets import Static, Button, ListView, ListItem, Label, Footer

from geometor.seer.navigator.renderers.char_grid import CharGrid
from geometor.seer.navigator.renderers.block_grid import BlockGrid
from geometor.seer.navigator.renderers.solid_grid import SolidGrid
from geometor.seer.tasks.tasks import Task  # Import Task
import numpy as np

class Navigator(App):
    CSS_PATH = "navigator.tcss"  # Use a separate CSS file
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "set_renderer_solid", "Solid"),
        ("c", "set_renderer_char", "Char"),
        ("b", "set_renderer_block", "Block"),
    ]

    def __init__(self, tasks: list, renderer=SolidGrid, **kwargs):
        super().__init__(**kwargs)
        self.tasks = tasks
        self.renderer = SolidGrid

    def compose(self) -> ComposeResult:
        """Create the UI layout."""
        with Horizontal():
            with Vertical(id="task-selection"):
                yield Static("Select a Task:", id="task_title")
                self.list_view = (
                    ListView()
                )  # Create the ListView, but don't add items yet
                yield self.list_view
            with ScrollableContainer(id="grid-display"):
                self.grid_container = Grid(id="grid-container")
                yield self.grid_container  # Add the grid container here
            yield Footer()

    def on_mount(self) -> None:
        """Populate the list view after mounting."""
        if self.tasks:  # Check if tasks are available
            for task in self.tasks:
                self.list_view.append(
                    ListItem(Label(str(task.id)), id=f"task_{task.id}")
                )
            self.current_task_id = self.tasks[0].id
            self.display_task(self.current_task_id)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Event handler for list view selection."""
        self.current_task_id = event.item.id.removeprefix("task_")
        task_id = event.item.id.removeprefix("task_")
        self.display_task(task_id)

    def display_task(self, task_id: str) -> None:
        """Display the selected task."""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            return

        # Clear previous grids
        #  for widget in list(self.grid_container.children):

        self.grid_container.remove_children()

        self.grid_container.styles.grid_size_rows = 2
        self.grid_container.styles.grid_size_columns = len(task.train)

        # Add train grids
        for i, task_pair in enumerate(task.train):
            input_grid = self.renderer(task_pair.input.grid)

            #  new_stopwatch.scroll_visible()
            self.grid_container.mount(input_grid)

        for i, task_pair in enumerate(task.train):
            output_grid = (
                self.renderer(task_pair.output.grid) if task_pair.output else Static("")
            )

            self.grid_container.mount(output_grid)

        # Add test grids, if they exist
        #  if task.test:
            #  j = 0  # counter for output grids
            #  for i, task_pair in enumerate(task.test):
                #  input_grid = self.renderer(task_pair.input.grid)
                #  self.grid_container.place(input_grid, area=f"test_input_{i}")

                #  if task_pair.output:
                    #  output_grid = self.renderer(task_pair.output.grid)
                    #  self.grid_container.place(output_grid, area=f"test_output_{j}")
                    #  j += 1

        self.grid_container.refresh()

    def action_set_renderer_solid(self) -> None:
        """Set the renderer to SolidGrid."""
        self.renderer = SolidGrid
        self.display_task(self.current_task_id)

    def action_set_renderer_char(self) -> None:
        """Set the renderer to CharGrid."""
        self.renderer = CharGrid
        self.display_task(self.current_task_id)

    def action_set_renderer_block(self) -> None:
        """Set the renderer to BlockGrid."""
        self.renderer = BlockGrid
        self.display_task(self.current_task_id)


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
