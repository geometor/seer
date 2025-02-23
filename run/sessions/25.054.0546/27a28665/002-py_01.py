"""
Counts the number of white (0) pixels along the diagonals of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Counts the number of 0s on the diagonals and returns a 1x1 grid with the count.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_array.shape

    # Initialize the count of white (0) pixels on the diagonals.
    count = 0

    # Check the main diagonal (top-left to bottom-right).
    for i in range(min(rows, cols)):
        if input_array[i, i] == 0:
            count += 1

    # Check the anti-diagonal (top-right to bottom-left).
    for i in range(min(rows, cols)):
        if input_array[i, cols - 1 - i] == 0:
            count += 1

    # handle case if both diagonals have 0 on same cell
    if rows % 2 != 0 and input_array[rows // 2, cols // 2] == 0:
       count -= 1
            
    # Create a 1x1 output grid with the final count.
    output_grid = np.array([[count]])

    return output_grid