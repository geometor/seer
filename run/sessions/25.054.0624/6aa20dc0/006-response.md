# 6aa20dc0 • 006 • refine_coder

---
```python
"""
The transformation rule is based on the interaction between a background and other, smaller objects. The background color changes to match any adjacent object of a different color, and this change spreads outwards.
"""

import numpy as np
from collections import deque

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
            if not visited[row, col]:
                obj_pixels = []
                dfs(row, col, grid[row, col], obj_pixels)
                if obj_pixels:  # Ensure object is not empty
                    objects.append((grid[row,col], obj_pixels))
    return objects

def get_neighbors(grid, row, col):
    """Get the neighbors of a pixel, including diagonals."""
    neighbors = []
    for r in range(max(0, row - 1), min(grid.shape[0], row + 2)):
        for c in range(max(0, col - 1), min(grid.shape[1], col + 2)):
            if (r, c) != (row, col):
                neighbors.append((r, c))
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find objects
    objects = get_objects(input_grid)

    # Determine background color (most frequent, for now)
    color_counts = {}
    for color, _ in objects:
        color_counts[color] = color_counts.get(color, 0) + 1
    background_color = max(color_counts, key=color_counts.get)
    
    # Create a queue for color spreading
    q = deque()

    # Initialize queue with non-background pixels
    for color, pixels in objects:
        if color != background_color:
            for r, c in pixels:
                q.append((r,c,color))

    # Breadth-First Search for color propagation
    visited = np.zeros_like(input_grid, dtype=bool) #reset visited
    while q:
      r, c, color = q.popleft()
      
      #set this color
      output_grid[r,c] = color

      #get neighbors for propagation
      for nr, nc in get_neighbors(input_grid, r, c):
        if output_grid[nr, nc] == background_color: #only change background
            if not visited[nr,nc]: # prevent re-queueing
                visited[nr,nc] = True
                q.append((nr, nc, color))

    return output_grid
```
