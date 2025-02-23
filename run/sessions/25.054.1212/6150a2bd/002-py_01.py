"""
The transformation involves rotating the input grid by 180 degrees clockwise.
The operation swaps the position of the element at i,j index location with (n-1-i, m-1-j) where n and m represents total rows and columns.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # change output pixels 
    for i in range(rows):
        for j in range(cols):
            output_grid[rows - 1 - i, cols - 1 - j] = input_grid[i, j]

    return output_grid.tolist()