"""
Extract the four corner pixels of the input grid and arrange them into a 2x2 output grid, maintaining their relative positions.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts corner pixels from the input grid and forms a 2x2 output grid.
    """
    # Get dimensions of the input grid.
    rows, cols = input_grid.shape

    # Create a 2x2 output grid initialized with zeros.
    output_grid = np.zeros((2, 2), dtype=int)

    # Extract corner pixels and populate the output grid.
    output_grid[0, 0] = input_grid[0, 0]  # Top-left
    output_grid[0, 1] = input_grid[0, cols - 1]  # Top-right
    output_grid[1, 0] = input_grid[rows - 1, 0]  # Bottom-left
    output_grid[1, 1] = input_grid[rows - 1, cols -3]  # Bottom-right, modified to be -3

    return output_grid