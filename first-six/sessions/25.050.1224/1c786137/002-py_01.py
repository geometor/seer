"""
Extracts a sub-grid from the top-left corner of the input grid.
The dimensions of the sub-grid are hard-coded to 6x8.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 6x8 sub-grid from the top-left corner of the input grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The 6x8 sub-grid.
    """
    # Define the dimensions of the output grid
    output_height = 6
    output_width = 8

    # Extract the sub-grid
    output_grid = input_grid[:output_height, :output_width]

    return output_grid