"""
1.  **Output Initialization:** Create a 3x3 output grid filled with white pixels (0).
2.  **Input Reference Point:** Determine a reference column on the input grid. This column is located three positions from the right edge of the input grid.
3.  **Iterate Output Grid:** Loop through each cell (row, col) of the 3x3 output grid.
4.  **Conditional Mapping:**
    *   Calculate a corresponding input column: `input_col = reference_col + output_col - 1`.
    *   Calculate corresponding input row: `input_row = output_row`
    *    If `input_col` is within the bounds of the input grid, and if the pixel at `input_grid[input_row, input_col]` is white (0), then set the output grid's current cell to red (2). Otherwise the output grid cell remains white(0).
5.  **Return:** Return the 3x3 output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Determine the reference column of the input grid (3 from the right edge)
    reference_col = input_grid.shape[1] - 3

    # Iterate through all positions in the output grid
    for row in range(3):
        for col in range(3):
            # Calculate the corresponding position in the input grid
            input_row = row
            input_col = reference_col + col - 1

            # Check if the input_col is within the bounds of input_grid
            if 0 <= input_row < input_grid.shape[0] and 0 <= input_col < input_grid.shape[1]:
                # Check if the corresponding input pixel is 0
                if input_grid[input_row, input_col] == 0:
                    # Set the output pixel to 2
                    output_grid[row, col] = 2

    return output_grid