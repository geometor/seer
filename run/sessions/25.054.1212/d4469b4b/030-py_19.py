"""
The input is a 5x5 grid, and the output is a 3x3 grid. Each output pixel corresponds to a 3x3 region in the input, centered at (i+1, j+1). If the center pixel of the input region is non-zero, the output pixel is grey (5); otherwise, it's white (0).
"""

import numpy as np

def get_region(input_array, row, col):
    """Extracts a 3x3 region from the input array centered at (row, col)."""
    row_start = max(0, row - 1)
    row_end = min(input_array.shape[0], row + 2)
    col_start = max(0, col - 1)
    col_end = min(input_array.shape[1], col + 2)
    return input_array[row_start:row_end, col_start:col_end]

def transform(input_grid):
    """Transforms a 5x5 input grid to a 3x3 output grid based on center pixel of a 3x3 region."""

    input_array = np.array(input_grid)
    output_array = np.zeros((3, 3), dtype=int)

    # Iterate through the 3x3 output grid
    for i in range(3):
        for j in range(3):
            # Calculate the center coordinates in the input grid
            input_row = i + 1
            input_col = j + 1

            # Get the 3x3 region centered at the corresponding input pixel
            # region = get_region(input_array, input_row, input_col)  # Not needed, we just want the center pixel

            # Check if the center pixel in the region is within bounds and not 0.
            if 0 <= input_row < input_array.shape[0] and 0 <= input_col < input_array.shape[1]:  # Check Bounds
                if input_array[input_row, input_col] != 0:
                    output_array[i, j] = 5  # Set output to grey (5)
                else:
                    output_array[i, j] = 0  # Set output to white (0)
            else:
                output_array[i,j] = 0 # if out of bounds, we make the output pixel white

    return output_array.tolist()