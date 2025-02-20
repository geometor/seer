"""
Transformation Rule: Within each column, move all non-zero cells to the bottom, maintaining their original relative order. Fill the remaining upper cells in each column with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a column-wise gravity effect.
    Non-zero elements "fall" to the bottom, preserving their relative order.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)  # Convert to NumPy array
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)  # Initialize output with zeros

    # Iterate over each column
    for j in range(cols):
        # Get the non-zero elements in the current column
        non_zero_elements = [input_grid[i, j] for i in range(rows) if input_grid[i, j] != 0]

        # Fill the bottom of the output column with the non-zero elements
        for k, value in enumerate(non_zero_elements):
            output_grid[rows - len(non_zero_elements) + k, j] = value

    return output_grid.tolist() # Convert back to list of lists