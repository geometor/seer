"""
Identify the top row of the input grid. For each pixel in the top row, if the pixel's color is white (0), change its color to yellow (4). Keep all other pixels unchanged. Construct output using modified and non-modified rows.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through the pixels of the top row (index 0)
    for x in range(output_grid.shape[1]):
        # If the pixel is white (0), change it to yellow (4)
        if output_grid[0, x] == 0:
            output_grid[0, x] = 4

    return output_grid