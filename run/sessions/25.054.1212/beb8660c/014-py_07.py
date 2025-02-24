"""
The transformation rule is as follows:
1. Leave the bottom row of the grid unchanged.
2. Rotate the remaining 2x2 sub-grid defined by the center pixel clockwise by 90 degrees.
3. Overwrite the cell to what now holds the top-left color with the background (0/white).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Leave the bottom row unchanged (already copied)

    # Rotate the 2x2 subgrid
    # extract top left
    top_left = input_grid[0, 0]

    # rotate, shift each element clockwise
    output_grid[0, 0] = input_grid[1, 0]  # top_left = bottom_left
    output_grid[0, 1] = top_left  # top_right = top_left
    output_grid[1, 0] = input_grid[1, 1]  # bottom_left = bottom_right
    output_grid[1, 1] = input_grid[0, 1]  # bottom_right = top_right

    # replace what use to be top-left with 0
    output_grid[0,0] = 0

    return output_grid