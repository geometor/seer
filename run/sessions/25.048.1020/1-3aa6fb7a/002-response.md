# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation identifies two azure (color 8) objects in the input grid. It then adds a blue (color 1) pixel adjacent to the topmost azure pixel of each object: to the right of the first object's topmost pixel, and to the top of the second object's topmost pixel. All other azure pixels from the input remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the specified color.
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

def find_topmost_pixel(object_pixels):
    # Find the topmost pixel of an object (smallest row index).
    return min(object_pixels, key=lambda p: p[0])

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = input_grid.copy()

    # Find azure objects.
    azure_objects = find_objects(input_grid, 8)

    # Process each azure object.
    for obj in azure_objects:
        # Find the topmost pixel.
        topmost_pixel = find_topmost_pixel(obj)
        row, col = topmost_pixel

        # Add blue pixel based on object index
        if azure_objects.index(obj) == 0:
            #first object, to the right
            if col + 1 < output_grid.shape[1]:
                output_grid[row,col+1] = 1
        elif azure_objects.index(obj) == 1 :
             #second object, one pixel up and one pixel to the left
            if row + 1 < output_grid.shape[0] and col -1 >=0:
                output_grid[row+1,col] = 1

    return output_grid
```
