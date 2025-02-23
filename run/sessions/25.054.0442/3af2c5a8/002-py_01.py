"""
1.  **Double Rows:** Duplicate each row of the input grid. This transforms a 3x4 grid into a 6x4 grid.
2.  **Double, and shift Columns:** For the 6x4 grid, duplicate each column. However, in the duplicated column, shift any non-zero values to the position of value to it's right in the input. If there is no value to its right, the values are not placed.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Double Rows
    for i in range(rows):
        output_grid[i*2, 0:cols] = input_grid[i, :]
        output_grid[i*2+1, 0:cols] = input_grid[i, :]
    
    # Double, and shift Columns:
    for j in range(cols):
      for i in range(rows * 2):
        output_grid[i,j*2] = output_grid[i,j]
        if j+1 < cols and input_grid[i//2,j] != 0:
            output_grid[i,j*2+1] = input_grid[i//2,j]
        else:
            output_grid[i, j*2 + 1] = 0


    return output_grid.tolist()