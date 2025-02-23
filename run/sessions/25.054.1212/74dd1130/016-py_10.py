"""
The output grid is the same size as the input grid (3x3).
The first row of the output grid is obtained by rotating the first row of input to the left by 1 position.
The second and third rows of the output grid are derived by swapping the first and last element.
"""

import numpy as np

def rotate_left(arr, n):
    """Rotates a 1D numpy array to the left by n positions."""
    n = n % len(arr)  # Handle rotations larger than array length
    return np.concatenate((arr[n:], arr[:n]))

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Rotate the first row to the left by 1 position
    output_grid[0] = rotate_left(input_grid[0], 1)

    # Swap the first and last elements of the second and third rows
    for i in range(1, len(input_grid)):
        if len(input_grid[i]) > 1: #ensure that rows have at least 2 elements before swapping
            output_grid[i, 0], output_grid[i, -1] = input_grid[i, -1], input_grid[i, 0]

    return output_grid