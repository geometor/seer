"""
Iterate through each pixel in the input grid. If the color is blue (1), keep the same color in the output grid. If the color is 2, 3, or 8 (red, green, or azure), change it to gray (5). Otherwise, retain the original color. Place each transformed or kept color value in the output grid using the index from iteration.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the input grid.
    for i in range(rows):
        for j in range(cols):
            # Check the color of the current pixel.
            color = input_grid[i, j]

            # If the color is blue (1), keep the same color.
            if color == 1:
                continue  # Output grid already has the same value.
            # If the color is 2, 3, or 8, change it to gray (5).
            elif color in (2, 3, 8):
                output_grid[i, j] = 5
            # Else, retain original color

    return output_grid