from geometor.seer.navigator.renderers.base_grid import *
#  from geometor.seer.tasks.tasks import Task  # Import Task
from rich.text import Text
from textual.widgets import Static

class SolidGrid(BaseGrid):

    def render(self):
        from rich.text import Text
        text = Text()

        block = "██"
        for row in self.grid:
            line = Text()
            for cell_value in row:
                fill_color = self.get_color(cell_value)  # Use get_color
                line.append(block, style=fill_color) # Use rich_color

            line.append("\n")
            text.append(line)

        return text
