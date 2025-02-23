# 5-150deff5 • 004 • refine_code - CODE

---
```python
"""
The transformation involves identifying gray (5) blobs in the input grid. If a gray blob is located in either of the two leftmost or two rightmost columns, it's considered a "corner" blob and its color is changed to azure (8). All other gray blobs (not in the corners) are changed to red (2). The black (0) background is preserved.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of (row, col) tuples representing the object's pixels.
    """
    objects = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []

        visited.add((row, col))
        region = [(row, col)]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            region.extend(dfs(row + dr, col + dc))
        
        return region

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the revised rule.
    """
    output_grid = np.copy(input_grid)
    gray_objects = find_objects(input_grid, 5)

    # Find left and right corner objects
    for obj in gray_objects:
        is_corner = False
        for r, c in obj:
            # Check if any part of the object is in the first two or last two columns
            if c in [0, 1] : # Left
                is_corner = True
                break
            if c in [input_grid.shape[1]-2,input_grid.shape[1]-1] : # Right
                is_corner = True
                break
            
        for r, c in obj:
          if is_corner:
              output_grid[r, c] = 8  # Change corner blobs to azure
          elif input_grid[r,c] == 5:
              output_grid[r, c] = 2  # Change other gray areas to red

    return output_grid
```

