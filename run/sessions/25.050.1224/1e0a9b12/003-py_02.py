"""
The colored cells are moved to the last row of the output, the other cells are filled with white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white cells to the last row,
    preserving their original column order, and filling the remaining cells with white.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find non-white cells and store their color and column
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], c))

    # Place the non-white cells in the last row
    for i, (color, col) in enumerate(non_white_cells):
        output_grid[rows - 1, col] = color

    return output_grid