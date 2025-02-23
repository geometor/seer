# f1cefba8 • 012 • refine_coder

---
```python
"""
Transforms an input grid by identifying objects, mirroring them across their 
horizontal axis, and performing edge modifications based on the object's 
horizontal axis.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous blocks of non-white (non-zero) pixels.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    objects = []

    def dfs(r, c, color, obj_pixels):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        obj_pixels.append((r, c))
        dfs(r + 1, c, color, obj_pixels)
        dfs(r - 1, c, color, obj_pixels)
        dfs(r, c + 1, color, obj_pixels)
        dfs(r, c - 1, color, obj_pixels)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and not visited[r, c]:
                obj_pixels = []
                dfs(r, c, grid[r, c], obj_pixels)
                objects.append((grid[r,c], obj_pixels))  # Store color with object
    return objects

def find_horizontal_axis(object_pixels):
    """
    Finds the horizontal axis of an object (row with the most pixels).
    """
    row_counts = {}
    for r, c in object_pixels:
        row_counts[r] = row_counts.get(r, 0) + 1
    max_count = 0
    axis_row = -1
    for r, count in row_counts.items():
        if count > max_count:
            max_count = count
            axis_row = r
    return axis_row

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = find_objects(input_grid)

    for color, obj_pixels in objects:
        # 2. Find Object horizontal axis
        axis_row = find_horizontal_axis(obj_pixels)

        # 3. Mirror
        for r, c in obj_pixels:
            if r != axis_row:
                dist = r - axis_row
                mirrored_row = axis_row - dist
                if 0 <= mirrored_row < rows:
                    output_grid[mirrored_row, c] = color

        # 4. Edge Modification
        #   Find extent of axis:
        axis_cols = [c for r, c in obj_pixels if r == axis_row]

        if len(axis_cols) > 0 :

          min_axis_col = min(axis_cols)
          max_axis_col = max(axis_cols)

          # 4a. Examine rows above and below
          for row_offset in [-1, 1]:
              check_row = axis_row + row_offset
              if 0 <= check_row < rows:
                  for c in range(min_axis_col, max_axis_col + 1):
                      if (check_row,c) not in obj_pixels:
                        output_grid[check_row, c] = color

          # 4b. Add object color to axis row adjacent to edge.
          if 0 in axis_cols:
              output_grid[axis_row, 0] = color
          if cols -1 in axis_cols:
              output_grid[axis_row, cols-1] = color
    return output_grid
```
