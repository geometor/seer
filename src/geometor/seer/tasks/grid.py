import numpy as np
#  from geometor.model import Model

from PIL import Image, ImageDraw, ImageFont

COLOR_MAP = {
    0: (238, 238, 238),  # White
    1: (30, 147, 255),  # Blue
    2: (220, 50, 40),  # Red
    3: (79, 204, 48),  # Green
    4: (230, 200, 0),  # Yellow
    5: (85, 85, 85),  # Gray
    6: (229, 58, 163),  # Magenta
    7: (230, 120, 20),  # Orange
    8: (135, 216, 241),  # Azure
    9: (146, 18, 49),  # Maroon
}


class Grid:
    def __init__(self, grid, puzzle_id, set_type, index, io_type):
        self.grid = np.array(grid, dtype=int)
        self.puzzle_id = puzzle_id
        self.set_type = set_type  # 'train' or 'test'
        self.index = index
        self.io_type = io_type  # 'input' or 'output'
        self._model = None

    @property
    def name(self):
        return f"{self.puzzle_id}-{self.set_type}-{self.index}-{self.io_type}"

    @property
    def height(self):
        return self.grid.shape[0]

    @property
    def width(self):
        return self.grid.shape[1]

    @property
    def size(self):
        return self.grid.size

    @property
    def colors(self):
        return set(np.unique(self.grid))

    @property
    def color_counts(self):
        unique, counts = np.unique(self.grid, return_counts=True)
        return dict(zip(unique, counts))

    #  @property
    #  def model(self):
        #  if self._model is None:
            #  self._model = self._create_model()
        #  return self._model

    #  def _create_model(self):
        #  model = Model(self.name)
        #  for y in range(self.height):
            #  for x in range(self.width):
                #  val = self.grid[y, x]
                #  model.set_point(x, y, classes=[str(val)], label=f"({x},{y})")
        #  return model

    def rotate(self, k=1):
        """
        Rotate the grid by 90 degrees k times.
        Positive k means clockwise rotation, negative k means counter-clockwise.

        returns copy of Grid
        """
        new_grid = np.rot90(self.grid, k=-k)
        return Grid(
            new_grid,
            self.puzzle_id,
            self.set_type,
            self.index,
            f"{self.io_type}_rotated{k*90}",
        )

    def flip(self, axis=0):
        """
        Flip the grid along the specified axis.
        axis=0 flips vertically, axis=1 flips horizontally.

        returns copy of Grid
        """
        new_grid = np.flip(self.grid, axis=axis)
        flip_type = "vertical" if axis == 0 else "horizontal"
        return Grid(
            new_grid,
            self.puzzle_id,
            self.set_type,
            self.index,
            f"{self.io_type}_flipped_{flip_type}",
        )

    def set_pixel(self, row: int, column: int, color: int) -> str:
        """Set grid value at a specific coordinate."""

        height, width = self.grid.shape
        row, column, color = int(row), int(column), int(color)

        if not (0 <= row < height):
            return False, f"Row {row} is out of bounds. Grid height is {height}"
        if not (0 <= column < width):
            return False, f"Column {column} is out of bounds. Grid width is {width}"

        self.grid[row, column] = color

        return True, f"set_pixel({row=}, {column=}, {color=})"

    def set_range(
        self, row1: int, column1: int, row2: int, column2: int, color: int
    ) -> str:
        """Set grid values for a range of pixels."""

        # Convert to int and ensure proper order
        r1, r2 = sorted([int(row1), int(row2)])
        c1, c2 = sorted([int(column1), int(column2)])
        color = int(color)

        # Add 1 to end indices to make them inclusive
        r2 += 1
        c2 += 1

        # Validate bounds
        height, width = self.grid.shape
        if (r1 >= height and r2 >= height) or (c1 >= width and c2 >= width):
            return False, f"Entire range is outside grid bounds ({height}x{width})"

        r1 = max(0, min(r1, height))
        r2 = max(0, min(r2, height))
        c1 = max(0, min(c1, width))
        c2 = max(0, min(c2, width))

        # Set the range
        for row in range(r1, r2):
            for col in range(c1, c2):
                self.grid[row, col] = color

        cells_modified = (r2 - r1) * (c2 - c1)

        return True, f"set_range({row1=}, {column1=}, {row2=}, {column2=}, {color=})\n {cells_modified} pixels modified"



    def set_floodfill(self, row: int, column: int, color: int) -> str:
        """
        Flood-fill algorithm to set all contiguous cells connected to (row, column)
        with the same initial color to the new color.
        """
        height, width = self.grid.shape
        row, column, color = int(row), int(column), int(color)

        if not (0 <= row < height):
            return False, f"Row {row} is out of bounds. Grid height is {height}"
        if not (0 <= column < width):
            return False, f"Column {column} is out of bounds. Grid width is {width}"

        # Get the initial color at the starting cell
        initial_color = self.grid[row, column]

        # If the initial color is the same as the new color, no need to proceed
        if initial_color == color:
            return False, "No change needed as the target color is the same as the initial color"

        # Stack for DFS
        stack = [(row, column)]
        cells_modified = 0

        # Perform flood-fill using DFS
        while stack:
            current_row, current_col = stack.pop()

            # Check if the current cell is within bounds and matches the initial color
            if (
                0 <= current_row < height
                and 0 <= current_col < width
                and self.grid[current_row, current_col] == initial_color
            ):
                # Set the cell to the new color
                self.grid[current_row, current_col] = color
                cells_modified += 1

                # Add neighboring cells to the stack (up, down, left, right)
                stack.append((current_row + 1, current_col))
                stack.append((current_row - 1, current_col))
                stack.append((current_row, current_col + 1))
                stack.append((current_row, current_col - 1))

        return True, f"set_floodfill({row=}, {column=}, {color=})\n {cells_modified} pixels modified"


    def to_string(self, row_delimiter="\n", cell_delimiter=" "):
        return row_delimiter.join(
            cell_delimiter.join(str(cell) for cell in row) for row in self.grid
        )

    def to_image(grid, cell_size=64, add_text=True):
        border = 2
        color_size = cell_size - 2 * border
        width = grid.width * cell_size
        height = grid.height * cell_size

        image = Image.new("RGB", (width, height), color="black")
        draw = ImageDraw.Draw(image)

        try:
            font_size = max(cell_size // 2, 8)  # Adjust font size based on cell size
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        for y in range(grid.height):
            for x in range(grid.width):
                color = COLOR_MAP.get(grid.grid[y, x], (0, 0, 0))
                draw.rectangle(
                    [
                        x * cell_size + border,
                        y * cell_size + border,
                        (x + 1) * cell_size - border,
                        (y + 1) * cell_size - border,
                    ],
                    fill=color,
                )

                if add_text:
                    value = str(grid.grid[y, x])
                    text_bbox = draw.textbbox((0, 0), value, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]

                    text_x = x * cell_size + (cell_size - text_width) // 2
                    text_y = y * cell_size + (cell_size - text_height) // 2

                    draw.text((text_x + 1, text_y - 1), value, fill="black", font=font)

        return image

    def to_python_string(self, indent_level=1):
        """
        Returns a string representation of the grid as a Python list of lists.
        """
        indent = "    " * indent_level
        return "[\n" + ",\n".join([indent + str(list(row)) for row in self.grid]) + "\n]"
