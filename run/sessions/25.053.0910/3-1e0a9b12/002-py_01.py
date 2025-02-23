"""
1. Identify all non-zero pixels in the input grid.
2. Move all the non-zero pixels to the last row of the output grid.
3. Sort the non-zero pixels in the last row of the output in ascending order, from left to right.
4. Fill all other cells in the output grid with zeros.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by moving and sorting non-zero pixels to the last row."""

    # Initialize the output grid with the same dimensions as the input, filled with zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Extract all non-zero pixel values.
    non_zero_pixels = [pixel for pixel in input_grid.flatten() if pixel != 0]

    # Sort the non-zero pixels in ascending order.
    non_zero_pixels.sort()

    # Place the sorted non-zero pixels in the last row of the output grid.
    for i, pixel in enumerate(non_zero_pixels):
        if i < cols: # prevent out of bounds on test cases
            output_grid[rows - 1, i] = pixel

    return output_grid