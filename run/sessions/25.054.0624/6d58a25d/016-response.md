# 6d58a25d • 016 • refine_coder

---
```python
"""
1.  **Identify** a contiguous shape of yellow (4) pixels within the input grid.
2.  **Replace** all pixels within the identified yellow shape with green (3) pixels.
3.  **Fill** all remaining pixels *not* part of the original yellow shape with green (3). This includes pixels of any color other than the original yellow shape.
"""

import numpy as np

def find_contiguous_shape(grid, color):
    """Finds the coordinates of a contiguous shape of the given color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    shape_coords = []

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        shape_coords.append((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        # Include diagonals:
        dfs(r + 1, c + 1)
        dfs(r + 1, c - 1)
        dfs(r - 1, c + 1)
        dfs(r - 1, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                dfs(r, c)
                return shape_coords  # Return after finding the *first* contiguous shape
    return [] # return empty if no shape found


def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find the coordinates of the contiguous yellow shape
    yellow_shape_coords = find_contiguous_shape(input_grid, 4)

    # Replace the yellow shape with green
    for r, c in yellow_shape_coords:
        output_grid[r, c] = 3

    # Fill all cells that were *not* part of the original yellow shape.
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in yellow_shape_coords:
                output_grid[r, c] = 3

    return output_grid
```

