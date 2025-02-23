"""
1.  **Iterate:** Go through each column of the input grid one by one.
2.  **Collect:** For the current column, identify and collect all the non-zero pixels, noting their original row order.
3.  **Stack:** In the corresponding column of the output grid, place these collected non-zero pixels starting from the *bottom* row, going upwards. Maintain the original row order from the input.
4.  **Fill:** Fill any remaining empty cells at the top of the output column with zeros.
5.  **Repeat:** Repeat steps 2-4 for all columns in the input grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with zeros and same dimensions as input.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column
    for c in range(cols):
        # Collect non-zero pixels and their row indices in the current column
        non_zero_pixels = []
        for r in range(rows):
            if input_grid[r, c] != 0:
                non_zero_pixels.append((r, input_grid[r, c]))

        # Stack non-zero pixels at the bottom of the corresponding output column
        output_row = rows - 1
        for _, value in reversed(non_zero_pixels):  # Iterate in reverse order to stack
            output_grid[output_row, c] = value
            output_row -= 1

    return output_grid