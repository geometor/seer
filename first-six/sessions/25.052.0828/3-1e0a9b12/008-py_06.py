"""
The transformation involves moving all non-zero colored cells to the bottom of their respective columns,
stacking them while maintaining their original order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the bottom of their respective columns,
    stacking them while maintaining their original order.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column
    for j in range(cols):
        # Find non-zero elements in the column
        non_zero_indices = np.nonzero(input_grid[:, j])[0]
        # If there are any non-zero elements
        if non_zero_indices.size > 0:
            # Move them to the bottom, maintaining order
            for i, row_index in enumerate(reversed(non_zero_indices)):
                output_grid[rows - 1 - i, j] = input_grid[row_index, j]

    return output_grid