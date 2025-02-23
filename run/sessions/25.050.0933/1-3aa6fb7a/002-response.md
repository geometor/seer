# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation identifies azure regions. From each identified regions, find the most isolated azure pixel, which has no neighbors with the same color and change it to blue. The rest of the structure is kept unchanged.
"""

import numpy as np

def get_objects(grid, color):
    """
    Identify contiguous regions of the specified color.
    Returns a list of sets, where each set contains the coordinates of an object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.add((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = set()
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def count_neighbors(grid, r, c, color):
  """
  Counts neighbors with given color
  """
  rows, cols = grid.shape
  count = 0
  for dr in [-1,0,1]:
    for dc in [-1,0,1]:
      if dr == 0 and dc == 0:
        continue
      nr, nc = r + dr, c + dc
      if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc] == color:
        count += 1
  return count
def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = input_grid.copy()
    azure_objects = get_objects(input_grid, 8)

    for obj in azure_objects:
        min_neighbors = 9
        least_connected_pixel = None
        for r,c in obj:
          neighbors = count_neighbors(input_grid, r, c, 8)
          if neighbors < min_neighbors:
            min_neighbors = neighbors
            least_connected_pixel = (r,c)
        if least_connected_pixel:
            output_grid[least_connected_pixel] = 1

    return output_grid
```
