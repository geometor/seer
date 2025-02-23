# a64e4611 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Red Shapes:** Locate all red (2) pixels in the input grid. These pixels form non-contiguous, scattered shapes.

2.  **Determine Bounding Rectangle:** Find the smallest rectangle that can enclose most part of red color, starting from the top-left corner (0,0). We'll can define this rectangle by its top-left and bottom-right corner coordinates. In fact, the green filling is done from (0,0), while the area is limited by red shapes from left, right and top.

3.  **Fill with Green:** Change all white (0) pixels within a bounding rectangle limited by red color to green (3), until the red color pixels from the input.
"""

import numpy as np

def find_red_pixels(grid):
    """Finds the coordinates of all red pixels in the grid."""
    red_pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel == 2:
                red_pixels.append((row_idx, col_idx))
    return red_pixels

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    red_pixels = find_red_pixels(input_grid)
    
    #find limits of red pixels
    max_row = input_grid.shape[0]
    max_col = input_grid.shape[1]

    # Fill with green (3) from top-left corner
    for r in range(max_row):
        for c in range(max_col):
            if output_grid[r,c] == 0: # Check if it's white
                output_grid[r,c] = 3 #Paint in green
            if output_grid[r,c] == 2:
                continue #If red, stop painting

    return output_grid
```
