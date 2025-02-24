"""
1.  **Find Center:** Locate the single blue pixel (value '1') within the input grid. Record its row and column coordinates.

2.  **Background:** Change all white pixels (value '0') in the input grid to azure (value '8').

3.  **Create Alternating Cross:** Construct a cross centered at the location found in step 1. The cross is created by the following:
    *   The center pixel is blue (value '1').
    *   Horizontal: Extend the line of pixels horizontally to the edges of the input grid. From the center, alternate between azure (8) and blue (1), where the first pixel in each direction from the center will be azure.
    *   Vertical: Extends the line of pixels vertically to the edges of the input grid. From the center, alternate between azure (8) and blue (1), where the first pixel above/below the center will be azure.

4. output the changed grid.
"""

import numpy as np

def find_object(grid, value):
    # finds all instances of value and returns coordinates
    coords = np.where(grid == value)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # initialize output_grid
    output_grid = np.full(input_grid.shape, 8)

    # find the location of the 1
    one_locations = find_object(input_grid, 1)
    if not one_locations:  # Handle edge case with no 1 present.
       return output_grid
       
    one_row, one_col = one_locations[0]

    # construct cross with alternating values
    # horizontal
    output_grid[one_row, one_col] = 1
    for i in range(one_col + 1, input_grid.shape[1]):
        output_grid[one_row, i] = 1 if (i - one_col) % 2 == 0 else 8
    for i in range(one_col - 1, -1, -1):
        output_grid[one_row, i] = 1 if (one_col - i) % 2 == 0 else 8

    # vertical
    for i in range(one_row + 1, input_grid.shape[0]):
        output_grid[i, one_col] = 1 if (i - one_row) % 2 == 0 else 8
    for i in range(one_row - 1, -1, -1):
        output_grid[i, one_col] = 1 if (one_row - i) % 2 == 0 else 8

    return output_grid