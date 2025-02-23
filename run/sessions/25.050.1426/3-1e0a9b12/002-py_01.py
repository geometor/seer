"""
The transformation operates column by column. For each column in the input grid, identify all the non-zero color values.  Then, in the output grid, populate the same column from bottom to top with these identified non-zero color values in the same order they appeared in the input column. Fill the remaining cells in the top rows of the output column with the color white (0). This effectively pushes all colored blocks in each column to the bottom.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by pushing all non-zero values in each column to the bottom.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate over each column
    for j in range(cols):
        # Extract non-zero values from the current column
        non_zero_values = input_grid[:, j][input_grid[:, j] != 0]
        # Calculate the starting row index for placing non-zero values
        start_row = rows - len(non_zero_values)
        # Place the non-zero values at the bottom of the output column
        output_grid[start_row:, j] = non_zero_values

    return output_grid.tolist()