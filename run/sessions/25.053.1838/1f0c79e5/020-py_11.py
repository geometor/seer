"""
The transformation rule involves these steps:
1. Identify the Core: Locate the non-zero pixels (the "central cluster") within the input grid.
2. Mirror and Rotate: create a mirrored, rotated version of the non-zero pixels
3. replace: Change all the non-zero pixels in the original to '7'
4. Background: Retain the '0' pixels in the input grid where there were '0' originally
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-zero pixels
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_pixels.append((r, c, input_grid[r,c]))

    # Apply transformation based on mirroring, rotating, and value changes
    for r, c, value in non_zero_pixels:
      output_grid[r,c] = 7
      output_grid[c,rows-1-r] = 7
      output_grid[cols-1-r,rows-1-c] = 7
      output_grid[cols-1-c,r] = 7    
    
    return output_grid