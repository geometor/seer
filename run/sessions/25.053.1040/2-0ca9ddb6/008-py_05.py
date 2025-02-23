"""
1.  **Initialization:** Create an output grid filled with zeros (white), having the same dimensions as the input grid.

2.  **Red Pixel Processing:** Locate each red (value 2) pixel in the input grid. For each red pixel, create a 2x2 square of yellow (value 4) pixels.  The red pixel should be located in the *bottom-right* corner of this yellow square.

3.  **Blue Pixel Processing:** Locate each blue (value 1) pixel in the input grid. For each blue pixel, create a 3x3 square of orange (value 7) pixels. The blue pixel should be located at the *center* of this orange square.

4.  **Output:** The output is the modified grid, containing only values 0, 4, and 7, where all pixels that are not part of a yellow or orange surround have the value 0.
"""

import numpy as np

def find_pixels(grid, color):
    # Find the coordinates of all pixels with the specified color.
    return np.argwhere(grid == color)

def transform(input_grid):
    # Initialize output_grid with zeros, same dimensions as input.
    output_grid = np.zeros_like(input_grid)

    # Create Yellow Surrounds for Red Pixels
    red_pixels = find_pixels(input_grid, 2)
    for red_pixel in red_pixels:
        row, col = red_pixel
        # Create the 2x2 yellow surround.  The red pixel will be at the bottom-right.
        for i in range(row , row + 2):
            for j in range(col, col + 2):
                if 0 <= i < output_grid.shape[0] and 0 <= j < output_grid.shape[1]:
                    output_grid[i, j] = 4

    # Create Orange Surrounds for Blue Pixels
    blue_pixels = find_pixels(input_grid, 1)
    for blue_pixel in blue_pixels:
        row, col = blue_pixel
        # Create the 3x3 orange surround, centered on the blue pixel.
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < output_grid.shape[0] and 0 <= j < output_grid.shape[1]:
                    output_grid[i, j] = 7

    return output_grid