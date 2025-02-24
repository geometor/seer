"""
The input grid (3x6) is transformed into an output grid (3x3). Non-white pixels (yellow/4 and green/3) in the input are replaced by magenta (6) in the output. White (0) pixels remain unchanged. The transformation is performed by reducing the input grid column-wise: two input columns condense into one output column. If either of the two columns contains a non-white pixel, the output is magenta.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with dimensions 3x3, filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through columns of the output grid
    for out_col in range(3):
        # Corresponding columns in the input grid
        in_col1 = out_col * 2
        in_col2 = out_col * 2 + 1

        # Iterate through rows
        for row in range(3):
            # Check if either corresponding input pixel is non-white
            if (input_grid[row, in_col1] != 0) or (input_grid[row, in_col2] != 0):
                output_grid[row, out_col] = 6  # Set output pixel to magenta (6)
            # else output is white.

    return output_grid