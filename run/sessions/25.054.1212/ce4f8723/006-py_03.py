"""
Downsamples the input grid to a 4x4 output grid. Non-white pixels in the input
grid's top-left 4x4 section map to green (3) in the output grid, while white
pixels (0) remain white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the 4x4 output grid with zeros (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through the top-left 4x4 section of the input grid
    for i in range(4):
        for j in range(4):
            # Check if the current position is within the bounds of the input grid
            if i < len(input_grid) and j < len(input_grid[0]):
                # Get the pixel value from the input grid.
                pixel_value = input_grid[i][j]

                # If the pixel is not white, set the corresponding output pixel to green.
                if pixel_value != 0:
                    output_grid[i][j] = 3

    return output_grid