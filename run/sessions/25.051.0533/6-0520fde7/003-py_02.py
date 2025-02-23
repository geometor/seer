"""
The transformation extracts the central vertical line from the input grid.
Each element of this line triggers the creation of a red pixel (color 2) in the
middle of each row (center column) of the output grid. The output grid is always
3x3 and filled mainly with color 0 (white).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid to a 3x3 output grid.
    It focuses on the central vertical line.
    """
    # Initialize output_grid as a 3x3 array filled with 0s.
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Find the center column of the input grid.
    center_col = cols // 2

    # Iterate through each row and check the center column.
    for i in range(min(rows, 3)):  # Ensure we don't exceed output grid bounds
      if input_grid[i,center_col] == 5:
        output_grid[i, 1] = 2

    return output_grid