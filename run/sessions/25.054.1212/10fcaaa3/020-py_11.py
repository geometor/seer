"""
Expands the input grid to double its size, replicates the red pixel, and fills 
alternating pixels with azure in a checkerboard pattern, leaving the rest white.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with double the dimensions of the input grid.
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 2, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Find the red pixel in the input grid.
    red_pixels = np.argwhere(input_grid == 2)

    # Replicate red pixels.
    for red_pixel in red_pixels:
      row, col = red_pixel
      output_grid[row*2+1, col*2+1] = 2  # original location in the upscaled output
      output_grid[row*2+1, (col+2)*2+1] = 2  # copy at the upscaled x-coordinate +4 to its right
      output_grid[(row+2)*2+1, col*2+1] = 2
      output_grid[(row+2)*2+1, (col+2)*2+1] = 2

    # Fill alternating pixels with azure (8).
    for i in range(output_height):
        for j in range(output_width):
            if (i + j) % 2 == 0:
                output_grid[i, j] = 8

    return output_grid