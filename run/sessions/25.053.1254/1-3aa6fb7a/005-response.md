# 1-3aa6fb7a • 005 • refine_coder

---
```python
"""
Identify azure (color 8) objects in the input grid. For each object, place a '1' in the output grid at the rightmost pixel of the object's top row.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of a specified color in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
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
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_rightmost_top_pixel(obj):
    """Finds the rightmost pixel on the top row of an object."""
    top_row = min(row for row, _ in obj)
    rightmost_col = max(col for row, col in obj if row == top_row)
    return (top_row, rightmost_col)
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Place '1's in the output grid
    for obj in azure_objects:
        top_row, rightmost_col = find_rightmost_top_pixel(obj)
        # shift down by 1
        output_grid[top_row+1, rightmost_col] = 1

    return output_grid
```
