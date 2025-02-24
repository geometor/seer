"""
Finds the '1' pixel in the input grid and replaces all '0' pixels with a checkerboard pattern of '8' and '1' values, radiating outwards from the location of the initial '1' pixel. The '1' pixel's location in the output corresponds directly to its location in the input.  The checkerboard pattern starts with '8' in the top-left corner of the output grid, regardless of where the '1' pixel is located.
"""

import numpy as np

def find_pixel(grid, value):
    # Find the coordinates of the pixel with the specified value.
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel == value:
                return (r, c)
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the coordinates of the '1' pixel.
    blue_pixel_coords = find_pixel(input_grid, 1)
    if blue_pixel_coords is None:
        return output_grid #should not happen based on prior

    # Iterate through the grid and apply the checkerboard pattern, starting from top-left (0,0).
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:
                if (r + c) % 2 == 0:
                    output_grid[r, c] = 8
                else:
                    output_grid[r, c] = 1

    return output_grid