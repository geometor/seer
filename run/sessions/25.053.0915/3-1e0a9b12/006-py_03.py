"""
1.  **Clear Top Rows:** Set all pixels in the top two rows (row indices 0 and 1) of the output grid to 0 (white).
2.  **Shift Down:** For the remaining rows (starting from row index 2) copy every non-zero pixel from the input grid to the output grid, but shift each one down to fill the empty space from top to down. The non-zero pixels must maintain its column.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.zeros_like(input_grid)

    # Shift down: Iterate through columns
    for col in range(input_grid.shape[1]):
        # Extract non-zero pixels from the input column, rows 2 and below
        non_zero_pixels = []
        for row in range(2, input_grid.shape[0]):
            if input_grid[row, col] != 0:
                non_zero_pixels.append(input_grid[row, col])

        # append non-zero pixel from rows 0,1 and 2.
        for row in range(0, 2):
            if input_grid[row, col] != 0:
                non_zero_pixels.append(input_grid[row, col])

        # Fill the output column, starting from row 2, with the extracted pixels
        output_row = 2
        for pixel_value in non_zero_pixels:
            if output_row < output_grid.shape[0]:
                output_grid[output_row, col] = pixel_value
                output_row += 1

    return output_grid