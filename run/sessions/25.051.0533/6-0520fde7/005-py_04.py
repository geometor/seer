"""
The transformation focuses on the first and last rows of the central column
of the input grid. If the top cell is color 5 (gray), a red pixel (2) is placed
in the top-left cell of the output grid. If the bottom cell is color 5 (gray),
a red pixel (2) is placed in the bottom-left cell of the output grid. The output
is always a 3x3 grid filled with color 0 (white), plus the red pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with 0s.
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Find the center column index of the input grid.
    center_col = cols // 2

    # Check the top cell of the central column.
    if input_grid[0, center_col] == 5:
        output_grid[0, 0] = 2

    # Check the bottom cell of the central column.
    if input_grid[rows - 1, center_col] == 5:
        output_grid[2, 0] = 2

    return output_grid