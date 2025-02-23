"""
1.  **Identify Target Region:** Define a rectangular region within the grid, starting from column 7 and ending at column 13, spanning all rows.
2.  **Preserve Outside Pixels:** All pixels *outside* of this defined rectangular region in the input grid should be copied directly to the output grid, maintaining their original color values.
3.  **Modify Inside Pixels:** All pixels *inside* the identified rectangular region will be changed to the color green (value 3) in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing a rectangular region to green (3).
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input_grid

    # Define the rectangular region's boundaries
    start_column = 7
    end_column = 13

    # Iterate through each row and modify the specified columns
    for row_index in range(output_grid.shape[0]):
        for col_index in range(start_column, end_column + 1):  # Inclusive range
            output_grid[row_index, col_index] = 3  # Set pixel to green (3)

    return output_grid