"""
1.  **Duplicate:** Create a vertically duplicated copy of the input grid. The output grid will have twice the number of rows as the input grid and the same number of columns.

2.  **Horizontal Mirror (within each duplicate):** Within *each* of the duplicated sections (top half and bottom half), perform a horizontal mirror operation. This means reversing the order of columns within each half.  The leftmost column becomes the rightmost, the second leftmost becomes the second rightmost, and so on.
"""

import numpy as np

def transform(input_grid):
    # Duplicate the input grid vertically
    output_grid = np.concatenate((input_grid, input_grid), axis=0)

    # Get dimensions of the output grid and input_grid
    rows_out, cols_out = output_grid.shape
    rows_in, cols_in = input_grid.shape

    # Horizontal Mirror (Top Half)
    for i in range(rows_in):
        output_grid[i, :] = input_grid[i, ::-1]  # Reverse the row

    # Horizontal Mirror (Bottom Half)
    for i in range(rows_in):
        output_grid[i + rows_in, :] = input_grid[i, ::-1] # Reverse the row

    return output_grid