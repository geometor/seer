"""
Divide the input grid into contiguous, non-overlapping 3x3 subgrids. For each row, iterate through the 3x3 subgrids. From each 3x3 subgrid, extract the pixel from the first column of the subgrid, which shares the row index with the output. Place the extracted pixel into the output grid, maintaining the relative spatial arrangement of the subgrids.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height
    output_width = input_width // 3
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for i in range(output_height):
        for j in range(output_width):
            # Extract pixel from the first column of the corresponding 3x3 subgrid
            output_grid[i, j] = input_grid[i , j * 3]

    return output_grid