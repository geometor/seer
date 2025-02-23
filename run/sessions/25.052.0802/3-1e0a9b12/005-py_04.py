"""
The transformation rule is as follows:
1. Iterate through each column of the input grid.
2. For each column, find the bottom-most non-white cell.
3. Move each of those cells to the last row of the output grid, maintaining the original column.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving the bottom-most non-white cell in each column
    to the last row, maintaining their original column order.
    """
    # Initialize the output grid as all zeros (white).
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column of the input grid.
    for j in range(input_grid.shape[1]):
        # Find the bottom-most non-white cell in the current column.
        for i in reversed(range(input_grid.shape[0])):
            if input_grid[i, j] != 0:
                # Place the color of the bottom-most non-white cell in the last row of the output grid.
                output_grid[-1, j] = input_grid[i, j]
                break  # Stop after finding the first non-white cell from the bottom

    #Copy the last row from the input to the output
    output_grid[-1,:] = input_grid[-1,:]

    #Add elements from the next to last row
    for j in range(input_grid.shape[1]):
      if input_grid[-2,j] != 0:
        output_grid[-2,j] = input_grid[-2,j]
    return output_grid