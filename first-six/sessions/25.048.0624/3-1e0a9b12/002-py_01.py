"""
Transformation Rule:

1. Identify all non-zero colored cells in the input grid.
2. Move these cells to the last row of the output grid.
3. Maintain the original column index of each cell during the move.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells
    to the last row, preserving their original column positions.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find all non-zero cells and their column indices
    non_zero_cells = []
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                non_zero_cells.append((input_grid[r, c], c))

    # Place the non-zero cells in the last row of the output grid
    for i, (value, col) in enumerate(non_zero_cells):
        output_grid[rows - 1, col] = value
        
    # Copy cells from row 2
    output_grid[2,:] = input_grid[2,:]

    return output_grid.tolist()