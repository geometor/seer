"""
1. **Calculate Output Dimensions**:
   *  Output grid width = Input grid width + Input grid Height
   * Output grid height = Input grid width + Input grid Height

2.  **Iterate and Replicate/Insert**:
    * Loop through input rows and columns
       * insert value in output[row][col]
       * if row + 1 < output height, insert 8 in output[row+1][col]
       * If col + 1 < output width, insert 8 in output [row][col + 1]
       * If row + 1 < output height and col + 1 < output width insert 8 in output [row+1][col+1]
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    input_height = input_grid.shape[0]
    input_width = input_grid.shape[1]

    # Calculate output dimensions.
    output_height = input_height + input_width
    output_width = input_height + input_width

    # Initialize output_grid with 8s.
    output_grid = np.full((output_height, output_width), 8, dtype=int)

    # Iterate through the input grid and replicate/insert values.
    for row in range(input_height):
        for col in range(input_width):
            output_grid[row][col] = input_grid[row][col]
            if row + 1 < output_height:
                output_grid[row + 1][col] = 8
            if col + 1 < output_width:
                output_grid[row][col + 1] = 8
            if row + 1 < output_height and col + 1 < output_width:
                output_grid[row + 1][col + 1] = 8


    return output_grid