"""
Divide the input grid into contiguous, non-overlapping 3x3 subgrids. For each 3x3 subgrid, extract the color of the top-left pixel in that subgrid. Place the extracted pixel in the output grid, maintaining the relative spatial arrangement of the subgrids.
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
            # Extract top-left pixel from the corresponding 3x3 subgrid
            output_grid[i, j] = input_grid[i , j * 3]

    return output_grid