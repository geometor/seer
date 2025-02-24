"""
The transformation rule takes each non-zero pixel in the input grid and replicates it diagonally downwards and to the right. The output grid is twice the size of the input grid (e.g. 3x3 input becomes 6x6 output).  The non-zero pixels from the input are copied to the output at the original location and then shifted one row down and one column right, repeating this shift until the boundary of output grid reached.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid with double the dimensions of the input_grid, filled with zeros.
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # iterate through each cell of the input_grid.
    for i in range(rows):
        for j in range(cols):
            # if the cell value is not 0 (not an empty cell).
            if input_grid[i, j] != 0:
                # replicate the pixel's value diagonally downwards and to the right.
                value = input_grid[i, j]
                for k in range(min(rows*2-i,cols*2-j)):
                    output_grid[i + k, j + k] = value

    return output_grid