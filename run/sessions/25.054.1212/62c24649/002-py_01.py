"""
Duplicate the input grid, doubling its dimensions. Each pixel in the input becomes a 2x2 block in the output.
Add a one-pixel border around the duplicated grid, using edge values of the original input.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    input_height, input_width = input_grid.shape

    # Calculate output grid dimensions
    output_height = input_height * 2 + 2
    output_width = input_width * 2 + 2

    # Initialize output grid with zeros
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Duplicate the input grid into the center of the output grid
    for i in range(input_height):
        for j in range(input_width):
            output_grid[2*i+1, 2*j+1] = input_grid[i, j]
            output_grid[2*i+1, 2*j+2] = input_grid[i, j]
            output_grid[2*i+2, 2*j+1] = input_grid[i, j]
            output_grid[2*i+2, 2*j+2] = input_grid[i, j]

    # Add the border
    # Top and Bottom
    for j in range(input_width):
      output_grid[0, 2*j+1] = input_grid[0,j]
      output_grid[0, 2*j+2] = input_grid[0,j]
      output_grid[-1, 2*j+1] = input_grid[-1,j]
      output_grid[-1, 2*j+2] = input_grid[-1,j]
    # Left and Right
    for i in range(input_height):
      output_grid[2*i+1, 0] = input_grid[i,0]
      output_grid[2*i+2, 0] = input_grid[i,0]
      output_grid[2*i+1, -1] = input_grid[i,-1]
      output_grid[2*i+2, -1] = input_grid[i,-1]
    return output_grid