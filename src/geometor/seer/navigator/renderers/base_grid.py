from textual.widgets import Static
from textual.color import Color  # Import the Color class

# Import COLOR_MAP from the tasks.grid module
from geometor.seer.tasks.grid import COLOR_MAP


class BaseGrid(Static):
    """Base widget class for rendering the colored grid."""

    def __init__(self, grid, **kwargs):
        super().__init__(**kwargs)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_color(self, cell_value: int) -> Color:
        """Gets a Textual Color object for the given cell value."""
        rgb_tuple = COLOR_MAP.get(cell_value)
        if rgb_tuple:
            return Color(*rgb_tuple).hex6  # Create a Color object from the RGB tuple
        else:
            return Color(0, 0, 0).hex6  # Default to black if color not found

