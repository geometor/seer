"""
Filename: textual_arc_grid_with_lines.py
Description: A Textual app that displays ARC-style colored grids with grid lines separating the cells.
It demonstrates several rendering methods (image-based, Unicode block, and half-block) with grid lines.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Button

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


class BaseGrid(Static):
    """Base widget class for rendering the colored grid."""

    def __init__(self, grid, **kwargs):
        super().__init__(**kwargs)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0


class ImageGrid(BaseGrid):
    """
    Grid rendered using an image-based approach via rich-pixels.
    This mode creates a PIL image with grid lines separating the cells.
    """

    def on_mount(self):
        try:
            from PIL import Image
            from rich_pixels import Pixels
        except ImportError:
            self.update(
                "Image rendering requires 'Pillow' and 'rich-pixels' libraries."
            )
            return

        # Determine cell pixel size (without grid lines)
        cell_pixel_size = 100
        lw = GRID_LINE_WIDTH
        # Compute total image size including grid lines between cells and around edges.
        img_width = self.cols * cell_pixel_size + (self.cols + 1) * lw
        img_height = self.rows * cell_pixel_size + (self.rows + 1) * lw

        # Create a new image and fill it with the grid line color.
        image = Image.new("RGB", (img_width, img_height), GRID_LINE_COLOR)
        # Fill each cell: calculate its top-left offset including the grid line offset.
        for r in range(self.rows):
            for c in range(self.cols):
                color = COLOR_PALETTE.get(self.grid[r][c], "black")
                # Convert color to an RGB tuple.
                rgb_color = Image.new("RGB", (1, 1), color).getpixel((0, 0))
                x0 = lw + c * (cell_pixel_size + lw)
                y0 = lw + r * (cell_pixel_size + lw)
                for y in range(y0, y0 + cell_pixel_size):
                    for x in range(x0, x0 + cell_pixel_size):
                        image.putpixel((x, y), rgb_color)
        pixels = Pixels.from_image(image)
        self.update(pixels)

    def on_resize(self, event):
        """Regenerate the image on resize so that cell sizes scale with available space."""
        try:
            from PIL import Image
            from rich_pixels import Pixels
        except ImportError:
            return

        if self.cols == 0 or self.rows == 0:
            return

        lw = GRID_LINE_WIDTH
        new_width, new_height = event.size  # in terminal cells (approximation)
        # Determine available cell size (simple heuristic)
        factor_x = max(1, new_width // (self.cols + self.cols + 1))
        factor_y = max(1, new_height // (self.rows + self.rows + 1))
        cell_pixel_size = (
            min(factor_x, factor_y) * 2
        )  # scale factor; adjust multiplier for detail

        img_width = self.cols * cell_pixel_size + (self.cols + 1) * lw
        img_height = self.rows * cell_pixel_size + (self.rows + 1) * lw

        image = Image.new("RGB", (img_width, img_height), GRID_LINE_COLOR)
        for r in range(self.rows):
            for c in range(self.cols):
                color = COLOR_PALETTE.get(self.grid[r][c], "black")
                rgb_color = Image.new("RGB", (1, 1), color).getpixel((0, 0))
                x0 = lw + c * (cell_pixel_size + lw)
                y0 = lw + r * (cell_pixel_size + lw)
                for y in range(y0, y0 + cell_pixel_size):
                    for x in range(x0, x0 + cell_pixel_size):
                        image.putpixel((x, y), rgb_color)
        pixels = Pixels.from_image(image)
        self.update(pixels)


class UnicodeBlockGrid(BaseGrid):
    """
    Grid rendered using colored Unicode blocks.
    This version inserts extra spaces with background styling to simulate grid lines.
    """

    def render(self):
        from rich.text import Text

        text = Text()
        cell_width = 2  # characters per cell (adjust for squareness)
        lw = GRID_LINE_WIDTH

        # Helper function to create a horizontal grid line.
        def horizontal_line():
            line = Text()
            # For each column, add a vertical grid separator and cell space.
            for col in range(self.cols + 1):
                line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                if col < self.cols:
                    line.append(" " * cell_width, style=f"on {GRID_LINE_COLOR}")
            return line

        # Append top horizontal grid line.
        text.append(horizontal_line())
        text.append("\n")

        # Build each grid row.
        for row in self.grid:
            cell_line = Text()
            for value in row:
                # Vertical separator before the cell.
                cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                cell_line.append(
                    " " * cell_width, style=f"on {COLOR_PALETTE.get(value, 'black')}"
                )
            # Final vertical separator.
            cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
            text.append(cell_line)
            text.append("\n")
            # Append horizontal grid line after the row.
            text.append(horizontal_line())
            text.append("\n")
        return text


class SplitBlockGrid(BaseGrid):
    """
    New Unicode rendering mode.

    For each grid cell, render:
      • A full block ("█") with the cell's fill color.
      • A vertical split block ("▌") styled with foreground = fill color and background = grid line color.

    This results in two characters per cell that show the cell color and a vertical separator.
    """

    def render(self):
        from rich.text import Text

        text = Text()
        # For each row in the grid
        for row in self.grid:
            # For each cell, output two characters
            for cell in row:
                fill_color = COLOR_PALETTE.get(cell, "black")
                # First character: full block in fill color.
                text.append("█", style=fill_color)
                # Second character: left half block, so its left half is fg and right half is bg.
                text.append("▌", style=f"{fill_color} on {GRID_LINE_COLOR}")
            text.append("\n")
        return text


class BoxDrawingGrid(BaseGrid):
    """
    A grid rendered with box-drawing characters to show horizontal and vertical lines clearly.
    Each cell is rendered as a box of text with a colored background.
    """

    def render(self):
        from rich.text import Text

        text = Text()

        # Number of text characters for each cell's width/height.
        cell_width = 3
        cell_height = 2

        # Define a few helper functions to build the horizontal lines (top, middle, bottom).

        def top_line():
            # Example for cols=3: "┌───┬───┬───┐"
            line = "┌"
            for col in range(self.cols - 1):
                line += "─" * cell_width + "┬"
            line += "─" * cell_width + "┐"
            return line

        def mid_line():
            # Example: "├───┼───┼───┤"
            line = "├"
            for col in range(self.cols - 1):
                line += "─" * cell_width + "┼"
            line += "─" * cell_width + "┤"
            return line

        def bot_line():
            # Example: "└───┴───┴───┘"
            line = "└"
            for col in range(self.cols - 1):
                line += "─" * cell_width + "┴"
            line += "─" * cell_width + "┘"
            return line

        # Build the top border line.
        text.append(top_line(), style=GRID_LINE_COLOR)
        text.append("\n")

        # Render each row of cells.
        for row_index in range(self.rows):
            # Each row of cells has 'cell_height' lines of text for the interior.
            for _ in range(cell_height):
                row_text = Text()
                # Start with left border.
                row_text.append("│", style=GRID_LINE_COLOR)

                # For each column/cell in this row:
                for col_index in range(self.cols):
                    fill_color = COLOR_PALETTE.get(
                        self.grid[row_index][col_index], "black"
                    )
                    # Append 'cell_width' spaces styled with the cell's fill color.
                    row_text.append(" " * cell_width, style=f"on {fill_color}")
                    # Append the right vertical line.
                    row_text.append("│", style=GRID_LINE_COLOR)

                # Add this row of text (one interior line of the box) plus a newline.
                text.append(row_text)
                text.append("\n")

            # After finishing the interior of row_index:
            # If it's not the last row, print the 'middle' line; otherwise, the bottom line.
            if row_index < self.rows - 1:
                text.append(mid_line(), style=GRID_LINE_COLOR)
            else:
                text.append(bot_line(), style=GRID_LINE_COLOR)
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


class HalfBlockGrid(BaseGrid):
    """
    Grid rendered using half-block characters (▀) to combine two rows.
    This version also adds grid lines.
    """

    def render(self):
        from rich.text import Text

        text = Text()
        cell_width = 2  # number of characters for each cell horizontally
        lw = GRID_LINE_WIDTH

        # Helper for horizontal grid line.
        def horizontal_line():
            line = Text()
            for col in range(self.cols + 1):
                line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                if col < self.cols:
                    line.append(" " * cell_width, style=f"on {GRID_LINE_COLOR}")
            return line

        text.append(horizontal_line())
        text.append("\n")

        r = 0
        while r < self.rows:
            if r < self.rows - 1:
                top_row = self.grid[r]
                bottom_row = self.grid[r + 1]
                cell_line = Text()
                for c in range(self.cols):
                    cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                    cell_line.append(
                        "▀" * cell_width,
                        style=f"{COLOR_PALETTE.get(top_row[c], 'black')} on {COLOR_PALETTE.get(bottom_row[c], 'black')}",
                    )
                cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                text.append(cell_line)
                text.append("\n")
                r += 2
            else:
                # For an odd number of rows, render the last row with full blocks.
                last_row = self.grid[r]
                cell_line = Text()
                for c in range(self.cols):
                    cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                    cell_line.append(
                        "▀" * cell_width,
                        style=f"{COLOR_PALETTE.get(last_row[c], 'black')} on {COLOR_PALETTE.get(last_row[c], 'black')}",
                    )
                cell_line.append(" " * lw, style=f"on {GRID_LINE_COLOR}")
                text.append(cell_line)
                text.append("\n")
                r += 1
            text.append(horizontal_line())
            text.append("\n")
        return text


class ARCGridApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    """
    def compose(self) -> ComposeResult:
        button_bar = Horizontal(
            Button("Image", id="mode_image"),
            Button("Unicode", id="mode_unicode"),
            Button("Split Grid", id="mode_split"),
            Button("Squares", id="mode_box"),  
            id="button_bar"
        )
        self.image_grid = ImageGrid(GRID_DATA, id="image_grid")
        self.unicode_grid = UnicodeBlockGrid(GRID_DATA, id="unicode_grid")
        self.split_grid = SplitBlockGrid(GRID_DATA, id="split_grid")

        # Instantiate our new BoxDrawingGrid
        self.box_grid = SquareCharGrid(GRID_DATA, id="box_grid")

        # Hide them by default (or show one by default)
        self.image_grid.styles.display = "none"
        self.unicode_grid.styles.display = "none"
        self.split_grid.styles.display = "none"
        self.box_grid.styles.display = "none"

        yield button_bar
        yield self.image_grid
        yield self.unicode_grid
        yield self.split_grid
        yield self.box_grid

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Switch the active rendering mode based on button presses."""
        # Hide all modes
        self.image_grid.styles.display = "none"
        self.unicode_grid.styles.display = "none"
        self.split_grid.styles.display = "none"
        self.box_grid.styles.display = "none"

        # Show whichever was pressed
        if event.button.id == "mode_image":
            self.image_grid.styles.display = "block"
        elif event.button.id == "mode_unicode":
            self.unicode_grid.styles.display = "block"
        elif event.button.id == "mode_split":
            self.split_grid.styles.display = "block"
        elif event.button.id == "mode_box":
            self.box_grid.styles.display = "block"

        self.refresh()

if __name__ == "__main__":
    app = ARCGridApp()
    app.run()
