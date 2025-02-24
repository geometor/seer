"""
The input grid is downsampled to a 4x4 grid. The top-left 4x4 subgrid of the input grid is selected.
Within this subgrid, all non-white (0) pixels are converted to green (3), while white pixels remain white.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a 4x4 array with zeros
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through the top-left 4x4 subgrid of the input
    for i in range(4):
        for j in range(4):
            # Get the pixel value from the input grid
            pixel_value = input_grid[i][j]

            # Apply the color transformation rule
            if pixel_value == 0:  # If white, keep white
                output_grid[i][j] = 0
            else:  # If not white, change to green
                output_grid[i][j] = 3

    return output_grid