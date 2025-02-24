"""
1.  **Identify:** Find the column index where every cell is blue (value 1).
2.  **Checkerboard Prep:** Create an output array with dimensions based on the input height and output width of three, and initialize all elements to 0 (white).
3.  **Recolor:** For all elements detected in step one, change their value to 8 (azure).
4.  **Checkerboard Pattern:** Apply a checkerboard to output. If the row is even, output an azure pixel in column three. If the row is odd, output an azure pixel in the first column.
5.  **Output:** Return the modified 3-column wide output grid.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find a vertical line of the specified color
    for col in range(grid.shape[1]):
        if np.all(grid[:, col] == color):
            return col
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    # initialize output grid
    output_height = input_grid.shape[0]
    output_width = 3
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Find the vertical line of blue (1) pixels
    blue_column_index = find_vertical_line(input_grid, 1)

    if blue_column_index != -1:
      # checkerboard
      for row in range(output_height):
          if (row % 2) == 0:
              output_grid[row, 2] = 8
          else:
              output_grid[row, 0] = 8

    return output_grid