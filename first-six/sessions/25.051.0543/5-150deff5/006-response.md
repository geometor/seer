# 5-150deff5 • 006 • example_3 - CODE

---
```python
"""
1. Find the gray object (color 5).
2. Copy gray object into output.
3. Change gray object color into azure (8).
4. Identify parts inside object.
5. Fill this parts with red (2).
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def is_inside(grid, coord, color):
    """
    Checks if a coordinate is inside the object
    by expanding around, making sure the coordinate is enclosed by 'color'.
    """
    rows, cols = grid.shape
    r, c = coord

    # Check if it is not on edge
    if r == 0 or r == rows-1 or c == 0 or c == cols-1:
      return False
      
    # Check boundaries
    if not (0 <= r < rows and 0 <= c < cols):
        return False

    # Check neighbors
    neighbors = [
        (r-1, c), (r+1, c), (r, c-1), (r, c+1),  # direct
        (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1) # diagonal
    ]

    for nr, nc in neighbors:
      if not (0 <= nr < rows and 0 <= nc < cols):
          continue
      if grid[nr, nc] != color and grid[nr,nc] != 0:
        return False
    
    return True
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5)
    gray_object_coords = find_object(input_grid, 5)

    # Change the gray object to azure (8) in the output grid
    for r, c in gray_object_coords:
        output_grid[r, c] = 8

    # Create an auxiliary grid to process the enclosed parts
    aux_grid = np.copy(input_grid)
    for r, c in gray_object_coords:
      aux_grid[r,c] = 0 # convert gray into background

    rows, cols = input_grid.shape

    for r in range(rows):
      for c in range(cols):
        if is_inside(output_grid, (r,c), 8):
          if aux_grid[r,c] == 5:
            output_grid[r,c] = 2

    return output_grid
```

