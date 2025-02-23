"""
1.  **Identify Objects:** Locate all pixels in the input grid that have a non-zero value (i.e., are not white/0). Consider each of these colored pixels as an individual object.

2.  **Conditional Extension:**
    *   If an object is blue (1), add orange (7) pixels to its immediate left, right, and below, if those positions are currently white (0).
    *   If an object is red (2), add yellow (4) pixels to its immediate top, and to the left and the right if those positions are currently white (0).
    *   If the object is magenta(6), do nothing

3.  The rest of the white(0) cells stay white(0)
"""

import numpy as np

def get_objects(grid):
    """Finds all non-zero pixels and returns their coordinates and values."""
    objects = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                objects.append(((r, c), value))
    return objects

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    objects = get_objects(input_grid)

    # Iterate through identified objects
    for (row, col), value in objects:
      # Conditional Extension
      if value == 1: # Blue
          #add orange(7) on the left, right and below,
          if col > 0 and output_grid[row, col - 1] == 0:
              output_grid[row, col - 1] = 7
          if col < output_grid.shape[1] - 1 and output_grid[row, col + 1] == 0:
              output_grid[row, col + 1] = 7
          if row < output_grid.shape[0] - 1 and output_grid[row + 1, col] == 0:
            output_grid[row+1,col] = 7
      elif value == 2:  # Red
            # Add yellow (4) above and below.
            if row > 0 and output_grid[row - 1, col] == 0:
                output_grid[row - 1, col] = 4
            if col > 0 and output_grid[row, col-1] == 0:
              output_grid[row,col-1] = 4
            if col < output_grid.shape[1] -1 and output_grid[row, col+1] == 0:
              output_grid[row, col+1] = 4

    return output_grid