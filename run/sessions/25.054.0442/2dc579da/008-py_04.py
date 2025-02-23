"""
Finds the blue (value 1) pixel in the input, and creates a 3x3 output grid centered on that blue pixel, 
copying the colors of the surrounding pixels from the input. All other parts of the input grid are discarded.
"""

import numpy as np

def find_blue_pixel(grid):
    # Find coordinates of the blue pixel (value 1)
    blue_pixels = np.where(grid == 1)
    if len(blue_pixels[0]) == 1:
      return blue_pixels[0][0], blue_pixels[1][0]  # (row, col)
    return None

def transform(input_grid):
    # Find the blue pixel
    blue_pixel_coords = find_blue_pixel(input_grid)

    # Handle the case where there's no single blue pixel or multiple
    if blue_pixel_coords is None:
        return input_grid.copy()

    blue_row, blue_col = blue_pixel_coords

    # Initialize the output grid with a default value (e.g., 0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Extract the 3x3 region around the blue pixel
    for i in range(3):
        for j in range(3):
            input_row = blue_row - 1 + i
            input_col = blue_col - 1 + j

            # Check if the indices are within the bounds of the input grid
            if 0 <= input_row < input_grid.shape[0] and 0 <= input_col < input_grid.shape[1]:
                output_grid[i, j] = input_grid[input_row, input_col]
            # else leave them as the default value (0)
            

    return output_grid