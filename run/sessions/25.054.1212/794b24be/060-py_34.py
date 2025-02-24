"""
1.  **First Row Transformation:** If there are any blue pixels in the input grid, change *all* pixels on the first row of the output grid to red.
2.  **Second Row Transformation:** If there is a blue pixel directly below a blue pixel of the input grid, change the pixel directly below the blue pixel to red.
3. **All Other Pixels:** Pixels not affected by step 1, or step 2 remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # get dimensions of grid
    rows, cols = output_grid.shape

    # 1. First Row Transformation
    has_blue = False
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 1:
            has_blue = True
            break
      if has_blue:
          break

    if has_blue:
        for j in range(cols):
          output_grid[0,j] = 2

    # 2. Second Row Transformation.
    for r in range(rows - 1):
      for c in range(cols):
        if input_grid[r,c] == 1 and input_grid[r+1, c] == 1:
            output_grid[r + 1, c] = 2

    return output_grid