"""
Locate the single blue pixel (value 1) in the input grid and change its value to red (value 2). Keep all other pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing the blue pixel to red.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the coordinates of the blue pixel (value 1)
    blue_pixel_coords = np.where(output_grid == 1)

    # Change the value of the blue pixel to red (value 2) if found.
    if blue_pixel_coords[0].size > 0:  # Check if a blue pixel was found
      output_grid[blue_pixel_coords[0][0], blue_pixel_coords[1][0]] = 2

    return output_grid