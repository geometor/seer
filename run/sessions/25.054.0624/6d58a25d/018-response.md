# 6d58a25d • 018 • refine_coder

---
```python
"""
1.  **Identify** all contiguous shapes of *yellow* (4) pixels within the input grid.
2.  **Within each yellow shape**: For any pixel within the yellow shape's boundaries, change its color to *green* (3).
3.  **Preserve other objects**: Colors and positions of objects that are not yellow should not be changed.
4. **Preserve background**: The color of the background should be preserved.
"""

import numpy as np

def find_all_contiguous_shapes(grid, color):
    """Finds coordinates of all contiguous shapes of the given color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    shapes = []

    def dfs(r, c, current_shape):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_shape.append((r, c))
        dfs(r + 1, c, current_shape)
        dfs(r - 1, c, current_shape)
        dfs(r, c + 1, current_shape)
        dfs(r, c - 1, current_shape)
        # Include diagonals:
        dfs(r + 1, c + 1, current_shape)
        dfs(r + 1, c - 1, current_shape)
        dfs(r - 1, c + 1, current_shape)
        dfs(r - 1, c - 1, current_shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_shape = []
                dfs(r, c, current_shape)
                shapes.append(current_shape)
    return shapes


def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = input_grid.copy()

    # Find all yellow shapes
    yellow_shapes = find_all_contiguous_shapes(input_grid, 4)

    # Change color within each yellow shape to green
    for shape in yellow_shapes:
        for r, c in shape:
            output_grid[r, c] = 3

    return output_grid
```
