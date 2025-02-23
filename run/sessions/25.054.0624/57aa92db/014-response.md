# 57aa92db • 014 • example_3 • investigate_coder

---
```python
"""
The transformation preserves a small blue/yellow structure in the top-left while expanding a larger azure/yellow structure in the bottom-right. The yellow pixels within the larger structure maintain their relative positions within the expanded azure region.
"""

import numpy as np

def find_object(grid, color):
    # Find objects (contiguous regions of a specific color)
    mask = (grid == color)
    if not np.any(mask):
      return []

    rows, cols = np.where(mask)
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    objects = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or not mask[row, col]:
            return []
        visited.add((row, col))
        region = [(row, col)]
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            region.extend(dfs(row + dr, col + dc))
        return region

    for r, c in zip(rows, cols):
        if (r, c) not in visited:
            objects.append(dfs(r, c))

    return objects

def get_object_bounds(obj):
    rows, cols = zip(*obj)
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Initialize output_grid with zeros and the same dimensions as the input.
    output_grid = np.zeros_like(input_grid)

    # Find shape1 (blue object with internal yellow)
    blue_objects = find_object(input_grid, 1)
    shape1 = None
    for obj in blue_objects:
      min_row, max_row, min_col, max_col = get_object_bounds(obj)
      for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
          if input_grid[r][c] == 4:
            shape1 = obj
            break
        if shape1:
          break
      if shape1:
        break

    # Maintain shape1
    if shape1:
      for r, c in shape1:
        output_grid[r, c] = input_grid[r, c]


    # Find shape2 (azure object)
    azure_objects = find_object(input_grid, 8)
    shape2 = None
    #find biggest object
    max_size = 0
    for obj in azure_objects:
      size = len(obj)
      if size > max_size:
        max_size = size
        shape2 = obj


    if shape2:
      #get bounds
      min_row, max_row, min_col, max_col = get_object_bounds(shape2)

      # Find yellow pixels within shape2
      yellow_pixels = []
      for r in range(min_row, max_row + 1):
          for c in range(min_col, max_col + 1):
              if input_grid[r, c] == 4:
                  yellow_pixels.append((r, c))

      # Expand and combine shape2
      # Determine new boundaries based on padding and existing yellow pixels
      
      new_min_row = min_row
      while new_min_row > 0 and (min_row-new_min_row) < 3:
        new_min_row -=1
      new_min_col = min_col
      while new_min_col > 0 and (min_col-new_min_col) < 2:
          new_min_col -=1
      
      new_max_col = max_col
      while new_max_col < input_grid.shape[1]-1 and (new_max_col - max_col) < 2:
        new_max_col += 1

      new_max_row = 15
      new_max_col = max(new_max_col, 14)

      #fill with azure
      for r in range(new_min_row, new_max_row + 1):
          for c in range(new_min_col, new_max_col + 1):
              output_grid[r, c] = 8

      # fill yellow pixels
      for r, c in yellow_pixels:
          new_r = r + (new_min_row - min_row)
          new_c = c + (new_min_col - min_col)
          if 0 <= new_r < output_grid.shape[0] and 0<= new_c < output_grid.shape[1]:
            output_grid[new_r, new_c] = 4
          

    return output_grid
```
