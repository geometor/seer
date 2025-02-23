"""
The transformation rule is as follows:
1. Iterate through each column of the input grid.
2. For each column, record the presence and color of any non-white cell.
3. Clear the input, leaving only the white cells.
4. Construct the output grid by placing these recorded colors in the last row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white cells to the last row,
    maintaining their original column order.
    """
    # Initialize the output grid as a copy of the input grid, then filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column of the input grid.
    for j in range(input_grid.shape[1]):
        # Find the non-white cell in the current column.
        for i in range(input_grid.shape[0]):
            if input_grid[i, j] != 0:
                # Place the color of the non-white cell in the last row of the output grid.
                output_grid[-1, j] = input_grid[i, j]
                break  # only one move per column

    return output_grid