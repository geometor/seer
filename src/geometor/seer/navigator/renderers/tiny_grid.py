from textual.color import Color
from rich.text import Text
from .base_grid import BaseGrid

class TinyGrid(BaseGrid):
    """
    Renders the grid using the Unicode upper half block character '▀'.
    Each character represents two rows:
    - Foreground color = top row cell color
    - Background color = bottom row cell color
    If there's an odd number of rows, the last row uses black for the background.
    """

    HALF_BLOCK_CHAR = "▀"  # U+2580

    def render(self) -> Text:
        text = Text()
        default_bg_color = Color(0, 0, 0).hex6  # Black for odd rows

        # Iterate over rows in steps of 2
        for r in range(0, self.rows, 2):
            line = Text()
            row1 = self.grid[r]
            # Check if there is a second row in the pair
            row2_exists = (r + 1) < self.rows
            row2 = self.grid[r + 1] if row2_exists else None

            for c in range(self.cols):
                fg_color = self.get_color(row1[c])
                # Use row2 color if it exists, otherwise default black
                bg_color = self.get_color(row2[c]) if row2_exists else default_bg_color

                # Create style string for Rich Text
                style = f"{fg_color} on {bg_color}"
                line.append(self.HALF_BLOCK_CHAR, style=style)

            line.append("\n")
            text.append(line)

        return text
