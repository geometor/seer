# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
Identify all azure (color 8) L-shaped objects.  Each L-shape is composed of three contiguous pixels. Extend each L-shape by adding a single blue pixel (color 1) to complete the 2x2, 2x3 or 3x2 square/rectangle that contains the L-shape. The position of the blue pixel is determined by finding the missing pixel to complete the rectangle.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_missing_pixel_for_rectangle(l_shape_coords):
    # Find the bounding box
    min_r = min(r for r, c in l_shape_coords)
    max_r = max(r for r, c in l_shape_coords)
    min_c = min(c for r, c in l_shape_coords)
    max_c = max(c for r, c in l_shape_coords)

    # Determine all possible coordinates within the bounding box
    potential_coords = [(r, c) for r in range(min_r, max_r + 1) for c in range(min_c, max_c + 1)]

    # Find the missing coordinate
    for coord in potential_coords:
        if coord not in l_shape_coords:
            return coord

    return None # should not happen, but added as a precaution


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # change output pixels
    for obj in azure_objects:
      if len(obj) == 3:  # Ensure it's an L-shape
        missing_pixel = find_missing_pixel_for_rectangle(obj)
        if missing_pixel:
             output_grid[missing_pixel] = 1

    return output_grid
```

