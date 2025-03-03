import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches  # Import patches
from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widgets import Footer
from textual.containers import Horizontal

# Define grid pattern generation functions
def make_checkerboard(size=8):
    """Generate an NxN checkerboard pattern with two colors (blue and yellow)."""
    grid = np.zeros((size, size, 3), dtype=float)
    # Define two colors
    color1 = np.array([0.0, 0.0, 1.0])  # blue
    color2 = np.array([1.0, 1.0, 0.0])  # yellow
    for i in range(size):
        for j in range(size):
            # Alternate colors based on parity of (i+j)
            grid[i, j] = color1 if ((i + j) % 2 == 0) else color2
    return grid

def make_gradient(size=8):
    """Generate an NxN gradient pattern (color varies smoothly from one corner to another)."""
    grid = np.zeros((size, size, 3), dtype=float)
    for i in range(size):
        for j in range(size):
            # Color components vary with position:
            # R increases from left (0) to right (1),
            # G is fixed at 0.5 for a moderate green tint,
            # B increases from top (0) to bottom (1).
            r = j / (size - 1)
            g = 0.5
            b = i / (size - 1)
            grid[i, j] = [r, g, b]
    return grid

def make_random(size=8):
    """Generate an NxN grid of random colors."""
    # Each cell gets a random RGB color
    return np.random.rand(size, size, 3)

# Map pattern identifiers to their generator functions and friendly names
PATTERNS = {
    "checkerboard": (make_checkerboard, "Checkerboard Pattern"),
    "gradient":     (make_gradient,     "Gradient Pattern"),
    "random":       (make_random,       "Random Pattern")
}

class GridApp(App):
    """Textual Application that displays buttons to select grid patterns and updates a Matplotlib plot."""
    CSS_PATH = None  # No external CSS, using default styling
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, patterns: dict[str, tuple], **kwargs):
        """
        Initialize the app with a given patterns dictionary.
        :param patterns: Dictionary mapping pattern keys to (function, name).
        """
        super().__init__(**kwargs)
        self.patterns = patterns
        self.fig = None
        self.ax = None

    def compose(self) -> ComposeResult:
        """Create the UI layout with one button per grid pattern."""
        with Horizontal():
            for key, (_, name) in self.patterns.items():
                # Create a Button for each pattern.
                # The button's label is the pattern name, and the id is the pattern key.
                yield Button(label=name, id=key)
        yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted (initialized). Set up Matplotlib figure here."""
        # Initialize Matplotlib in interactive mode so updates don't block the app
        plt.ion()
        # Configure Matplotlib to not show the toolbar
        plt.rcParams['toolbar'] = 'None'
        # Create a Matplotlib figure and axes
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.manager.set_window_title("Grid Pattern Viewer")
        self.fig.patch.set_facecolor('black')  # Set background to black

        # Optionally, display an initial pattern (e.g., the first pattern in the list)
        first_pattern_key = next(iter(self.patterns))
        self.display_pattern(first_pattern_key)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler for button presses. Updates the Matplotlib plot based on which button was clicked."""
        pattern_key = event.button.id  # e.g., "checkerboard", "gradient", or "random"
        self.display_pattern(pattern_key)

    def display_pattern(self, pattern_key: str) -> None:
        """Generate and display the grid pattern corresponding to the given key on the Matplotlib plot."""
        # Safety check: ensure the pattern_key exists
        if pattern_key not in self.patterns:
            return  # Unknown pattern, do nothing (or could log an error)
        pattern_func, pattern_name = self.patterns[pattern_key]
        # Generate the pattern data (an NxN RGB grid)
        data = pattern_func()  # call the function to get the pattern array
        size = data.shape[0]
        # Clear the previous image on the axes
        self.ax.clear()
        # Display the new grid pattern
        self.ax.imshow(data, interpolation='nearest', extent=[0, size, size, 0])

        # Add black grid lines using Rectangle patches
        for i in range(size + 1):
            # Horizontal lines
            self.ax.add_patch(patches.Rectangle((0, i), size, 0.05, facecolor='black'))
            # Vertical lines
            self.ax.add_patch(patches.Rectangle((i, 0), 0.05, size, facecolor='black'))

        # Adjust axes for better appearance
        self.ax.set_title(pattern_name, color='white') # Set title color
        self.ax.set_facecolor('black') # Set background to black
        self.ax.axis('off')  # hide the axes ticks/grid for a cleaner look
        self.ax.set_xlim(0, size)
        self.ax.set_ylim(size, 0)
        # Force a redraw of the figure canvas to show the updated image
        self.fig.canvas.draw_idle()
        plt.pause(0.1)  # Add a short pause to allow Matplotlib to process events

    def on_unmount(self) -> None:
        """Called when the app is unmounted. Close the Matplotlib plot."""
        if self.fig:
            plt.close(self.fig)

if __name__ == "__main__":
    # Run the Textual application
    app = GridApp(PATTERNS)
    app.run()
