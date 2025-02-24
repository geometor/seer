"""
1.  Find the Blue Column: Identify the index (`j`) of the column in the input grid that contains the value '1' (blue).
2.  Determine Output Dimensions:
    *   The output grid has the same height as the input grid.
    *   The output grid's width is calculated as: `input_width` - `j`.
3.  Create Output Grid: Initialize an output grid filled with '0' (white) with the calculated dimensions.
4.  Transform Pixels: Iterate through each cell of the input grid:
    *   If a cell's value is '1' (blue):
        *   Place a '3' (green) in the output grid at the same row and in the last column ( output_width -1 ).
    *   All other input values are discarded. The output grid remains '0' where no '1' was found in the corresponding input row.
"""

import numpy as np

def find_blue_column(grid):
    # Iterate through columns to find the one containing '1'
    for j in range(grid.shape[1]):
        if 1 in grid[:, j]:
            return j
    return -1  # Return -1 if no column contains '1'

def transform(input_grid):
    # Find the column index containing '1's
    blue_column_index = find_blue_column(input_grid)

    # Handle the case where no '1' is found (should not normally occur in valid tasks)
    if blue_column_index == -1:
        return np.zeros_like(input_grid)

    # Determine output grid dimensions
    output_height = input_grid.shape[0]
    output_width = input_grid.shape[1] - blue_column_index

    # Initialize output grid with zeros
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through the input grid and transform '1's to '3's in the output grid
    for i in range(input_grid.shape[0]):
        if 1 in input_grid[i, :]:
            if input_grid[i, blue_column_index] == 1:
              output_grid[i, output_width - 1] = 3
            

    return output_grid