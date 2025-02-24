"""
Transforms a 1xN input grid into an MxN output grid where non-zero values in the input expand into
growing squares, and zero values remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with zeros.  The height is determined by counting non-zero elements.
    input_grid = np.array(input_grid)
    num_nonzero = np.count_nonzero(input_grid)
    output_grid = np.zeros((num_nonzero, input_grid.shape[1]), dtype=int)

    # Iterate through the input row
    for j in range(input_grid.shape[1]):
        if input_grid[0, j] != 0:
            # Find how many non-zero values are there to the left.
            non_zero_count = np.count_nonzero(input_grid[0, :j+1])
            # Expand non-zero values into squares.
            for i in range(non_zero_count):
                output_grid[i, j:j + non_zero_count-i] = input_grid[0, j]
        else:
            # Copy zero values directly.
            for i in range(num_nonzero):
                output_grid[i, j] = input_grid[0, j]
    return output_grid