"""
1. Iterate through each pixel in the input grid.
2. If a pixel's value is 1 (blue) and it is located in the first row of the input grid, change its value to 2 (red) in the output grid.
3.  Check If the pixel has value of 1 (blue) and is located in the last row, the value in the output will be 0 (white)
4. Else, keep the original value of the pixel (0, white) unchanged in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions and values as the input grid.
    output_grid = np.copy(input_grid)
    rows = input_grid.shape[0]
    cols = input_grid.shape[1]

    # Iterate through each pixel in the input grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel's value is 1 (blue).
            if input_grid[i, j] == 1:
                # If the pixel is in the first row, change its value to 2 (red).
                if i == 0:
                    output_grid[i, j] = 2
                # If the pixel is in the last row, change its value to 0
                elif i == rows -1:
                    output_grid[i,j] = 0

    return output_grid