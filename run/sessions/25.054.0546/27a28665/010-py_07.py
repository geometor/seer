"""
Examine the corners of the input grid. Count how many corner pixels are not black (value != 0). Create a 1x1 output grid where the single pixel's value is equal to the count, using the corresponding color for the count.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by counting non-black pixels at the corners and returning the count as a 1x1 grid.
    """
    # Initialize count
    count = 0

    # Get grid dimensions
    rows, cols = input_grid.shape

    # Check corners for non-black (value != 0)
    if input_grid[0, 0] != 0:
        count += 1
    if input_grid[0, cols - 1] != 0:
        count += 1
    if input_grid[rows - 1, 0] != 0:
        count += 1
    if input_grid[rows - 1, cols - 1] != 0:
        count += 1

    # Create output grid (1x1 with the count as the pixel value)
    output_grid = np.array([[count]])

    return output_grid