"""
1. Identify Input and Output Grid size: The output grid will be the same size with the input grid. In this case, they are 3x3 grids.
2. Identify Blue Pixels: Locate all pixels within the input grid that have a value of 1 (blue).
3. Transform to Red: In output grid, change the color of the identified blue pixels to red (value 2).
4. Other Pixels: The other pixels in the input grid remains the same.
5. Output: A grid with the same size as the input, with the blue pixels changed to red and all other pixels remain the same.
"""

import numpy as np

def find_blue_pixels(grid):
    # Find the indices of all blue (1) pixels
    return np.where(grid == 1)

def transform(input_grid):
    # Initialize the output grid with the same shape and data type as the input
    output_grid = np.copy(input_grid)

    # Find all blue pixels
    blue_pixels = find_blue_pixels(input_grid)

    # Change to red and keep the same position in the output grid
    for i in range(len(blue_pixels[0])):
        row = blue_pixels[0][i]
        col = blue_pixels[1][i]
        output_grid[row, col] = 2

    return output_grid