"""
The input grid is transformed into an output grid where each column is repeated three times, and within that repeated block, there is also a horizontal duplication of colors.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid based on expansion factors.
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 3, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through each column of the input grid.
    for j in range(input_width):
        # Get the current column.
        column = input_grid[:, j]

        # Repeat the column three times vertically.
        repeated_column = np.concatenate([column, column, column])

        # Iterate through the expanded column
        for i in range(output_height):
          # Get the color
          color = repeated_column[i]

          # Duplicate horizontally
          output_grid[i, j*2] = color
          output_grid[i, j*2 + 1] = color


    return output_grid