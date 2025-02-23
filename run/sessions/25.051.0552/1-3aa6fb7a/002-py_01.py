"""
The transformation rule is as follows:
1. Copy the input grid to the output grid.
2. Insert a blue pixel (color 1) to the right side of the pixel at row 1, column 2.
3. Insert a blue pixel (color 1) to the left side of the pixel at row 4, column 5.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # change output pixels
    output_grid[1, 3] = 1
    output_grid[4, 4] = 1

    return output_grid