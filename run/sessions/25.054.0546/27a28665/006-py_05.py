"""
Counts the total number of pixels on both diagonals of the input grid, avoiding double-counting the center pixel if it lies on both diagonals.
"""

import numpy as np

def transform(input_grid):
    """
    Counts pixels on both diagonals, handling the center pixel correctly.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Initialize the count.
    count = 0

    # Count pixels on the main diagonal.
    for i in range(min(rows, cols)):
        count += 1

    # Count pixels on the anti-diagonal.
    for i in range(min(rows, cols)):
        count += 1

    # Adjust count for the center pixel in grids with odd dimensions.
    if rows % 2 != 0 and cols % 2 !=0 and rows == cols:
        count -= 1

    # Create the 1x1 output grid.
    output_grid = np.array([[count]])

    return output_grid