"""
1.  **Initialization:** Start with the input grid.

2.  **Copy Down:** Iterate through the input grid from top to bottom.
    *   If a pixel is not white (color 0), check downwards in its column. If a non-zero pixel in the column is found, copy/move all continuous non-zero pixels downwards to positions below the last non-zero pixel.

3.  **Whitespace:** All remaining pixels that have not been filled through step 2, change them to white (color 0).
"""

import numpy as np

def find_non_zero_below(grid, col):
    """Finds the row indices of non-zero elements below the last non-zero element in a column."""
    rows, _ = grid.shape
    non_zero_rows = []
    last_non_zero = -1

    #find last non zero
    for i in range(rows):
      if grid[i,col] != 0:
        last_non_zero = i

    if last_non_zero == -1:
        return [] #no non-zero in column

    for i in range(last_non_zero + 1, rows):
        if grid[i, col] != 0:
          non_zero_rows.append(i)

    return non_zero_rows

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through columns.
    for j in range(cols):
        non_zero_indices = find_non_zero_below(input_grid, j)

        #if none, skip the copy
        if not non_zero_indices:
          continue

        #get all non zero values above this
        last_non_zero_in_col = -1
        for i in range(rows):
          if input_grid[i,j] != 0:
            last_non_zero_in_col = i

        values_to_move = []
        for i in range(0, last_non_zero_in_col + 1):
          if input_grid[i,j] != 0:
            values_to_move.append(input_grid[i,j])

        #copy/move down based on last_non_zero
        write_idx = last_non_zero_in_col + 1
        for val in values_to_move:
          if write_idx < rows:
            output_grid[write_idx, j] = val
            write_idx += 1

    return output_grid