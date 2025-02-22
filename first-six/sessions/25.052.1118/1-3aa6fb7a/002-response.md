# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves existing azure colored vertical rectangles and adds blue pixels (1) next to each top part of the azure rectangles.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    # Find azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Add blue pixels (1) next to the top of each azure rectangle
    for obj in azure_objects:
        # Sort the object coordinates by row to find the top cell
        top_cell = sorted(obj, key=lambda x: x[0])[0]
        # Calculate the position for the new blue pixel
        blue_pixel_row = top_cell[0]
        blue_pixel_col = top_cell[1] + 1
        # Check if the blue pixel position is within the grid bounds
        if 0 <= blue_pixel_row < output_grid.shape[0] and 0 <= blue_pixel_col < output_grid.shape[1]:
            output_grid[blue_pixel_row, blue_pixel_col] = 1

    return output_grid
```

