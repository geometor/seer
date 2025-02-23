# 88a62173 • 002 • example_1 • investigate_coder

---
```python
"""
Extract the top-left 2x2 block of red color and the single bottom-right red pixel.
"""

import numpy as np

def find_top_left_red_square(grid):
    # Find the top-left red square
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2:
                if r + 1 < rows and c + 1 < cols:
                  if grid[r+1,c] == 2 and grid[r, c+1] == 2 and grid[r+1,c+1] == 2:
                      return (r,c)
                else:
                    return None
    return None

def find_bottom_right_white(grid):
  rows, cols = grid.shape
  for r in range(rows):
    for c in range(cols):
      if grid[r,c] == 2:
        if r+1 < rows and c+1 < cols:
          if (grid[r,c] == 2 and grid[r+1, c] == 2 and
              grid[r,c+1] == 2 and grid[r+1,c+1] == 0 ):
            return (r+1, c+1)
          elif (grid[r,c] == 2 and grid[r+1, c] == 0 and
              grid[r,c+1] == 2 and grid[r+1,c+1] == 2 ):
            return (r+1, c)
          elif (grid[r,c] == 2 and grid[r+1, c] == 2 and
              grid[r,c+1] == 0 and grid[r+1,c+1] == 2 ):
            return (r, c+1)

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros((2, 2), dtype=int)

    # find top left 2x2 red square
    top_left_coords = find_top_left_red_square(input_grid)
    if top_left_coords:
      r, c = top_left_coords
      output_grid[0,0] = 2
      output_grid[0,1] = 2
      output_grid[1,0] = 2

    # find the single white cell
    white_coords = find_bottom_right_white(input_grid)
    if white_coords:
      output_grid[1,1] = 0

    return output_grid.tolist()
```
