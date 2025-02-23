"""
Copies the input grid to the output grid, then changes the color of the pixel at the bottom-left corner (coordinates (2, 0)) from red (2) to blue (1).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Change the color of the pixel at the bottom-left corner (2, 0) to blue (1).
    output_grid[2, 0] = 1

    return output_grid