import numpy as np
import matplotlib.pyplot as plt
from textual.app import App, ComposeResult
from textual.widgets import Button, Static, ListView, ListItem, Label
from textual.widgets import Footer
from textual.containers import Vertical
from matplotlib.patches import Rectangle

class GridApp(App):
    """Textual Application that displays buttons to select tasks and updates a Matplotlib plot."""
    CSS_PATH = None  # No external CSS, using default styling
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, tasks: list, cell_size: int = 32, line_width: int = 1, **kwargs):
        """
        Initialize the app.
        :param tasks: List of Task objects.
        :param cell_size: Size of each cell in pixels.
        :param line_width: Width of the grid lines in pixels.
        """
        super().__init__(**kwargs)
        self.tasks = tasks
        self.fig = None
        self.ax = None
        self.cell_size = cell_size
        self.line_width = line_width
        self.map_colors = [
            '#FFFFFF',  # 0: white
            '#0074D9',  # 1: blue
            '#FF4136',  # 2: red
            '#2ECC40',  # 3: green
            '#FFDC00',  # 4: yellow
            '#AAAAAA',  # 5: gray
            '#F012BE',  # 6: magenta
            '#FF851B',  # 7: orange
            '#7FDBFF',  # 8: cyan
            '#870C25',  # 9: brown
        ]

    def compose(self) -> ComposeResult:
        """Create the UI layout with one button per task."""
        with Vertical():
            yield Static("Select a Task:", id="task_title")  # Add a title
            list_view = ListView()
            yield list_view  # Yield the ListView *before* adding items

            # Add the ListItems to the ListView after it has been mounted
            for task in self.tasks:
                list_view.compose_add_child(ListItem(Label(str(task.id)), id=f"task_{task.id}"))

            yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted (initialized). Set up Matplotlib figure here."""
        plt.ion()
        plt.rcParams['toolbar'] = 'None'
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.manager.set_window_title("Task Viewer")
        self.fig.patch.set_facecolor('black')

        if self.tasks:
            self.display_task(self.tasks[0].id)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Event handler for list view selection."""
        task_id = event.item.id
        self.display_task(task_id)

    def _data_to_pixel(self, row, col, grid_height, grid_width):
        """Converts data coordinates (row, col) to pixel coordinates."""
        x = col * (self.cell_size)
        y = row * (self.cell_size)
        return x, y

    def _draw_grid(self, task):
        """Draws the grid lines and cells on the axes."""
        self.ax.clear()
        self.ax.set_facecolor('black')
        self.ax.axis('off')

        # --- Calculate maximum dimensions for TRAIN set (stacked pairs) ---
        max_train_width = 0  # Maximum width of a *single* stacked pair
        max_train_height = 0 # Maximum height of a *single* stacked pair
        for task_pair in task.train:
            input_height = task_pair.input.grid.shape[0]
            input_width = task_pair.input.grid.shape[1]
            output_height = task_pair.output.grid.shape[0] if task_pair.output else 0
            output_width = task_pair.output.grid.shape[1] if task_pair.output else 0

            max_train_width = max(max_train_width, max(input_width, output_width))  # Find widest pair
            max_train_height = max(max_train_height, input_height + output_height) # Find tallest pair

        # total_train_width_pixels: max width of a pair * number of pairs
        total_train_width_pixels = max_train_width * self.cell_size * len(task.train)
        # total_train_height_pixels: max height of a stacked pair
        total_train_height_pixels = max_train_height * self.cell_size

        # --- Calculate maximum dimensions for TEST set (separate rows) ---
        max_rows_input = 0
        max_cols_input = 0
        for task_pair in task.test:
            max_rows_input = max(max_rows_input, task_pair.input.grid.shape[0])
            max_cols_input = max(max_cols_input, task_pair.input.grid.shape[1])

        max_rows_output = 0
        max_cols_output = 0
        for task_pair in task.test:
            if task_pair.output is not None:
                max_rows_output = max(max_rows_output, task_pair.output.grid.shape[0])
                max_cols_output = max(max_cols_output, task_pair.output.grid.shape[1])

        total_test_input_height_pixels = max_rows_input * (self.cell_size)
        total_test_input_width_pixels = max_cols_input * (self.cell_size)
        total_test_output_height_pixels = max_rows_output * (self.cell_size)
        total_test_output_width_pixels = max_cols_output * (self.cell_size)

        # --- Calculate total dimensions and set axis limits ---
        # Total width:  the wider of (all train pairs) and (test inputs + test outputs)
        total_width_pixels = max(total_train_width_pixels, total_test_input_width_pixels, total_test_output_width_pixels)
        # Total height: train height + test input height + test output height + spacing
        total_height_pixels = total_train_height_pixels + total_test_input_height_pixels + total_test_output_height_pixels + 4 * self.cell_size

        self.ax.set_xlim(0, total_width_pixels)
        self.ax.set_ylim(total_height_pixels, 0)
        self.ax.set_aspect('equal')

        # --- Draw train pairs (stacked) ---
        y_offset = 0
        x_offset = 0
        x_offset = self._draw_train_pairs(task, x_offset, y_offset)

        # --- Draw test inputs ---
        y_offset += total_train_height_pixels + 3 * self.cell_size  # Add space after train set
        x_offset = 0
        x_offset = self._draw_single_grid_row(task.test, "input", x_offset, y_offset)

        # --- Draw test outputs ---
        y_offset += total_test_input_height_pixels + 2 * self.cell_size
        x_offset = 0
        x_offset = self._draw_single_grid_row(task.test, "output", x_offset, y_offset)

        self.ax.set_title(task.id, color='white')
        self.fig.canvas.draw_idle()
        plt.pause(0.1)

    def _draw_train_pairs(self, task, x_offset, y_offset):
        """Draws training input/output pairs, stacked vertically."""
        initial_x_offset = x_offset
        for task_pair in task.train:
            # Draw input grid
            self._draw_single_grid(task_pair.input, x_offset, y_offset)
            input_height_pixels = task_pair.input.grid.shape[0] * (self.cell_size)
            input_width_pixels = task_pair.input.grid.shape[1] * (self.cell_size)

            # Calculate y_offset for output grid (below input)
            output_y_offset = y_offset + input_height_pixels + 2 * self.cell_size

            # Draw output grid
            if task_pair.output:
                self._draw_single_grid(task_pair.output, x_offset, output_y_offset)
                output_width_pixels = task_pair.output.grid.shape[1] * (self.cell_size)
            else:
                output_width_pixels = 0

            # Update x_offset for next pair
            x_offset += max(input_width_pixels, output_width_pixels) + 2 * self.cell_size

        return max(initial_x_offset, x_offset)

    def _draw_single_grid_row(self, task_set, io_type, x_offset, y_offset):
        """Draws a row of grids (either all inputs or all outputs)."""
        initial_x_offset = x_offset
        for task_pair in task_set:
            grid_obj = task_pair.input if io_type == "input" else task_pair.output
            if grid_obj is not None:  # Check for None, as test set may not have outputs
                self._draw_single_grid(grid_obj, x_offset, y_offset)
                grid_width_pixels = grid_obj.grid.shape[1] * (self.cell_size)
                x_offset += grid_width_pixels + 2 * self.cell_size  # Add space between grids

        return max(x_offset, initial_x_offset) # in case this row is empty, return the initial offset

    def _draw_single_grid(self, grid_obj, x_offset, y_offset):
        """Draws a single grid (either input or output)."""
        grid = grid_obj.grid
        rows, cols = grid.shape
        for row in range(rows):
            for col in range(cols):
                x, y = self._data_to_pixel(row, col, rows, cols)
                x += x_offset  # Apply the x_offset
                y += y_offset
                color = self.map_colors[grid[row, col]]
                rect = Rectangle(
                    (x, y), self.cell_size, self.cell_size,
                    facecolor=color, edgecolor='black', lw=1
                )
                self.ax.add_patch(rect)


    def display_task(self, task_id: str) -> None:
        """Generate and display the task image."""
        task = next((t for t in self.tasks if f"task_{t.id}" == task_id), None)
        if not task:
            return

        self._draw_grid(task)

    def on_unmount(self) -> None:
        """Called when the app is unmounted. Close the Matplotlib plot."""
        if self.fig:
            plt.close(self.fig)


def main():
    """
    Loads tasks from the specified directory and runs the GridApp to display them.
    """
    from pathlib import Path
    from geometor.seer.tasks.tasks import Tasks
    from geometor.seer.navigator import GridApp

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

    # 2. Create and run the GridApp
    app = GridApp(tasks[:5])
    app.run()

if __name__ == "__main__":
    main()
