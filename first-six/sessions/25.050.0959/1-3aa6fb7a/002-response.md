# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule identifies azure L-shaped (3 cells) objects within the grid. For each of those objects, it locates a cell on its top-right corner and colors it in blue. Other cells are kept unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of coordinate tuples, each representing an L-shape.  
    An L shape is defined by these relative coordinates:
      (0,0) (1,0)
            (1,1)
      and rotations.
    Each coordinate returned contains the "corner" of the L.
    """
    
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for the four possible L-shape orientations
            if grid[r, c] == color and grid[r + 1, c] == color and grid[r + 1, c + 1] == color:
                l_shapes.append((r, c))  # Top-left corner
            if grid[r, c] == color and grid[r, c+1] == color and grid[r+1, c] == color:
                l_shapes.append((r,c))
            if grid[r, c+1] == color and grid[r+1, c+1] == color and grid[r+1, c] == color:
                l_shapes.append((r,c))
            if grid[r, c] == color and grid[r, c + 1] == color and grid[r + 1, c + 1] == color:
                l_shapes.append((r, c))  # Top-left corner

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Find azure L-shapes, and change the color of cell adjacent to its top-right to blue.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid, 8)

    for r, c in l_shapes:
      # determine the orientation and find the top-right corner
      if input_grid[r,c] == 8 and input_grid[r+1,c] == 8 and input_grid[r+1,c+1] == 8: # original orientation
        # change top-right cell to blue if it is white
        if r < input_grid.shape[0] -1 and c < input_grid.shape[1] -2 and input_grid[r,c+2] == 0:
          output_grid[r,c+2] = 1
      if input_grid[r,c] == 8 and input_grid[r,c+1] == 8 and input_grid[r+1,c] == 8: # 90 degree
        if r > 0  and c < input_grid.shape[1] -1 and input_grid[r-1,c] == 0:
          output_grid[r-1,c] = 1

      if input_grid[r,c+1] == 8 and input_grid[r+1,c] == 8 and input_grid[r+1,c+1] == 8: #270 degree
        if r < input_grid.shape[0] -1 and c >0 and input_grid[r+1,c-1] == 0:
          output_grid[r+1,c-1] = 1
      if input_grid[r,c] == 8 and input_grid[r,c+1] == 8 and input_grid[r+1,c+1] == 8: # 180 degree
        if c < input_grid.shape[1] - 1 and r < input_grid.shape[0] -2 and input_grid[r+2,c+1] == 0:
          output_grid[r+2,c+1] = 1
      
    return output_grid
```
