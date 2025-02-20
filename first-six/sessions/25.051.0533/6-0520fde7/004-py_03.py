"""
The transformation extracts the central vertical column from the input grid.
If a pixel in this column is color 5 (gray), a red pixel (color 2) is placed
in the corresponding row and center column of the output grid. The output is
always a 3x3 grid filled with color 0 (white), except for the red pixels
determined by the central column of the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with 0s.
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Find the center column index of the input grid.
    center_col = cols // 2

    # Iterate through the rows of the input grid's central column.
    for i in range(min(rows,3)):  # Limit to the size of the output grid
        # Check if the pixel in the central column is color 5 (gray).
        if input_grid[i, center_col] == 5:
            # If so, set the corresponding pixel in the output grid to color 2 (red).
            output_grid[i, 1] = 2

    return output_grid