"""
Identify a 2x2 square region of uniform color within the input grid, and output this region.
"""

import numpy as np

def find_2x2_square(grid):
    """
    Finds the first 2x2 square of the same color in a grid.
    Returns the (row, col) of the top-left pixel and the color, or None if not found.
    """
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            color = grid[r, c]
            if (grid[r, c+1] == color and
                grid[r+1, c] == color and
                grid[r+1, c+1] == color):
                return (r, c, color)
    return None

def transform(input_grid):
    """
    Transforms the input grid by extracting the first 2x2 square of uniform color.
    """
    # Find the first 2x2 square.
    square_info = find_2x2_square(input_grid)

    # Extract the 2x2 square if found.
    if square_info:
        start_row, start_col, _ = square_info
        output_grid = input_grid[start_row:start_row+2, start_col:start_col+2]
        return output_grid
    else:
        return None  # Should not occur based on problem definition, but good practice
