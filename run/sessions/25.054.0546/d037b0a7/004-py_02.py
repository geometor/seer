"""
1.  **Iterate through all pixels:** Examine each pixel in the input grid, row by row and column by column.
2.  **Check for Non-Zero Pixels:** If a pixel's value is not 0 (white), initiate a downward propagation.
3.  **Downward Propagation:** Propagate the non-zero pixel's value downwards, replacing any 0 (white) pixels encountered in the same column. Stop the propagation when a non-zero pixel or the bottom edge of the grid is reached.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through all pixels
    for row_index in range(rows):
        for col_index in range(cols):
            # Check for non-zero pixels
            if input_grid[row_index, col_index] != 0:
                # Downward Propagation
                for k in range(row_index + 1, rows):
                    if output_grid[k, col_index] == 0:
                        output_grid[k, col_index] = output_grid[row_index, col_index]
                    else:
                        break  # Stop propagation at non-zero pixel

    return output_grid