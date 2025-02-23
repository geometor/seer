"""
Transforms a 4x3 input grid into a 6x3 output grid. The first two columns are copied directly. 
The third column's values [1, 1, 8, 8] are transformed to [8, 8, 0, 0]. 
Two new rows are added at the bottom, with the first element being 1 and the remaining elements being 0.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 6x3 array filled with zeros.
    output_grid = np.zeros((6, 3), dtype=int)

    # Copy the first column.
    output_grid[:4, 0] = input_grid[:, 0]

    # Copy the second column.
    output_grid[:4, 1] = input_grid[:, 1]

    # Transform and copy the third column.
    output_grid[0, 2] = 8
    output_grid[1, 2] = 8
    output_grid[2, 2] = 0
    output_grid[3, 2] = 0

    # Add the new rows.
    output_grid[4, 0] = 1
    output_grid[5, 0] = 1

    return output_grid