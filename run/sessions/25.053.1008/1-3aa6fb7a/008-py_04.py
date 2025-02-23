"""
The transformation identifies azure (8) pixels in the input grid. 
It then changes white (0) pixels to blue (1) if they are immediately to the left or above an azure pixel.
"""

import numpy as np

def get_azure_pixels(grid):
    """Finds the coordinates of all azure (8) pixels."""
    return np.argwhere(grid == 8)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_pixels = get_azure_pixels(input_grid)

    for row, col in azure_pixels:
        # Check Left
        if col > 0 and output_grid[row, col - 1] == 0:
            output_grid[row, col - 1] = 1
        # Check Above
        if row > 0 and output_grid[row - 1, col] == 0:
            output_grid[row - 1, col] = 1

    return output_grid