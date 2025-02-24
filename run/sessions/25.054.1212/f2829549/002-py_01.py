"""
Transforms a 7x4 input grid to a 4x3 output grid. The transformation identifies the column containing '1's (blue) in the input, 
changes these '1's to '3's (green) and keeps the same row. Other values ('7' or '5') are discarded. Empty output space is filled with 0.
"""

import numpy as np

def transform(input_grid):
    # Find the column index containing '1's
    column_with_ones = -1
    for j in range(input_grid.shape[1]):
        if 1 in input_grid[:, j]:
            column_with_ones = j
            break

    # Initialize output grid with zeros, based on the column of 1.
    output_grid = np.zeros((input_grid.shape[0], column_with_ones+1), dtype=int)

    # Iterate through the input grid and transform pixels
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == 1:
                # Transform '1' to '3' and place it in the output grid
                output_grid[i, input_grid.shape[1] - (column_with_ones +1 )] = 3

    return output_grid