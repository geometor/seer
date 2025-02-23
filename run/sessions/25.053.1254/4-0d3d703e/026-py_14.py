"""
Replace all red pixels with magenta pixels, leaving all other colored pixels as they are.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid to avoid modifying the original.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel of the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Check if the pixel is red (value 2).
            if output_grid[i, j] == 2:
                # Change the pixel to magenta (value 6).
                output_grid[i, j] = 6

    return output_grid