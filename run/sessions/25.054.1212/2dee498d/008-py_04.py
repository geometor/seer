"""
Extracts the 4x4 subgrid located at the top-left corner of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the top-left 4x4 subgrid from the input grid.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The 4x4 subgrid.
    """
    # Initialize the output grid as an empty list.
    output_grid = []

    # Iterate through the first 4 rows of the input grid.
    for i in range(4):
        # Extract the first 4 columns of the current row and append to output.
        output_grid.append(input_grid[i][:4])

    return output_grid