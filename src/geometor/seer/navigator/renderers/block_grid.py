from geometor.seer.navigator.renderers.base_grid import *
#  from geometor.seer.tasks.tasks import Task  
from rich.text import Text

class BlockGrid(BaseGrid):
    """
    first row cells are made of 3 characters - half vertical and full
    next row made of top and bottom half - 1 space, 1 half block
    " ██"
    " ▄▄"
    " ▀▀"
    """

    def render(self):

        text = Text()
        # For each row in the grid
        for row_num, row in enumerate(self.grid):
            if row_num % 2:
                for cell in row:
                    fill_color = self.get_color(cell) 
                    text.append(" ██", style=fill_color)
                text.append("\n")
            else:
                top_half = Text()
                bottom_half = Text()
                for cell in row:
                    fill_color = self.get_color(cell)  
                    top_half.append(" ▄▄", style=fill_color) 
                    bottom_half.append(" ▀▀", style=fill_color) 
                text.append(top_half)
                text.append("\n")
                text.append(bottom_half)
                text.append("\n")
        return text
