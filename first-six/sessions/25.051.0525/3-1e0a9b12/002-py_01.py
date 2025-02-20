"""
The transformation rule involves moving every non-zero object down to the last available row of the grid, while retaining the horizontal order. All the objects from the first row drop down to the last row. The order of the colored objects from the last row of the input is preserved, and the zero-colored cells in the last row are the only ones to change.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving each non-zero colored cell to the last row,
    maintaining their original horizontal order.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the dimensions of the grid
    rows, cols = input_grid.shape

    # Create a list to store non-zero elements and their original column indices
    non_zero_elements = []

    # Iterate through the input grid to find non-zero elements
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_elements.append((input_grid[r, c], c))

    # Sort the non-zero elements by their column index to maintain horizontal order
    non_zero_elements.sort(key=lambda x: x[1])

    # Clear the last row of the output grid
    output_grid[rows - 1, :] = 0

    # Place the non-zero elements in the last row of the output grid
    for i, (value, _) in enumerate(non_zero_elements):
        output_grid[rows - 1, i] = value
    
    # move non_zero objects to their new positions in the last row
    for c in range(cols):
      for r in range(rows):
        if input_grid[r,c] != 0:
          output_grid[rows-1,c] = input_grid[r,c]
          if r != rows -1:
            output_grid[r,c] = 0
    

    return output_grid