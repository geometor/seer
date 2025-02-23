"""
The input grid is divided into nine 3x3 subgrids. Each subgrid maps to a single pixel in the output grid.  The output color for each subgrid is determined by the color value of the center pixel ONLY if it contains a 1, 2, 3, or 6. Otherwise, the value is 0.
"""

import numpy as np

def get_subgrid_center_value(grid, row_index, col_index):
    """Gets the value of the center pixel of a 3x3 subgrid."""
    subgrid_center_row = row_index * 3 + 1
    subgrid_center_col = col_index * 3 + 1
    return grid[subgrid_center_row, subgrid_center_col]
    

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid) # make sure input is numpy array

    # Iterate through each 3x3 subgrid.
    for row in range(3):
        for col in range(3):
            # Determine the output color for the current subgrid.
            center_value = get_subgrid_center_value(input_grid, row, col)
            if center_value in (1, 2, 3, 6):
                output_grid[row, col] = center_value
            else:
                output_grid[row, col] = 0

    return output_grid