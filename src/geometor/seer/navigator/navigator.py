"""
A Textual app that displays ARC-style colored grids with grid lines separating the cells.
It demonstrates several rendering methods (image-based, Unicode block, and half-block) with grid lines.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Button

from geometor.seer.navigator.base_grid import BaseGrid

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
    CSS = """
    Screen {
        align: center middle;
    }
    """
    def compose(self) -> ComposeResult:
        button_bar = Horizontal(
            Button("Split Grid", id="mode_split"),
            Button("Squares", id="mode_box"),  
            id="button_bar"
        )
        #  self.image_grid = ImageGrid(GRID_DATA, id="image_grid")
        self.split_grid = SplitBlockGrid(GRID_DATA, id="split_grid")
        self.box_grid = SquareCharGrid(GRID_DATA, id="box_grid")

        # Hide them by default (or show one by default)
        #  self.image_grid.styles.display = "none"
        self.split_grid.styles.display = "none"
        self.box_grid.styles.display = "none"

        yield button_bar
        yield self.split_grid
        yield self.box_grid

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Switch the active rendering mode based on button presses."""
        # Hide all modes
        self.split_grid.styles.display = "none"
        self.box_grid.styles.display = "none"

        # Show whichever was pressed
        if event.button.id == "mode_split":
            self.split_grid.styles.display = "block"
        elif event.button.id == "mode_box":
            self.box_grid.styles.display = "block"

        self.refresh()

if __name__ == "__main__":
    app = Navigator()
    app.run()
