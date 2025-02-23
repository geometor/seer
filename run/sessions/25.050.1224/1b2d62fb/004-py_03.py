"""
Transforms an input grid with a vertical blue line into an output grid. The output grid has a width of 3 and the same number of rows as the input. Two azure pixels are placed in the output grid on the row where the blue line starts in the input, and the rest of the grid is filled with white (0).
"""

import numpy as np

def get_blue_column_and_first_row(grid):
    """Finds the column index and the first row index containing blue pixels."""
    rows, cols = grid.shape
    first_row = -1
    for j in range(cols):
      for i in range(rows):
        if grid[i, j] == 1:  # Assuming blue is represented by 1.
           if first_row == -1:
              first_row = i
           return j, first_row #Return the col index, and where a blue pixel starts.
    return -1, -1 # Not found

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    # Initialize output grid: same number of rows, width = 3, filled with 0s.
    rows = input_grid.shape[0]
    output_grid = np.zeros((rows, 3), dtype=int)

    # Get the column and the first row where blue appears.
    blue_col, first_blue_row = get_blue_column_and_first_row(input_grid)

    # If blue is found, place two azure pixels in the corresponding row.
    if first_blue_row != -1:
      output_grid[first_blue_row, 1] = 8  # Azure color
      output_grid[first_blue_row, 2] = 8  # Azure color
    
    return output_grid