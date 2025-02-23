# 1f85a75f • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Target Region:** Locate the contiguous block of pixels with the color value 4 (yellow) within the input grid.
2.  **Determine Boundaries:** Find maximal x and y for color 4 in input.
3. **Create Output:** create a 3x3 output grid, using x,y coordinate from last step as the top-left corner.
4. **Fill values:** copy cells from input to output, for cells where x,y is outside of the input grid, use 0.
"""

import numpy as np

def get_bounding_box(grid, color):
    # Find coordinates of the specified color
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None, None, None, None

    #find min and max
    min_y, min_x = coords.min(axis=0)
    max_y, max_x = coords.max(axis=0)

    return min_x, min_y, max_x, max_y

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the bounding box for color 4 (yellow)
    min_x, min_y, max_x, max_y = get_bounding_box(input_grid, 4)

    if min_x is not None:
      #copy values to output
      for y in range(3):
        for x in range(3):
          in_y = min_y + y
          in_x = min_x + x

          if 0 <= in_y < input_grid.shape[0] and 0 <= in_x < input_grid.shape[1]:
            output_grid[y,x] = input_grid[in_y, in_x]

    return output_grid
```
