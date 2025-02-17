"""
Copies non-zero colored cells from the input grid to the last row of the output grid,
maintaining their relative horizontal order, except for objects in the third row which stays in place.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored cells to the last row,
    maintaining their order, except for objects in the third row which stays in place.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Get the height (number of rows) of the grid.
    height = input_grid.shape[0]
    
    # Copy the third row from input to output.
    output_grid[height - 2, :] = input_grid[height-2, :]

    # Get non-zero elements from the input grid.
    non_zero_indices = np.where(input_grid != 0)
    non_zero_values = input_grid[non_zero_indices]

    # Create a list to store non-zero elements and their original column indices for sorting, filtering third row.
    non_zero_elements = []
    for i in range(len(non_zero_values)):
      if non_zero_indices[0][i] != height - 2: #filter elements from third row.
        non_zero_elements.append((non_zero_values[i], non_zero_indices[1][i]))

    # Sort the non-zero elements based on their original column index.
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the sorted non-zero elements in the last row of the output grid.
    for i, (value, _) in enumerate(non_zero_elements):
        output_grid[height - 1, i] = value

    return output_grid