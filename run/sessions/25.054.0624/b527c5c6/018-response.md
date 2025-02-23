# b527c5c6 • 018 • refine_coder

---
```python
"""
1.  **Top-Left Object Modification:** Find the top-most green (3) object in the input grid. If there is a red (2) pixel to the immediate right of this green object, change the right-most green pixel of the top-most green object in that row to white (0).
2.  **Bottom-Right Object Extension:** Find the bottom-most green (3) object. Extend this bottom-most object, starting from its bottom edge, to the left with red (2) pixels. The extension should be a rectangle of red pixels that has the same width as the bottom-most green object.
"""

import numpy as np

def find_objects(grid, color):
    # Find objects of a specific color in the grid.
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
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
    # Get the bounding box of an object.
    rows, cols = zip(*obj)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    return min_row, max_row, min_col, max_col
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find green objects
    green_objects = find_objects(input_grid, 3)
    
    # Identify top-most and bottom-most green objects
    if not green_objects:
        return output_grid

    top_green = sorted(green_objects, key=lambda obj: get_object_bounds(obj)[0])[0]
    bottom_green = sorted(green_objects, key=lambda obj: get_object_bounds(obj)[0])[-1]

    top_bounds = get_object_bounds(top_green)
    bottom_bounds = get_object_bounds(bottom_green)

    # 1. Top-Left Object Modification
    for r in range(top_bounds[0], top_bounds[1] + 1):
        for c in range(top_bounds[2], top_bounds[3] + 1):
          if (r,c) in top_green:
            if c + 1 < input_grid.shape[1] and input_grid[r, c + 1] == 2:
                # find rightmost green in this row of the object:
                row_pixels = [(row,col) for (row, col) in top_green if row == r]
                rightmost_c = max([col for row, col in row_pixels])
                output_grid[r, rightmost_c] = 0


    # 2. Bottom-Right Object Extension
    extension_width = bottom_bounds[3] - bottom_bounds[2] + 1
    
    start_row = bottom_bounds[1] + 1

    for r in range(start_row, start_row + extension_width):
        for c in range(bottom_bounds[2] - extension_width, bottom_bounds[2]):
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 2

    return output_grid
```

