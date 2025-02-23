"""
The transformation involves the following steps:

1.  **Identify the red pixel:** Locate the single red (color 2) pixel in the input grid.
2.  **Determine output positions:**  The output positions are determined relative to where the input red pixel *would have been* if the grid was 5x5 and the red pixel was always in the diagonal from top-left to bottom right.
3.  **Map Input Red pixel location to color:**
    *   If the red pixel is on an odd row and odd column, create 4 output pixels: green (3) above and left, magenta(6) above and right, azure (8) down and left and orange(7) down and right.
    *   If the red pixel is on an even row and even column, create 4 output pixels: green (3) above and left, magenta(6) above and right, azure (8) down and left and orange(7) down and right.
    *   If the red pixel is on an odd row and even column, generate an azure (8) pixel to the left and an orange (7) pixel to the right on the row below.
    *    If the red pixel is on an even row and odd column, generate a green(3) pixel directly above.

4.  **All other output pixels are black (0).**
"""

import numpy as np

def find_red_pixel(grid):
    # Find the coordinates of the red pixel (color 2).
    red_pixels = np.argwhere(grid == 2)
    if len(red_pixels) > 0:
      return red_pixels[0]
    return None

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input, filled with black (0).
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find the red pixel in the input.
    red_pixel = find_red_pixel(input_grid)

    if red_pixel is None:
        return output_grid

    row, col = red_pixel

    # Apply transformation rules based on red pixel position.
    if (row % 2 != 0 and col % 2 != 0) or (row % 2 == 0 and col % 2 == 0):
        if row > 0 and col > 0:
          output_grid[row - 1, col - 1] = 3
        if row > 0 and col < output_grid.shape[1] -1:
          output_grid[row - 1, col + 1] = 6
        if row < output_grid.shape[0] -1 and col > 0:
          output_grid[row + 1, col - 1] = 8
        if row < output_grid.shape[0] - 1 and col < output_grid.shape[1] - 1:
          output_grid[row + 1, col + 1] = 7
    elif row % 2 != 0 and col % 2 == 0:
        if row < output_grid.shape[0] -1 and col > 0:
          output_grid[row + 1, col - 1] = 8
        if row < output_grid.shape[0] - 1 and col < output_grid.shape[1] -1:
          output_grid[row + 1, col + 1] = 7
    elif row % 2 == 0 and col % 2 != 0:
        if row > 0:
          output_grid[row - 1, col] = 3

    return output_grid