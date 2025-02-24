"""
Transforms a 1xN input grid into an MxN output grid where non-zero values in the input expand into
growing "squares" (actually triangles), and zero values are copied to all rows. The height M of the
output grid is equal to the number of non-zero values in the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with zeros.
    input_grid = np.array(input_grid)
    num_nonzero = np.count_nonzero(input_grid)
    output_grid = np.zeros((num_nonzero, input_grid.shape[1]), dtype=int)

    # Keep track of number of non-zeros
    non_zero_count = 0

    # Iterate through the input row
    for j in range(input_grid.shape[1]):
        if input_grid[0, j] != 0:
            # Expand non-zero values into growing triangles.
            color = input_grid[0, j]
            for i in range(non_zero_count,num_nonzero):
                row_width = i - non_zero_count + 1
                output_grid[i, j:min(j + row_width,input_grid.shape[1])] = color #stay within bound
            non_zero_count += 1
        else:
            # Copy zero values directly to all rows.
            for i in range(num_nonzero):
                output_grid[i, j] = input_grid[0, j]
    return output_grid