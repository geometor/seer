"""
1.  **Iterate through Columns:** For each column in the input grid, perform the following steps.
2.  **Identify Top-Row Color:** Determine the color value of the pixel in the first row (row 0) of the current column.
3.  **Propagate Downwards:** Copy the identified color value to all pixels below the first row within the *same* column in the output grid.
4.  **Output:** The output grid is the result of these column-wise propagations.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each column
    for j in range(cols):
        # Identify the color of the top-row pixel in the current column
        top_row_color = output_grid[0, j]

        # Propagate the top-row color downwards in the same column
        for i in range(1, rows):
            output_grid[i, j] = top_row_color

    return output_grid