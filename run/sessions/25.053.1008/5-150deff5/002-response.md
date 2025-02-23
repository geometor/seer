# 5-150deff5 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify the Object:** Locate the contiguous region of gray (5) pixels within the input grid.
2.  **Identify Border:** locate the border pixels of the object. A border pixel is one that is adjacent (up, down, left, right and diagonal) to the background color (0)
3.  **Inner fill:** Change all the inner pixels to azure color (8)
4.  **Outer fill:** Change the outer pixels to a red color (2)
5.  **Preserve Background:**  Leave all white (0) pixels unchanged.
"""

import numpy as np

def get_objects(grid, background_color=0):
    """Find contiguous regions of non-background color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] == background_color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        # Check neighbors (up, down, left, right, diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] != background_color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_border(grid, object_pixels, background_color=0):
    """Find the border pixels of an object."""
    border_pixels = []
    for row, col in object_pixels:
        is_border = False
        # Check neighbors (up, down, left, right, diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if (
                    nr < 0
                    or nr >= grid.shape[0]
                    or nc < 0
                    or nc >= grid.shape[1]
                    or grid[nr, nc] == background_color
                ):
                    is_border = True
                    break  # Optimization: Once a border is found, no need to check other neighbors
            if is_border:
                break
        if is_border:
            border_pixels.append((row, col))
    return border_pixels
def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()
    background_color = 0
    # Get objects
    objects = get_objects(input_grid, background_color)
    
    # process each object
    for obj in objects:
      # get border
      border_pixels = get_border(input_grid, obj, background_color)
      # fill inner
      for r, c in obj:
          output_grid[r,c] = 8
      # fill border
      for r, c in border_pixels:
          output_grid[r,c] = 2

    return output_grid
```
