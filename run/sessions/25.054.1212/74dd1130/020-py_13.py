"""
1.  **Identify Stable Elements:** Locate all blue (1) pixels. Their positions in the output grid remain identical to their positions in the input grid.

2.  **Horizontal swap:** For each row, locate the magenta(6) cell and swap it's value with the red (2) value cell in that row that is on the opposite horizontal end of the grid.
    For example, if the magenta is at postion (0,2), swap with the red at postion (0,0)
"""

import numpy as np

def get_blue_pixels(grid):
    # find the coordinates of all blue pixels (value 1)
    blue_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
          if pixel == 1:
            blue_pixels.append((row_index, col_index))
    return blue_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows = len(input_grid)
    cols = len(input_grid[0])

    # find and set blue pixels
    blue_pixels = get_blue_pixels(input_grid)
    for row, col in blue_pixels:
      output_grid[row][col] = 1

    # Horizontal swap
    for row_index in range(rows):
      magenta_col = -1
      red_col = -1
      for col_index in range(cols):
        if input_grid[row_index][col_index] == 6:
            magenta_col = col_index
        if input_grid[row_index][col_index] == 2:
           if red_col == -1:
            red_col = col_index
           else:
            if col_index > red_col:
              if magenta_col < red_col:
                red_col = col_index
            elif col_index < red_col:
              if magenta_col > red_col:
                red_col = col_index

      if magenta_col != -1 and red_col !=-1:
        if magenta_col < red_col:
          output_grid[row_index][0] = 6 #left most
          output_grid[row_index][cols-1] = 2
        else:
          output_grid[row_index][0] = 2 #left most
          output_grid[row_index][cols-1] = 6 #right most

    return output_grid