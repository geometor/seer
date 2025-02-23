# 5-150deff5 • 006 • example_3 - CODE

---
```python
"""
1.  Identify the contiguous shape composed of grey (5) pixels in the input grid.
2.  Divide this shape vertically. The leftmost segment is one column of the height of GreyShape.
3.  Redraw each segment on output grid.
4.  Change the color of leftmost segment to red (2).
5.  Change the color of rest of segment to azure (8).
6.  Leave all other pixels in the output grid as black (0).
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of all pixels with the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None
    return coords

def get_object_bounds(coords):
    # Get the bounding box of an object
    min_row = np.min(coords[:, 0])
    max_row = np.max(coords[:, 0])
    min_col = np.min(coords[:, 1])
    max_col = np.max(coords[:, 1])
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find the grey object.
    grey_coords = find_object(input_grid, 5)
    if grey_coords is None:
        return output_grid

    # get grey object bounds
    min_row, max_row, min_col, max_col = get_object_bounds(grey_coords)
    
    # divide this shape vertically
    # change color of segment to red
    for row in range(min_row, max_row + 1):
        output_grid[row, min_col] = 2

    # change color of rest of the segments to azure
    for row in range(min_row, max_row + 1):
      for col in range(min_col+1, max_col + 1):
          if input_grid[row, col] == 5:
            output_grid[row, col] = 8
    
    return output_grid
```
