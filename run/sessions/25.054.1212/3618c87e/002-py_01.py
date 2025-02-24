"""
The transformation rule is to swap the colors of the blue (1) pixel and the gray (5) pixel directly below it.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    # Find the coordinates of a pixel of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return first occurrence
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the blue (1) pixel
    blue_pixel_coords = find_pixel_by_color(input_grid, 1)

    if blue_pixel_coords:
        # Calculate coordinates of the pixel below
        row_below = blue_pixel_coords[0] + 1
        col_same = blue_pixel_coords[1]

        # Check if the pixel below is within bounds and is gray (5)
        if row_below < output_grid.shape[0] and output_grid[row_below, col_same] == 5:
            # Swap colors
            output_grid[blue_pixel_coords[0], blue_pixel_coords[1]] = 5
            output_grid[row_below, col_same] = 1

    return output_grid