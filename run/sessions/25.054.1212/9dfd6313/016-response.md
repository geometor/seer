# 9dfd6313 • 016 • refine_coder

---
```python
"""
1.  **Identify Objects:** Identify all distinct objects in the input grid. An object is a contiguous group of pixels of the same color.
2. **Top Row Object Identification:** Locate the object(s) containing azure (8) pixels. If found, move the entire azure object to the top row, positioning its leftmost pixel in the third column (index 2). Other positions of this object are determined by the positions relative to this leftmost pixel.
3.  **Second Top Row Placement**: Locate the object(s) containing red (2) pixels. If found, move the red object to the top row, positioning its leftmost pixel adjacent to the rightmost pixel of the azure object. Other positions of this object are determined by the positions relative to this leftmost pixel.
4. **Conditional Shift:** If an object does not have color 8 or 2, then move down by one row.
5. **Preservation:** Pixels not part of moved objects shift down by exactly one row.
"""

import numpy as np

def find_objects(grid):
    """Identifies distinct objects in the grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, color, current_object)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c]:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r, c], current_object))  # Store color and object pixels
    return objects

def move_object(grid, object_pixels, target_row, target_col_start):
    """Moves an object to a new location within the grid"""
    new_grid = np.copy(grid)

    #clear old positions
    for r, c in object_pixels:
        new_grid[r,c] = 0

    #compute the new positions
    min_col = min([c for _, c in object_pixels])
    for r,c in object_pixels:
        new_grid[target_row, target_col_start + (c - min_col)] = grid[r,c]

    return new_grid


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = find_objects(input_grid)

    # 2. & 3. Move Azure and Red Objects
    azure_object = None
    red_object = None

    for color, pixels in objects:
        if color == 8:
            azure_object = pixels
        elif color == 2:
            red_object = pixels

    if azure_object is not None:
        output_grid = move_object(output_grid, azure_object, 0, 2)
    if red_object is not None:
       if azure_object is not None:
          max_azure_col = max([c for _, c in azure_object])
          output_grid = move_object(output_grid,red_object, 0, max_azure_col + 1 )
       else:
          output_grid = move_object(output_grid, red_object, 0, 2)

    # 4. & 5. Shift other objects/pixels down
    for color, pixels in objects:
       if color != 8 and color != 2:
            for r, c in pixels:
                if r + 1 < rows:
                    output_grid[r+1,c] = color

    return output_grid
```
