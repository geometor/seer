"""
Extracts the bottom-left 2x2 subgrid of the input to create the output.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the bottom-left 2x2 subgrid of the input grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The 2x2 subgrid from the bottom-left corner.
    """
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Extract the bottom-left 2x2 subgrid.
    output_grid = input_grid[rows-2:rows, 0:2]

    return output_grid