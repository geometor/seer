"""
Moves all non-white cells to the last row, preserving their original horizontal order, and setting all other cells to white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-white objects to the bottom row,
    preserving their horizontal order.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-white cells and their column indices
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((c, input_grid[r, c]))

    # Sort non-white cells by their column index (original horizontal order)
    non_white_cells.sort()

    # Place non-white cells in the last row of the output grid
    for i, (col, color) in enumerate(non_white_cells):
        output_grid[rows - 1, i] = color

    return output_grid.tolist()