"""
1.  **Iterate** through each pixel in the input grid.
2.  **For each pixel:**
    *   Get the pixel's value (`V`).
    *   If `V` is not zero:
        *   Create a square block of pixels with dimensions (`V` + 1) x (`V` + 1).
        *   Fill this block with the color represented by `V`.
        *   Place this block in the output grid, starting at a row index,
            where the top left block starts on the original row.
            The row blocks begin on multiples of `input_height`.
        *   Place the additional blocks in successive columns.
        * That is, if `input[row,col]` is the original pixel location, put the top left corner of the blocks beginning at `output[row + i * input_height, col + j]` for i and j from 0 to V
    *   If `V` is zero:
        *   Copy the zero value to its original position.
		*	Copy the zeros to vertically stacked output grids.
"""

import numpy as np

def transform(input_grid):
    input_height, input_width = input_grid.shape

    # Find maximum height multiplier
    max_multiplier = 0
    for row in range(input_height):
        for col in range(input_width):
            if input_grid[row, col] != 0:
                max_multiplier = max(max_multiplier, input_grid[row,col] + 1)

    output_height = input_height * max_multiplier
    output_width = input_width + (input_width-1) * (max_multiplier - 1)  # Calculate max possible output width.
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate and expand
    for row in range(input_height):
        for col in range(input_width):
            value = input_grid[row, col]
            if value != 0:
                for i in range(value + 1):
                    for j in range(value + 1):
                        output_row = row + i * input_height
                        output_col = col + j
                         # Check output bounds
                        if output_row < output_height and output_col < output_width:
                            output_grid[output_row, output_col] = value
            else:
                for i in range(max_multiplier):
                    output_row = row + i * input_height
                     # Check output bounds
                    if output_row < output_height and col < output_width :
                        output_grid[output_row, col] = 0

    return output_grid