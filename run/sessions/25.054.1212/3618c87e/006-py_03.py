"""
1.  Identify all blue (1) pixels in the input grid.
2.  For each blue pixel, check if a gray (5) pixel exists directly below it.
3.  If a gray pixel is found directly below a blue pixel, swap their positions: the blue pixel moves to the gray pixel's location, and the gray pixel moves to the blue pixel's original location.
4.  The final output grid reflects these single swaps. The bottom row, initially all gray, will have blue pixels where swaps occurred. Other rows will shift accordingly.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds coordinates of all pixels of a given color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid by swapping blue and gray pixels."""
    output_grid = np.copy(input_grid)
    blue_pixels = find_pixels_by_color(output_grid, 1)

    for row, col in blue_pixels:
        next_row = row + 1
        # Check bounds and if the pixel below is gray
        if next_row < output_grid.shape[0] and output_grid[next_row, col] == 5:
            # Swap the blue and gray pixels
            output_grid[row, col], output_grid[next_row, col] = output_grid[next_row, col], output_grid[row, col]

    return output_grid