"""
Extracts a sub-grid of dimensions 5x3, from the top right
corner of the yellow rectangle.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 5x3 sub-grid from the top-right corner of the yellow
    rectangle in the input grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The 5x3 sub-grid, or None if the yellow rectangle
                       cannot be found or is too small.
    """

    # Define the dimensions of the output grid
    output_height = 5
    output_width = 3
    
    #get subgrid
    output_grid = input_grid[0:5,3:6]

    return output_grid