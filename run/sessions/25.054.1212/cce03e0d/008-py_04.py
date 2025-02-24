"""
Transforms a 3x3 input grid into a 9x9 output grid by replicating the input grid in the top-right and bottom-left corners of the output grid, and filling the rest with 0s.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 9x9 output grid filled with 0s.
    output_grid = np.zeros((9, 9), dtype=int)

    # Copy the input grid to the top-right corner of the output grid.
    output_grid[0:3, 6:9] = input_grid

    # Copy the input grid to the bottom-left corner of the output grid.
    output_grid[6:9, 0:3] = input_grid

    return output_grid