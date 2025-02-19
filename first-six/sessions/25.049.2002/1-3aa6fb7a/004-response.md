# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation consists in painting in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.
"""

import numpy as np

def get_objects(grid):
    """
    Identify contiguous regions of the same color as separate objects.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col]!=0:
                color = grid[row, col]
                obj = []
                dfs(row, col, color, obj)
                objects.append((color, obj))
    return objects
def transform(input_grid):
   """
    Transforms the input grid according to the rule: 
    Paint in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.
   """
   output_grid = np.copy(input_grid)
   objects = get_objects(input_grid)

   # Iterate and paint
   for color, obj in objects:
    if color == 8:
      for row,col in obj:
        if col+1 < input_grid.shape[1] and input_grid[row,col+1] == 0:
            is_right_edge = True
            for r,c in obj:
              if r==row and c == col+1:
                is_right_edge=False
                break
            if is_right_edge:
              output_grid[row,col+1] = 1

   return output_grid
```

