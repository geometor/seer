# 6aa20dc0 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation identifies non-blue (not 1) objects in the input grid. It then expands azure (8) colored objects that have adjacent, connected azure objects.
The expansion involves filling any adjacent blue (1) pixels with azure (8).
2x2 azure squares are grown to 4x4.
"""

import numpy as np

def get_objects(grid):
    """Finds contiguous objects (non-background pixels) in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, color, obj_pixels):
        """Depth-first search to find contiguous pixels of the same color."""
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
        obj_pixels.append((row, col))
        dfs(row + 1, col, color, obj_pixels)
        dfs(row - 1, col, color, obj_pixels)
        dfs(row, col + 1, color, obj_pixels)
        dfs(row, col - 1, color, obj_pixels)
        dfs(row + 1, col + 1, color, obj_pixels)  # Check diagonals
        dfs(row - 1, col - 1, color, obj_pixels)
        dfs(row + 1, col - 1, color, obj_pixels)
        dfs(row - 1, col + 1, color, obj_pixels)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] != 1:
                obj_pixels = []
                dfs(row, col, grid[row, col], obj_pixels)
                objects.append(obj_pixels)
    return objects

def is_2x2_square(object_pixels, grid):
    """Checks if an object forms a 2x2 square."""
    if len(object_pixels) != 4:
        return False
    rows, cols = zip(*object_pixels)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    return (max_row - min_row == 1) and (max_col - min_col == 1) and all(grid[r,c] == grid[object_pixels[0]] for r,c in object_pixels)

def expand_object(grid, object_pixels, new_color):
    """Expands connected azure objects by one layer and expands 2x2 to 4x4."""
    new_grid = np.copy(grid)
    rows, cols = zip(*object_pixels)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    if is_2x2_square(object_pixels, grid):

      # Expand to 4x4
      for r in range(min_row - 1, max_row + 2):
        for c in range(min_col - 1, max_col + 2):
          if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
             new_grid[r,c] = new_color

    for row, col in object_pixels: #grow azure shapes
      for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
          if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
            if grid[r,c] == 8:
              new_grid[r,c] = 8

    for row, col in object_pixels: # grow all azure objects
      for r in range(row - 1, row + 2):
          for c in range(col - 1, col + 2):
              if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] :
                  if grid[r, c] == 1:  # Expand onto blue background
                      new_grid[r, c] = new_color
    return new_grid
def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find objects
    objects = get_objects(output_grid)

    # Expand azure objects
    for obj_pixels in objects:
      first_pixel_row, first_pixel_col = obj_pixels[0]
      if output_grid[first_pixel_row, first_pixel_col] == 8: #if azure color
        output_grid = expand_object(output_grid, obj_pixels, 8)

    return output_grid
```
