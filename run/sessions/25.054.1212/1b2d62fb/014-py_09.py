"""
1.  **Identify the Target:** Locate the vertical line of blue (1) pixels in the input grid. It's in the center (column 4).
2.  **Extract:** extract the column where all the values are equal to one
3.  **Resize/Compress:** Reduce the width of the extracted column to three. Place the column in the center
4.  **Recolor:** Change all blue (1) pixels in the extracted area to azure (8).
5.  **Fill Remaining:** Fill all other cells in output with the color white (0).
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find a vertical line of the specified color
    for col in range(grid.shape[1]):
        if np.all(grid[:, col] == color):
            return col
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    # Find the vertical line of blue (1) pixels
    blue_column_index = find_vertical_line(input_grid, 1)

    # initialize output grid
    output_height = input_grid.shape[0]
    output_width = 3
    output_grid = np.zeros((output_height, output_width), dtype=int)

    if blue_column_index != -1:
      # Extract the blue column
      blue_column = input_grid[:, blue_column_index]

      # Recolor the blue column to azure (8)
      blue_column[blue_column == 1] = 8
      
      # place in the center of output
      output_grid[:, 1] = blue_column


    return output_grid