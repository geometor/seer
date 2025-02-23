"""
The transformation operates on each column independently. It identifies the non-zero elements (colored blocks) within each column of the input grid. These non-zero elements are then moved to the bottom of the corresponding column in the output grid, maintaining their original vertical order. The remaining cells at the top of the column in the output grid are filled with zeros (white color).
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