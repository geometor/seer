# 1-3aa6fb7a • 008 • example_2 - CODE

---
```python
"""
Scan the input. If an azure pixel has a black pixel to its immediate right, and the azure pixel is at the right border of an azure area, insert a blue pixel to the right of the azure pixel in the output grid.
"""

import numpy as np

def get_objects(grid, color):
    """
    Find contiguous regions of the specified color.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        # Explore adjacent cells
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    azure_objects = get_objects(input_grid, 8)

    for obj in azure_objects:
      for r,c in obj:
        if c + 1 < cols and input_grid[r,c+1] == 0:
          #check if on border:
          is_border = True
          for other_r, other_c in obj:
            if other_c == c+1:
              is_border = False
              break
          if is_border:
            output_grid[r,c+1] = 1

    return output_grid
```

