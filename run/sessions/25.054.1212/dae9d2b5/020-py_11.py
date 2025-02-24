"""
The transformation takes the left half of the input grid and replaces all non-white colors (specifically green and yellow) with magenta, resulting in a 3x3 output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols // 2), dtype=int)

    # change output pixels 
    for i in range(rows):
        for j in range(cols // 2):
            if input_grid[i][j] == 3 or input_grid[i][j] == 4:
                output_grid[i][j] = 6
            else:
                output_grid[i][j] = input_grid[i][j]

    return output_grid