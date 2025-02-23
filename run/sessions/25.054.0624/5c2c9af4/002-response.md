# 5c2c9af4 • 002 • example_1 • investigate_coder

---
```python
"""
Expands azure (8) pixels in the input grid both vertically and horizontally, creating lines and filling enclosed areas, bounded by grid edges or other azure regions.
"""

import numpy as np

def get_azure_pixels(grid):
    """Finds the coordinates of all azure (8) pixels in the grid."""
    return np.argwhere(grid == 8)

def expand_vertically(grid, start_coords):
    """Expands azure pixels vertically, creating lines."""
    rows, cols = grid.shape
    expanded_grid = grid.copy()

    for r, c in start_coords:
        # Expand upwards
        for i in range(r - 1, -1, -1):
            if grid[i, c] == 8:
                break
            expanded_grid[i,c] = 8
        # Expand downwards
        for i in range(r + 1, rows):
            if grid[i, c] == 8:
                break
            expanded_grid[i,c] = 8

    return expanded_grid

def expand_horizontally(grid, start_coords):
    """Expands azure pixels horizontally, creating lines."""
    rows, cols = grid.shape
    expanded_grid = grid.copy()
    for r, c in start_coords:
      # expand left
        for j in range(c - 1, -1, -1):
            if grid[r, j] == 8:
                break
            expanded_grid[r,j] = 8
        # Expand right
        for j in range(c + 1, cols):
            if grid[r, j] == 8:
                break
            expanded_grid[r,j] = 8
    return expanded_grid

def fill_between(grid):
  """fill the area between the border and expanded areas"""
  filled_grid = grid.copy()
  rows, cols = filled_grid.shape

  #fill horizontal
  for r in range(rows):
    left = -1
    right = -1

    for c in range(cols):
      if filled_grid[r,c] == 8:
        if left == -1:
          left = c
        else:
          right = c
    if left > -1 and right > -1:
        filled_grid[r,left:right+1] = 8

  #fill vertical
  for c in range(cols):
    top = -1
    bottom = -1
    for r in range(rows):
        if filled_grid[r, c] == 8:
            if top == -1:
              top = r
            else:
              bottom = r

    if top > -1 and bottom > -1:
        filled_grid[top:bottom+1,c] = 8

  return filled_grid

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # Initialize output grid as a copy of the input grid.
    output_grid = input_grid.copy()

    # Get initial azure pixel coordinates.
    azure_coords = get_azure_pixels(output_grid)
    #expand area to include the borders
    rows, cols = output_grid.shape
    for r in range(rows):
        output_grid[r,0] = 8
        output_grid[r,cols-1] = 8
    for c in range(cols):
        output_grid[0,c] = 8
        output_grid[rows-1,c] = 8
    # Expand vertically.
    output_grid = expand_vertically(output_grid, azure_coords)
    # Get new azure coordinates
    azure_coords_v = get_azure_pixels(output_grid)
    # Expand horizontally.
    output_grid = expand_horizontally(output_grid, azure_coords_v)

    # fill areas
    output_grid = fill_between(output_grid)

    return output_grid
```
