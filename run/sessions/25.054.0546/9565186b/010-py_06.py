"""
Iterate through each pixel of the input grid. If the input pixel's color is 1, 2, 3 or 8, and 4 is present in the input, change the color in the output grid to gray (5). If the input pixel's color is 4, keep the color 4. If there is no 4 in the input, then: if the color is 8, change it to 5. If the color is 1, change it to 5. Otherwise, keep original colors.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    has_color_4 = 4 in input_grid

    # Iterate through each pixel in the input grid.
    for i in range(rows):
        for j in range(cols):
            color = input_grid[i, j]

            if has_color_4:
                if color in (1, 2, 3, 8):
                    output_grid[i,j] = 5
                elif color == 4:
                    output_grid[i,j] = 4
            else:
                if color == 8:
                    output_grid[i,j] = 5
                elif color == 1:
                    output_grid[i, j] = 5
                #else retain the original color, no operation necessary

    return output_grid