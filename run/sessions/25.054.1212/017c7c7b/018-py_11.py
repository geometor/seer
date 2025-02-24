"""
1.  **Color Swap:** Scan the input grid. Replace every blue pixel (value 1) with a red pixel (value 2). White pixels (value 0) are unchanged.
2.  **Extend Grid:** Create a new, empty grid that has the same number of columns as the input grid, but with three additional rows.
3.  **Copy Original Rows:** Copy all rows of the *original* input grid into the top of the new grid.
4.  **Replicate Rows:** Copy the first three rows of the *original* input grid into the three newly added rows at the bottom of the output grid, maintaining their original order (row 1 to row `rows`, row 2 to row `rows+1`, and row 3 to row `rows+2`).
"""

import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to modify for color replacement
    modified_grid = np.copy(input_grid)

    # Replace all blue (1) pixels with red (2) pixels
    modified_grid[modified_grid == 1] = 2

    # Get the dimensions of the original input grid
    rows, cols = input_grid.shape

    # Create a new, empty grid with 3 extra rows
    output_grid = np.zeros((rows + 3, cols), dtype=int)

    # Copy the color-modified grid into the new grid
    output_grid[:rows, :] = modified_grid

    # Replicate the FIRST three rows of the ORIGINAL input grid
    output_grid[rows:rows + 3, :] = input_grid[:3, :]

    return output_grid