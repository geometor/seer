"""
The transformation takes the input grid, inverts the positions of pixels across both axes (effectively rotating it 180 degrees), and creates the output, preserving pixel colors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 3x3 input grid into a 3x3 output grid.
    The transformation inverts and mirrors the input across both axes
      while preserving the colors of the pixels.

    Args:
        input_grid (list of lists): A 3x3 grid represented as a list of lists.

    Returns:
        list of lists: The transformed 3x3 grid.
    """
    # Initialize the output grid as a 3x3 matrix filled with zeros
    output_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    n = len(input_grid)

    # Iterate through each cell of the input grid
    for i in range(n):
        for j in range(n):
            # Calculate the new indices by swapping across both diagonals
            new_i = n - 1 - j
            new_j = n - 1 - i

            # Assign colors of input pixels to the output pixels
            output_grid[new_i][new_j] = input_grid[i][j]

    return output_grid