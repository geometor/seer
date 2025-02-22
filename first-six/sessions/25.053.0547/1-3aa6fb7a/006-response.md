# 1-3aa6fb7a • 006 • refine_code - CODE

---
```python
"""
For each azure object, find the right-most column. Within that column, change
the top azure pixels to blue.  A top azure pixel is defined as one that does
not have an azure pixel directly above it.
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

def get_rightmost_column(object_pixels):
    # Find the right-most column of an object
    return max(p[1] for p in object_pixels)

def get_top_pixels_in_column(object_pixels, column):
    # Find the top pixels in the specified column
    pixels_in_column = [p for p in object_pixels if p[1] == column]
    top_pixels = []
    for (row,col) in pixels_in_column:
        if (row -1, col) not in object_pixels:
            top_pixels.append((row,col))

    return top_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find azure objects
    azure_objects = find_objects(input_grid, 8)

    # change output pixels 
    for obj in azure_objects:
        rightmost_column = get_rightmost_column(obj)
        top_pixels = get_top_pixels_in_column(obj, rightmost_column)
        for pixel in top_pixels:
          output_grid[pixel] = 1

    return output_grid
```
