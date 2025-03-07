from geometor.seer.navigator.renderers.base_grid import *
#  from geometor.seer.tasks.tasks import Task  # Import Task
from rich.text import Text

class CharGrid(BaseGrid):
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
                fill_color = self.get_color(cell_value)  # Use get_color
                # Append the square character with the fill color
                line.append(self.SQUARE_CHAR, style=fill_color) 
            # Add a newline after finishing a row
            line.append("\n")
            text.append(line)
        return text
