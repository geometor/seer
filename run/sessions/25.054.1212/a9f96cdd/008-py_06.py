"""
Locate the single non-zero pixel in the input grid. Change its color from 2 (red) to 3 (green). Move the pixel one position diagonally up and to the left. Construct the output grid with the moved and recolored pixel, and all other cells set to 0.
"""

import numpy as np

def find_non_zero_pixel(grid):
    # Find the coordinates of the non-zero pixel
    non_zero_indices = np.nonzero(grid)
    return list(zip(non_zero_indices[0], non_zero_indices[1]))[0]

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.zeros_like(input_grid)

    # Find the non-zero pixel in the input grid
    input_pixel_coords = find_non_zero_pixel(input_grid)

    # Calculate the new coordinates for the pixel (one step up and one step left)
    output_pixel_coords = (input_pixel_coords[0] - 1, input_pixel_coords[1] - 1)

    # Change color and set output
    output_grid[output_pixel_coords[0], output_pixel_coords[1]] = 3

    return output_grid