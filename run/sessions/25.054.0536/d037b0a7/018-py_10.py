"""
1.  **Iterate through Columns:** For each column in the input grid:
2.  **Identify Top-Row Color:** Note the color of the pixel in the first row (row 0) of the current column. This is the initial `propagation_color`.
3.  **Conditional Propagation:** Iterate down the rows of the current column, starting from the second row (row 1):
    *   If the current cell in the input grid is 0, replace it with the current `propagation_color` in the output grid.
    *   If the current cell in the input grid is *not* 0, update the `propagation_color` to this new color, and *then* set the output cell to the `propagation_color`.
4.  **Output:** The output grid after processing all columns.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column
    for j in range(cols):
        # Identify the top-row color as the initial propagation color
        propagation_color = input_grid[0, j]
        output_grid[0,j] = propagation_color

        # Iterate down the rows of the column, starting from the second row
        for i in range(1, rows):
            # If the current cell in the input grid is 0, propagate the current color
            if input_grid[i, j] == 0:
                output_grid[i, j] = propagation_color
            # If the current cell is not 0, update propagation color and then propagate
            else:
                propagation_color = input_grid[i, j]
                output_grid[i, j] = propagation_color

    return output_grid