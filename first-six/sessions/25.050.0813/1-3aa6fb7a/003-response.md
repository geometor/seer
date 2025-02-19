# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three L-shaped structures, two of them rotated."
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three L-shaped structures, two of them rotated."
    - color: 1 (blue)
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "Three single cells that replaces one cell of each color 8 shape."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can find three distinct "L-shaped" objects made of azure (color 8) cells.

2.  **Locate inner corner**:
    * Find the 'inner corner' of each L shape, where it forms the right angle of the "L" shape.

3.  **Change cell to color 1**:
     * Replace the corner cell identified in the previous step of each L-shaped structure by color 1 (blue)

4.  **Preserve all other cells**:

**Transformation Rule Summary**
The 'inner-corner' of each of the three azure L-shapes is changed to blue.

```python
"""
The 'inner-corner' of each of the three azure L-shapes is changed to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.
    Returns a list of coordinates.
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
    Finds the inner corner pixel of the L-shaped figures.
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
    The 'inner-corner' of each of the three azure L-shapes is changed to blue.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    corners = []
    for obj in azure_objects:
      inner_corner = find_inner_corner(obj)
      if inner_corner:
          corners.append(inner_corner)
    
    for corner in corners:
      output_grid[corner]=1

    return output_grid
```

