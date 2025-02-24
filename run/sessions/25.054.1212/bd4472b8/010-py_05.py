"""
1.  **Copy First Two Rows:** Copy the first two rows of the `input_grid` directly to the `output_grid`.

2.  **Element-wise Repetition:** For each element (pixel value) in the first row of the `input_grid`:
    *   Create subsequent rows in the `output_grid` by repeating that element to create columns of each value from the first row, repeated for the height of the original input grid.

3. The number of rows created below the copied rows is equal to the input_grid height minus two, which is the number of rows copied to the top.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input_grid
    output_grid = np.copy(input_grid)

    # Copy the first two rows of the input_grid to the output_grid
    #output_grid[:2] = input_grid[:2]  # Already handled by np.copy

    # Get the first row of the input grid
    first_row = input_grid[0]
    num_rows_to_add = input_grid.shape[0] - 2

    # Iterate through each element in the first row and create new rows
    for i in range(len(first_row)):
      for j in range(num_rows_to_add):
        output_grid[2 + j, i] = first_row[i]

    return output_grid