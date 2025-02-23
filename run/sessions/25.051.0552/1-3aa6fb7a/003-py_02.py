"""
The transformation rule is as follows:
1. Copy the input grid to the output grid.
2. Insert a blue pixel (color 1) to the left side of the pixel at row 0, column 5.
3. Insert a blue pixel (color 1) at position (2, 3).
4. Insert a blue pixel (color 1) on top of the pixel at row 6, column 3.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # change output pixels
    output_grid[0, 4] = 1
    output_grid[2, 3] = 1
    output_grid[5, 3] = 1

    return output_grid