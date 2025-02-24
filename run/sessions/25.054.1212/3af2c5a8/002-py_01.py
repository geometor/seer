"""
The input grid's dimensions are doubled to create the output grid (height x2, width x2).
Azure (8) pixel location in input is replicated at four different locations in output grid.
If we consider the output grid is divided in 2x2 subgrids.
The azure (8) pixels are present at the bottom right cell in 2x2 subgrid that corresponds to its position in input grid.
The remaining azure (8) pixels are present at the top left cell in adjacent 2x2 subgrids in output.
All other cells in the output grid, not occupied by azure, are filled with white (0).
"""

import numpy as np

def transform(input_grid):
    # Double Dimensions: The input grid's dimensions are doubled.
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through the input grid.
    for i in range(input_height):
        for j in range(input_width):
            # Replicate and Offset for azure (8) pixels.
            if input_grid[i, j] == 8:
                # place one azure pixel in bottom right of the corresponding 2x2 sub grid
                output_grid[2*i+1, 2*j+1] = 8

                # place one azure pixel in top left of adjacent 2x2 sub grids
                if j+1 < input_width:
                  output_grid[2*i,2*j+2] = 8

                if i + 1 < input_height:
                  output_grid[2*i+2,2*j] = 8


    return output_grid