"""
The transformation extracts a 5x5 subgrid from the top-left corner of the input grid and removes all blue (1) pixels, retaining only the green (3) and azure (8) pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Crops the input grid to a 5x5 subgrid from the top-left corner and removes blue pixels.
    """
    # Crop the grid to 5x5
    cropped_grid = input_grid[:5, :5]

    # Create a copy to avoid modifying the original cropped grid directly
    output_grid = np.copy(cropped_grid)

    # Remove blue pixels (replace 1s with 3s, which is the background color)
    output_grid[output_grid == 1] = 3

    return output_grid