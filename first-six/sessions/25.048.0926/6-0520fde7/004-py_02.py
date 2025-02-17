"""
The transformation extracts the central pixel of the original shape to create a new 3x3 grid. For each row,
it counts the blue pixels. If the blue count is greater than 0, it replaces the central white pixel in the
output grid with a red one (color code 2). The other pixels in the output remain white (color code 0).
"""

import numpy as np

def transform(input_grid):
    # Create an output grid with size 3x3 filled with white pixels (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through each row of the input grid.
    for i in range(input_grid.shape[0]):
        # Count the number of blue objects (pixels with value 1) in the current row.
        blue_count = np.count_nonzero(input_grid[i, :] == 1)

        # If blue_count is greater than 0, set the corresponding central pixel in the output grid to 2 (red).
        if blue_count > 0:
            output_grid[i, 1] = 2

    return output_grid