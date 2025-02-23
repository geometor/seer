"""
1.  **Identify the "hole"**: Locate the empty (value 0) region within the red (value 2) shape in the input grid. This is the internal space that is not part of the red square's perimeter. It can consist of one or several 0 pixels.
2.  **Find the vertical center**: The new pixels are vertically centered.
3. **Place Green Pixels**: In the output, the center of the hole is made of two green pixels stacked on top of one another. All the red pixels are turned to white pixels.
"""

import numpy as np

def find_hole(grid):
    # Find the bounding box of the red shape
    red_pixels = np.argwhere(grid == 2)
    min_row, min_col = np.min(red_pixels, axis=0)
    max_row, max_col = np.max(red_pixels, axis=0)

    # Iterate within the bounding box and check for 0s that are surrounded by 2s
    for r in range(min_row + 1, max_row):
        for c in range(min_col + 1, max_col):
            if grid[r,c] == 0:
              return (r,c)
    return None

def transform(input_grid):
    # initialize output_grid as a copy of the input grid, changing the type.
    output_grid = np.zeros_like(input_grid)

    # Find center of the 'hole'
    hole_center = find_hole(input_grid)

    if hole_center:
      r,c = hole_center
      output_grid[r,c]=3
      output_grid[r-1,c]=3

    return output_grid