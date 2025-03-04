from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Button

class BaseGrid(Static):
    """Base widget class for rendering the colored grid."""

    def __init__(self, grid, **kwargs):
        super().__init__(**kwargs)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

