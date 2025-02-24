"""
The transformation rule is as follows:
1. Copy and Expand: Create a new grid which doubles the height and width from the input grid to new grid.
2. Duplicate Magenta: Copy all the magenta element in the original grid locations in the new grid, then duplicate the magenta pixels at a mirrored location at the right side.
3. Mirror Magenta: Duplicate the expanded top grid, below a solid line of azure.
4. Fill Azure: Add a complete line of azure below the created top grid.
5. Fill Azure: Fill with azure the columns between the two first and between the next two columns in the original grid.
6. Fill Azure: Fill the created structure with azure where ever required.
"""

import numpy as np

def transform(input_grid):
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Duplicate and mirror magenta pixels, and introduce azure.
    for i in range(input_height):
        for j in range(input_width):
            if input_grid[i, j] == 6:
                output_grid[i, j] = 6
                output_grid[i, j + input_width] = 6

    # Fill between magenta columns with azure in the top half.
    magenta_cols = []
    for j in range(output_width) :
        for i in range(output_height) :
            if output_grid[i,j] == 6:
                magenta_cols.append(j)
                break;

    if len(magenta_cols) > 0:
      for j in range(len(magenta_cols)-1):
        cur_col = magenta_cols[j]
        next_col = magenta_cols[j+1]
        if next_col - cur_col > 1:
           for k in range(cur_col+1,next_col):
             for i in range(input_height):
                  output_grid[i,k] = 8

    # Add a complete line of azure.
    output_grid[input_height, :] = 8

    # Mirror the top part of the grid to the bottom.
    for i in range(input_height):
        for j in range(output_width):
            output_grid[output_height - 1 - i, j] = output_grid[i, j]
            if (output_grid[output_height - 1 - i, j] == 8) and (i != input_height-1):
               output_grid[output_height - 1 - i, j] = 0

    return output_grid