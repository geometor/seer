# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Object Identification:** The program searches for objects composed of *exactly two* azure (color code 8) pixels.  These are the only objects of interest.

2.  **Orientation Check:** For each identified two-pixel azure object, determine its orientation.  There are only two possibilities to consider at this stage:
    *   **Horizontal:** The two azure pixels are adjacent and in the same row.
    *  **Vertical**

3.  **Conditional Transformation:**
    *   **If Horizontal:** Locate the leftmost azure pixel within the two-pixel object. Insert a *blue* (color code 1) pixel directly *below* this leftmost azure pixel.
    * if Vertical: then it will insert the blue pixel to the right of the bottom most pixel.

4.  **Output:** All other pixels from the input grid remain unchanged in the output grid. The output is the result of applying the above steps to all two-pixel azure objects in the input.
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

def get_bottommost_pixel(object_pixels):
    # object assumed to have only 2 pixels
    if object_pixels[0][0] > object_pixels[1][0]:
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
        # insert blue pixel (1) below leftmost pixel of horizontal object
        leftmost_pixel = get_leftmost_pixel(obj)
        row = leftmost_pixel[0] + 1
        col = leftmost_pixel[1]
        # only insert if within grid bounds
        if row < output_grid.shape[0]:
          output_grid[row, col] = 1  # Corrected color to blue (1)
      else: # Vertical case
        bottommost_pixel = get_bottommost_pixel(obj)
        row = bottommost_pixel[0]
        col = bottommost_pixel[1] + 1
        if col < output_grid.shape[1]:
            output_grid[row,col] = 1

    return output_grid
```
