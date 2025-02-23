"""
1.  Identify all non-zero colored cells in the input grid.
2.  Locate the maroon(9) cell. Move cell to the bottom row of it's original column.
3.  All other cells are unchanged, including all white(0) cells and non-zero cells.
"""

import numpy as np

def find_colored_cell(grid, color):
    # Find the coordinates of a cell with the specified color.
    coords = np.argwhere(grid == color)
    if coords.size > 0:
        return coords[0]
    else:
        return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find the maroon (9) cell.
    maroon_cell = find_colored_cell(input_grid, 9)

    # If a maroon cell exists, move it to the bottom row of its column.
    if maroon_cell is not None:
        maroon_row, maroon_col = maroon_cell
        output_grid[maroon_row, maroon_col] = 0  # Clear the original position
        output_grid[rows - 1, maroon_col] = 9     # Move to the bottom row

    return output_grid