# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves the azure L-shaped objects. The transformation paints blue the cells at the right of the top-left element of each azure L-shape.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
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

def get_top_left(object_coords):
     # Sort by row, then by column, and take the first element
    return sorted(object_coords, key=lambda x: (x[0], x[1]))[0]
    

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Preserves azure L-shaped objects and paints blue the cell to the right
    of the top-left corner of each L-shape.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # find top-left element
        top_left = get_top_left(obj)

        # Paint the cell to the right of the top-left corner blue
        paint_row = top_left[0]
        paint_col = top_left[1] + 1

        if 0 <= paint_row < output_grid.shape[0] and 0 <= paint_col < output_grid.shape[1]:
             output_grid[paint_row, paint_col] = 1

    return output_grid
```

