# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The 'inner-corner' of each azure L-shape is changed to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.
    Returns a list of coordinates for each object.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_inner_corner(object_coords):
    """
    Finds the inner corner pixel of an L-shaped figure.
    The inner corner is the cell where the right angle of the "L" is formed.
    """

    rows = [r for r, c in object_coords]
    cols = [c for r, c in object_coords]
    
    for r in sorted(rows):
        for c in sorted(cols):
          if (r+1,c) in object_coords and (r,c+1) in object_coords:
              return (r,c)
          if (r-1,c) in object_coords and (r,c+1) in object_coords:
              return (r,c)          
          if (r+1,c) in object_coords and (r,c-1) in object_coords:
              return (r,c)
          if (r-1,c) in object_coords and (r,c-1) in object_coords:
              return (r,c)

    return None

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    The 'inner-corner' of each of the azure L-shapes is changed to blue.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Find the inner corner of each azure L-shape
    corners = []
    for obj in azure_objects:
      inner_corner = find_inner_corner(obj)
      if inner_corner:
          corners.append(inner_corner)
    
    # Change the identified corner pixels to color 1 (blue)
    for corner in corners:
      output_grid[corner]=1

    return output_grid
```

