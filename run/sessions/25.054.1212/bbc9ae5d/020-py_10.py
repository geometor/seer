"""
Replicate the input row three times. Then, in the new grid, keep only the first row of two '0' (white) values from the input, eliminating the rest below them.
"""

import numpy as np

def transform(input_grid):
    # Replicate the input row three times.
    output_grid = np.tile(input_grid, (3, 1))

    # Keep only the top row of last two column constant
    output_grid[1:, 4:] = input_grid[0,4]
    output_grid[2,5] = input_grid[0,4]
    output_grid[1,5] = input_grid[0,4]


    return output_grid