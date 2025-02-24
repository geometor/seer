"""
The input grid is expanded into a 9x9 grid. The connected region of green (3) pixels in the input is identified.
This green region is then replicated to form four quadrants within the output grid, where each quadrant corresponds to a scaled green area of the same dimension as input.
The remaining cells in the output grid are filled with white (0) pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 9x9 array filled with white (0).
    output_grid = np.zeros((9, 9), dtype=int)

    # Get the dimensions of the input grid.
    input_rows, input_cols = input_grid.shape

    # Iterate through the input grid to find green pixels.
    for i in range(input_rows):
        for j in range(input_cols):
            if input_grid[i, j] == 3:  # Check for green pixel
                # Calculate the corresponding quadrant coordinates in the output grid.
                for row_mult in range(3):
                    for col_mult in range(3):
                      output_grid[i + row_mult * input_rows, j + col_mult* input_cols] = 3

    return output_grid