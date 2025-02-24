"""
1.  **Locate Center:** Find the coordinates of the single pixel with the value '1' (blue) in the input grid.
2.  **Fill Background:** Replace all '0' (white) pixels in the input grid with '8' (azure). This creates the background for the output.
3. **Create Cross:**
   * Using the coordinates of the located '1' (the center) from step 1:
   * Along the x-axis (row), starting at the center coordinate and extending outwards in both directions:
      Alternate by placing first an 8 then a 1.
   * Along the y-axis (column), starting at the center coordinate and extending outwards in both directions:
        Alternate by placing first a 1 then an 8.
"""

import numpy as np

def find_object(grid, value):
    # finds all instances of value and returns coordinates
    coords = np.where(grid == value)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # initialize output_grid
    output_grid = np.full(input_grid.shape, 8)

    # find the location of the 1
    one_locations = find_object(input_grid, 1)
    if not one_locations:  # Handle edge case with no 1 present.
       return output_grid
       
    one_row, one_col = one_locations[0]

    # construct cross with alternating values
    # horizontal
    output_grid[one_row, one_col] = 1
    for i in range(one_col + 1, output_grid.shape[1]):
        output_grid[one_row, i] = 8 if (i - one_col) % 2 != 0 else 1
    for i in range(one_col - 1, -1, -1):
        output_grid[one_row, i] = 8 if (one_col - i) % 2 != 0 else 1

    # vertical
    for i in range(one_row + 1, output_grid.shape[0]):
        output_grid[i, one_col] = 1 if (i - one_row) % 2 != 0 else 8
    for i in range(one_row - 1, -1, -1):
        output_grid[i, one_col] = 1 if (one_row - i) % 2 != 0 else 8

    return output_grid