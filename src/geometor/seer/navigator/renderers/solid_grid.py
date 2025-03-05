from geometor.seer.navigator.renderers.base_grid import *
#  from geometor.seer.tasks.tasks import Task  # Import Task
from rich.text import Text

class SolidGrid(BaseGrid):

    def render(self):
        from rich.text import Text
        text = Text()

        block = "██"
        for row in self.grid:
            line = Text()
            for cell_value in row:
                fill_color = COLOR_PALETTE.get(cell_value, "black")
                line.append(block, style=fill_color)

            line.append("\n")
            text.append(line)

        return text


