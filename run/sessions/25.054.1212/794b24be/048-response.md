# 794b24be • 048 • refine_coder

---
```python
"""
Identify the contiguous region of blue (1) pixels in the input grid, considering both horizontal, vertical, and diagonal connections.
Change all pixels in this region to red (2).
Create a new output grid of the same dimensions, filled with black (0) pixels.
Place the transformed red object at the top-left corner (0,0) of the output grid.
"""

import numpy as np

def find_object_with_diagonal(grid):
    """Finds the contiguous region of 1s, including diagonal connections."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    object_pixels = []

    def dfs(row, col):
        """Depth-first search to find connected components."""
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row, col] or grid[row, col] != 1:
            return
        visited[row, col] = True
        object_pixels.append((row, col))
        # Check all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1 and not visited[r, c]:
                object_pixels = []  # Reset for each new object
                dfs(r, c)
                if object_pixels:
                    # yield the object pixels of this object
                    return object_pixels
    return [] # return empty list if there are no objects
                

def transform(input_grid):
    """Transforms the input grid by moving the blue object to the top-left and changing its color to red."""
    # Find the object's pixels, including diagonal connections
    object_pixels = find_object_with_diagonal(input_grid)

    # Initialize output grid with 0s
    output_grid = np.zeros_like(input_grid)

    if object_pixels:
        # Find the top-left corner of the object in the original image
        min_row = min(p[0] for p in object_pixels)
        min_col = min(p[1] for p in object_pixels)

        # Copy the object to the top-left of the output grid, changing color to red (2)
        for r, c in object_pixels:
            output_grid[r - min_row, c - min_col] = 2

    return output_grid
```
