"""
The transformation replaces the top row of yellow (4) pixels with gray (5) pixels and the rest with white (0) pixels.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy to avoid modifying the original
    output_grid = np.copy(input_grid)
    
    # get dimensions
    rows, cols = output_grid.shape

    # replace values in the first row with 5
    output_grid[0, :] = 5

    # replace values in the second and third rows with 0
    for i in range(1, rows):
        output_grid[i, :] = 0

    return output_grid