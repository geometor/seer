# 1-3aa6fb7a • 004 • refine_coder

---
```python
"""
Transformation Rule:

1.  Identify Azure Objects: Scan the input grid and find all distinct objects
    that consist of exactly two azure (8) colored pixels.

2.  Determine Orientation: For each identified two-pixel azure object, determine
    its orientation:
    *   Horizontal: If the two pixels are in the same row and adjacent columns.

3.  Apply Transformation (Conditional):
    *   If Horizontal: Find the leftmost azure pixel in the horizontal object.
        Insert a white (0) pixel directly below this leftmost azure pixel in
        the output grid.
    *   If not horizontal: there is no change to this object

4.  Output: The output grid is the result of applying these transformations to
    the input grid. All other pixels in the input grid remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
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
                if len(current_object) == 2: # only look for objects with 2 pixels
                  objects.append(current_object)
    return objects

def is_horizontal(object_pixels):
    # object assumed to have only 2 pixels
    return object_pixels[0][0] == object_pixels[1][0]

def get_leftmost_pixel(object_pixels):
    # object assumed to have only 2 pixels
    if object_pixels[0][1] < object_pixels[1][1]:
      return object_pixels[0]
    else:
      return object_pixels[1]

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      if is_horizontal(obj):
        # insert white pixel (0) below leftmost pixel of horizontal object
        leftmost_pixel = get_leftmost_pixel(obj)
        row = leftmost_pixel[0] + 1
        col = leftmost_pixel[1]
        # only insert if within grid bounds
        if row < output_grid.shape[0]:
          output_grid[row, col] = 0

    return output_grid
```
