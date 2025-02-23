"""
The transformation rule consists of changing the color value of each cell by a fixed amount.
The amount is determined by the parity of the column's index:

- Subtract 4 from the values of cells on odd columns.
- Add 1 to the values of cells on even columns.
Values are wrapped around using the modulo operator to keep the color values between 0-9.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing the color value of each cell
    based on the parity of its column index.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell of the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the column index is even or odd
            if (j + 1) % 2 == 1:  # Odd column
                output_grid[i, j] = (output_grid[i,j] - 4) % 10
            else:  # Even column
                output_grid[i, j] = (output_grid[i,j] + 1) % 10
    return output_grid