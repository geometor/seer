"""
This script transforms an input grid based on the following rules:
1. Identifies the positions of single red (2) and blue (1) cells.
2. Constructs a plus-shaped pattern around the red cell using yellow (4) cells.
3. Constructs a plus-shaped pattern around the blue cell using orange (7) cells.
The positions of the original red and blue cells remain unchanged.
"""

import numpy as np

def find_cell(grid, color):
    """Finds the coordinates of the first occurrence of a single cell of the specified color."""
    coords = np.argwhere(grid == color)
    if len(coords) > 0:
        return tuple(coords[0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the red and blue cells
    red_pos = find_cell(input_grid, 2)
    blue_pos = find_cell(input_grid, 1)

    # Construct plus pattern around the red cell
    if red_pos:
        row, col = red_pos
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        if row < rows - 1:
            output_grid[row + 1, col] = 4  # Below
        if col > 0:
            output_grid[row, col - 1] = 4  # Left
        if col < cols - 1:
            output_grid[row, col + 1] = 4  # Right

    # Construct plus pattern around the blue cell
    if blue_pos:
        row, col = blue_pos
        if row > 0:
            output_grid[row - 1, col] = 7  # Above
        if row < rows - 1:
            output_grid[row + 1, col] = 7  # Below
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < cols - 1:
            output_grid[row, col + 1] = 7  # Right

    return output_grid