# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
For each azure object, change the last pixel, or right most pixel to blue.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous objects of the specified color
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
            if not visited[row, col] and grid[row, col] == color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_last_pixel(object_pixels):
    # for vertical objects, last is lowest row
    # for horizontal, last is right-most
    # break ties arbitrarily
    
    return max(object_pixels, key=lambda p: (p[1]))

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find azure objects
    azure_objects = find_objects(input_grid, 8)

    # change output pixels 
    for obj in azure_objects:
        last_pixel = get_last_pixel(obj)
        output_grid[last_pixel] = 1

    return output_grid
```
