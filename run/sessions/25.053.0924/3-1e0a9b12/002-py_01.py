"""
Extracts all non-zero values from the input, preserves their order, and 
places them sequentially in the last row of the output grid. The rest of 
the output grid is filled with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the last row,
    preserving their order, and filling the rest of the grid with zeros.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed grid.
    """
    # Initialize the output grid with the same shape and data type as the input
    output_grid = np.zeros_like(input_grid)

    # Extract non-zero elements from the input grid
    non_zero_elements = input_grid[input_grid != 0]

    # Place the non-zero elements in the last row of the output grid
    output_grid[-1, :len(non_zero_elements)] = non_zero_elements

    return output_grid