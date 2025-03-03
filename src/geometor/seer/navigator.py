import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches  # Import patches
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.widgets import Footer
from textual.containers import Horizontal, Vertical

# Removed pattern generation functions and PATTERNS

class GridApp(App):
    """Textual Application that displays buttons to select tasks and updates a Matplotlib plot."""
    CSS_PATH = None  # No external CSS, using default styling
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, tasks: list, **kwargs):
        """
        Initialize the app with a list of Task objects.
        :param tasks: List of Task objects.
        """
        super().__init__(**kwargs)
        self.tasks = tasks
        self.fig = None
        self.ax = None

    def compose(self) -> ComposeResult:
        """Create the UI layout with one button per task."""
        with Vertical():
            yield Static("Select a Task:", id="task_title")  # Add a title
            with Horizontal():
                for task in self.tasks:
                    # Create a Button for each task.
                    # The button's label is the task ID, and the id is the task ID.
                    yield Button(label=str(task.id), id=f"task_{task.id}")  # Prefix task ID
            yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted (initialized). Set up Matplotlib figure here."""
        # Initialize Matplotlib in interactive mode
        plt.ion()
        # Configure Matplotlib to not show the toolbar
        plt.rcParams['toolbar'] = 'None'
        # Create a Matplotlib figure and axes
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.manager.set_window_title("Task Viewer")
        self.fig.patch.set_facecolor('black')  # Set background to black

        # Optionally, display an initial task (e.g., the first task in the list)
        if self.tasks:
            self.display_task(self.tasks[0].id)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler for button presses. Updates the Matplotlib plot based on which button was clicked."""
        task_id = event.button.id
        self.display_task(task_id)

    def display_task(self, task_id: str) -> None:
        """Generate and display the task image corresponding to the given task ID on the Matplotlib plot."""
        # Find the task with the given ID
        #  task = next((t for t in self.tasks if t.id == task_id), None) # Original
        task = next((t for t in self.tasks if f"task_{t.id}" == task_id), None) # Modified for prefixed IDs
        if not task:
            return  # Unknown task, do nothing (or could log an error)

        # Generate the task image
        img = task.to_image()

        # Clear the previous image on the axes
        self.ax.clear()

        # Display the new image
        self.ax.imshow(img, interpolation='nearest')

        # Adjust axes for better appearance
        self.ax.set_title(task.id, color='white') # Set title color
        self.ax.set_facecolor('black') # Set background to black
        self.ax.axis('off')  # hide the axes ticks/grid for a cleaner look

        # Force a redraw of the figure canvas to show the updated image
        self.fig.canvas.draw_idle()
        plt.pause(0.1)  # Add a short pause to allow Matplotlib to process events

    def on_unmount(self) -> None:
        """Called when the app is unmounted. Close the Matplotlib plot."""
        if self.fig:
            plt.close(self.fig)
