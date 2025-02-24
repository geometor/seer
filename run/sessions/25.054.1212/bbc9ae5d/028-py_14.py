"""
1.  **Iterate** through each pixel of the input grid.
2.  **Check** if the pixel value is non-zero.
3.  **If non-zero:**
    *   Let `value` be the pixel's value.
    *   Calculate `output_height` as `input_height * (value + 1)`.
    *   Expand. For *each* row in the original input grid where there is
    *   Replicate current pixel `value + 1` times horizontally in the output grid. Perform this operation `value + 1` times vertically.
    *  That is, if the original pixel is at `input[row, col]`, and original value is V, output grid will include the same value `value + 1` times horizontally, at rows, `row`, `row + input_height`, `row + 2*input_height`, ..., `row + V*input_height`
4. **If zero:** preserve the pixel in the output grid at the respective expanded positions. Copy the zeros to all vertically stacked output grids.
"""

import numpy as np

def transform(input_grid):
    input_height, input_width = input_grid.shape
    output_height = 0  # Initialize for later determination

    # Find maximum height multiplier
    max_multiplier = 0
    for row in range(input_height):
        for col in range(input_width):
            if input_grid[row, col] != 0:
                max_multiplier = max(max_multiplier, input_grid[row,col] + 1)

    output_height = input_height * max_multiplier
    output_grid = np.zeros((output_height, input_width), dtype=int)

    # Iterate and expand
    for row in range(input_height):
        for col in range(input_width):
            value = input_grid[row, col]
            if value != 0:
                for i in range(value + 1):
                    for j in range(value + 1):
                      output_grid[row + i * input_height, col + j] = value
            else: # value is 0
                for i in range(max_multiplier):
                    output_grid[row + i * input_height, col] = 0


    return output_grid