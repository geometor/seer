"""
1.  **Identify the central horizontal line:** Locate the middle row of the 3x3 grid.
2.  **Check for azure:** Iterate through the pixels on this central line.
3.   **Change Azure to Grey:** If a pixel on the central line is azure (8), change it to gray (5).
4.  **Preserve other colors:** All other pixels, specifically the red (2) ones, and those not on the central line, remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # get the height of the grid.
    height = output_grid.shape[0]

    # Identify the central horizontal line (middle row).
    middle_row = height // 2

    # Iterate through the pixels on the central line.
    for x in range(output_grid.shape[1]):
      #Change Azure to Grey
      if output_grid[middle_row, x] == 8:
          output_grid[middle_row, x] = 5

    # Preserve all other colors and return
    return output_grid