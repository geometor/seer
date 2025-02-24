"""
Create a border of 8s around a central rectangular region of 0s. The central region's dimensions are calculated as the input grid's dimensions minus 2 in each direction.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by creating a border of 8s and a central rectangle of 0s.

    Args:
        input_grid: A numpy array representing the input grid.

    Returns:
        A numpy array representing the transformed grid.
    """
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Create an output grid of the same size, initialized with 8s.
    output_grid = np.full((rows, cols), 8)

    # Calculate the dimensions of the inner rectangle.
    inner_rows = rows - 2
    inner_cols = cols - 2

    # Iterate through the inner rectangle and set values to 0.
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            output_grid[i, j] = 0

    return output_grid