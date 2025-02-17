"""
The transformation rule involves taking non-white cells on the input grid and moving them to the last row of the output grid if the row index is less than number of rows-1, keeping their original column position. Otherwise the coloured cells remain in place. All other cells turn white.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid, then fill with white (0).
    output_grid = np.zeros_like(input_grid)

    # Get the dimensions of the grid.
    rows, cols = input_grid.shape

    # Iterate through the input grid to find non-white cells.
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != 0:
                # Move the non-white cell to the last row of the output grid.
                if i < rows - 1:
                  output_grid[rows - 1, j] = input_grid[i, j]
                else:
                  output_grid[i,j] = input_grid[i,j]
    
    # Iterate over original positions of moved cells, making them zero
    for j in range(cols):
        for i in range(rows-1):
           if input_grid[i,j]!= 0: output_grid[i,j] = 0
    
    return output_grid