# b527c5c6 • 004 • refine_coder

---
```python
"""
1.  **Identify Green Objects:** Locate all contiguous regions of green (3) pixels.
2.  **Leftmost Green Expansion:** The leftmost green object expands vertically downwards to the bottom of the grid. Any red pixels directly to the left of this expanding green object are replaced with green.
3. **Identify Red Objects:** Find all red objects.
4.  **Right Green Object Expansion:** Locate the green object to the right.
5.  **Red Expansion to Right of Rightmost Green Object:** Find any red pixels *adjacent* to the right green object. Use the right edge of the right green object, and these adjacent pixels as a seed to expand red down to the bottom of the board.
"""

import numpy as np

def find_objects(grid, color):
    """Find contiguous regions of a specific color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_object_bounds(obj):
    """Get the bounding box of an object."""
    min_row = min(p[0] for p in obj)
    max_row = max(p[0] for p in obj)
    min_col = min(p[1] for p in obj)
    max_col = max(p[1] for p in obj)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # 1. Identify Green Objects
    green_objects = find_objects(input_grid, 3)

    # Sort green objects by leftmost column
    green_objects.sort(key=lambda obj: min(p[1] for p in obj))
    
    if len(green_objects) >= 1:
      # 2. Leftmost Green Expansion
      left_green_object = green_objects[0]
      min_row, max_row, min_col, max_col = get_object_bounds(left_green_object)

      for col in range(min_col, max_col + 1):
          for row in range(min_row, height):
              # Check for red pixels to the left
              if col > 0 and input_grid[row, col-1] == 2:
                 output_grid[row,col-1] = 3
              output_grid[row, col] = 3

    if len(green_objects) > 1:
        # 4. Right Green Object
        right_green_object = green_objects[1]
        min_row_r, max_row_r, min_col_r, max_col_r = get_object_bounds(right_green_object)

        # 3. Identify Red Objects
        red_objects = find_objects(input_grid, 2)
        
        # 5. Red Expansion to Right of Rightmost Green Object
        for robj in red_objects:
            for rpix in robj:
                r, c = rpix
                # check for adjacent red pixels on the right
                if (
                    (r + 1, c) in right_green_object or
                    (r - 1, c) in right_green_object or
                    (r, c + 1) in right_green_object or
                    (r, c - 1) in right_green_object
                ):
                    # expand red down
                    for row in range(r, height):
                         output_grid[row, max_col_r] = 2
    # change output pixels

    return output_grid
```
