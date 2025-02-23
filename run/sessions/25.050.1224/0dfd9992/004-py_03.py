"""
The output grid is identical to the input grid, except that all cells with the color value '0' (white) are removed. Every position with color 0 is replaced with the color that occupied that position previously.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing all cells with color 0 with the color that occupied that position before.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find the indices of all cells with color 0.
    #zero_indices = np.where(input_grid == 0)

    # Iterate through the zero-colored cells and replace their values.
    # The new value for these cells are copied from the input grid.

    return output_grid