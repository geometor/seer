"""
Swap the values of the pixels at positions (0, 0) and (0, 1) in the input grid if both are non-zero.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping the values of two specific pixels.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed grid.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = [row[:] for row in input_grid]

    # Check if the values at (0, 0) and (0, 1) are non-zero
    if output_grid[0][0] != 0 and output_grid[0][1] != 0:
        # Swap the values
        output_grid[0][0], output_grid[0][1] = output_grid[0][1], output_grid[0][0]

    return output_grid