"""
1.  **Background Fill:** Replace all 0s in the input grid with 8s.

2.  **Cross Construction:**
    *   Locate the single cell with the value of 1 in the input grid
    *   In the output grid, set this original location to 1.
    *   From this position extend the value 1 outwards along the row and column to form the four points of the cross.
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

    # construct cross
    output_grid[one_row, :] = 1    # horizontal
    output_grid[:, one_col] = 1    # vertical

    return output_grid