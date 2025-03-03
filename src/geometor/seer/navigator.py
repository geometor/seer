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

    def __init__(self, tasks: list, cell_size: int = 32, line_width: int = 2, **kwargs):
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
        self.colors = [
            '#000000',  # 0: black
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
        x = col * (self.cell_size + self.line_width)
        y = row * (self.cell_size + self.line_width)
        return x, y

    def _draw_grid(self, task):
        """Draws the grid lines and cells on the axes."""
        self.ax.clear()
        self.ax.set_facecolor('black')
        self.ax.axis('off')

        # find max dimensions across train and test
        max_rows = 0
        max_cols = 0
        for task_set in [task.train, task.test]:
            for task_pair in task_set:
                max_rows = max(max_rows, task_pair.input.grid.shape[0])
                max_cols = max(max_cols, task_pair.input.grid.shape[1])
                if task_pair.output is not None:
                    max_rows = max(max_rows, task_pair.output.grid.shape[0])
                    max_cols = max(max_cols, task_pair.output.grid.shape[1])

        total_height_pixels = max_rows * (self.cell_size + self.line_width) - self.line_width
        total_width_pixels = max_cols * (self.cell_size + self.line_width) - self.line_width

        # Set the axis limits *in pixel coordinates*
        self.ax.set_xlim(0, total_width_pixels)
        self.ax.set_ylim(total_height_pixels, 0)  # Invert y-axis for correct display
        self.ax.set_aspect('equal')

        # Draw train pairs
        x_offset = 0
        for task_pair in task.train:
          x_offset = self._draw_task_pair(task_pair, x_offset) + 2 * self.cell_size # Add spacing

        # Draw test pairs
        x_offset += 3 * self.cell_size
        for task_pair in task.test:
          x_offset = self._draw_task_pair(task_pair, x_offset) + 2 * self.cell_size

        self.ax.set_title(task.id, color='white')
        self.fig.canvas.draw_idle()
        plt.pause(0.1)

    def _draw_task_pair(self, task_pair, x_offset):
        """Draws a single task pair (input and output grids)."""

        self._draw_single_grid(task_pair.input, x_offset)
        input_width_pixels = task_pair.input.grid.shape[1] * (self.cell_size + self.line_width) - self.line_width
        x_offset += input_width_pixels + 2 * self.cell_size  # Add space between input/output

        if task_pair.output is not None:
            self._draw_single_grid(task_pair.output, x_offset)
            output_width_pixels = task_pair.output.grid.shape[1] * (self.cell_size + self.line_width) - self.line_width
            x_offset += output_width_pixels
        return x_offset

    def _draw_single_grid(self, grid_obj, x_offset):
      """Draws a single grid (either input or output)."""
      grid = grid_obj.grid
      rows, cols = grid.shape
      for row in range(rows):
          for col in range(cols):
              x, y = self._data_to_pixel(row, col, rows, cols)
              x += x_offset  # Apply the x_offset
              color = self.colors[grid[row, col]]
              rect = Rectangle(
                  (x, y), self.cell_size, self.cell_size,
                  facecolor=color, edgecolor='none'
              )
              self.ax.add_patch(rect)

      # Draw grid lines
      for row in range(rows + 1):
          y = row * (self.cell_size + self.line_width) - self.line_width / 2
          y += 0  # No y_offset needed as we are drawing full lines
          x_start = x_offset - self.line_width / 2
          x_end = x_offset + cols * (self.cell_size + self.line_width) - self.line_width / 2
          self.ax.plot([x_start, x_end], [y, y], color='white', linewidth=self.line_width)
      for col in range(cols + 1):
          x = col * (self.cell_size + self.line_width) - self.line_width / 2
          x += x_offset
          y_start = - self.line_width / 2
          y_end = rows * (self.cell_size + self.line_width) - self.line_width / 2
          self.ax.plot([x, x], [y_start, y_end], color='white', linewidth=self.line_width)


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
