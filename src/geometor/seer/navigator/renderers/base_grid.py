#  from textual.app import App, ComposeResult
#  from textual.containers import Horizontal
from textual.widgets import Static

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
    7: "#DC143C",
    8: "#ff8800",  # orange
    9: "#00ffff",  # cyan variant
}

class BaseGrid(Static):
    """Base widget class for rendering the colored grid."""

    def __init__(self, grid, **kwargs):
        super().__init__(**kwargs)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

