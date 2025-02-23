"""
The input grid is transformed into an output grid of the same dimensions. All pixels in the output grid are assigned the color green (value 3), regardless of the input grid's pixel values.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing all pixel values with 3 (green).

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid, with all pixels set to 3.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Set all pixels in the output grid to 3.
    output_grid[:] = 3

    return output_grid