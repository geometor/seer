# 1-3aa6fb7a • 008 • refine_coder

---
```python
"""
1.  **Find Azure Objects:** Locate all contiguous regions (objects) of azure (8) pixels in the input grid.
2.  **Iterate and Transform**: Iterate over all the azure objects, processing each object by finding it's top-left pixel.
3.  **First Object**: Set the pixel that is adjacent to the *right* of the top-left pixel of the object to blue (1).
4.  **Second and later**: If there is more than one object, set the pixel that is adjacent to the *top* of the object to the blue (1)
"""

import numpy as np

def find_objects(grid, color):
    # Find objects of a specific color in the grid.
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

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)
    
    for i, obj in enumerate(azure_objects):
        # Find top-left pixel
        rows, cols = zip(*obj)
        top_left_row, top_left_col = (min(rows), min(cols))

        # Apply transformation rules based on object order
        if i == 0 :  # First object: adjacent right
            if top_left_row >= 0 and top_left_row < output_grid.shape[0] and top_left_col + 1 >= 0 and top_left_col + 1 < output_grid.shape[1]:
                output_grid[top_left_row, top_left_col + 1] = 1

        if i > 0: # adjacent top of next object
           if top_left_row - 1 >= 0 and top_left_row - 1 < output_grid.shape[0] and top_left_col >= 0 and top_left_col < output_grid.shape[1]:
                output_grid[top_left_row - 1, top_left_col] = 1


    return output_grid
```

