"""
The transformation rule is to shift the top row of the input grid down by one position, making it the middle row in the output grid. The other rows shift accordingly, with original middle row becoming the bottom row in the input and original bottom row becoming the top row in the output. In other words, cyclically permute rows down by one.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows = input_grid.shape[0]

    # cyclically permute rows down by one
    output_grid[0, :] = input_grid[rows-1, :]
    output_grid[1, :] = input_grid[0, :]
    output_grid[2, :] = input_grid[1, :]
    

    return output_grid