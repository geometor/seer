"""
1.  Identify all non-zero and non-grey (not equal to 5) cells in the top row of the input grid.
2.  Sum the values of these identified cells.
3.  Replace the value of the top-left cell (first cell) in the output grid with this sum.
4. Set values of the summed cells of the top row in the input to 0 in the output grid.
5.  Copy all other cells, which are not located in the top row or are grey, from the input grid to the output grid without changes.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Calculate the sum of non-zero and non-grey values in the top row.
    top_row_sum = 0
    for i in range(len(input_grid[0])):
      if input_grid[0, i] != 0 and input_grid[0, i] != 5:
          top_row_sum += input_grid[0, i]
          output_grid[0,i] = 0

    # Replace the top-left cell's value with the sum.
    output_grid[0, 0] = top_row_sum


    return output_grid