"""
Transforms an input grid with a blue vertical line into an output grid with 
two azure pixels horizontally centered on the *first* row where blue was present, 
and the rest of the grid filled with white.
"""

import numpy as np

def get_blue_column_and_first_row(grid):
    """Finds the column index and the first row index containing the vertical blue line."""
    rows, cols = grid.shape
    first_row = -1
    for j in range(cols):
      for i in range(rows):
        if grid[i, j] == 1:  # Assuming blue is represented by 1.
           if first_row == -1:
              first_row = i
           
           return j, first_row #Return the col index, and where the blue line starts.
    return -1, -1

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """

    rows = input_grid.shape[0]
    output_grid = np.zeros((rows, 3), dtype=int)

    blue_col, first_blue_row = get_blue_column_and_first_row(input_grid)
    
    output_grid[first_blue_row, 1] = 8
    output_grid[first_blue_row, 2] = 8

    return output_grid