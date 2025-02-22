# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves two azure L-shaped objects and introduces two new blue pixels.
One blue pixel is placed at the (1, 2), corresponding to the top corner of the top-left azure L-shape.
Another blue pixel is placed at (4, 5), corresponding to the top corner of the center-right azure L-shape.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))

        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                objects.append(dfs(row, col))

    return objects

def find_l_shape_top_corner(object_pixels):
    # Sort the pixels by row and then by column
    sorted_pixels = sorted(object_pixels, key=lambda x: (x[0], x[1]))

    # Return top-left corner
    return sorted_pixels[0]

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = input_grid.copy()

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Find L-shape top corners and place blue pixels
    for obj in azure_objects:
      #check the size of object
      if len(obj) == 3:
        top_corner = find_l_shape_top_corner(obj)

        #Adjust for L shape top corner

        if (top_corner[0]+1, top_corner[1]+2) in obj:
            output_grid[top_corner[0], top_corner[1]+1] = 1
        elif (top_corner[0]+1, top_corner[1]-2) in obj:
            output_grid[top_corner[0]+1, top_corner[1]-1] = 1
        elif (top_corner[0]+2, top_corner[1]-1) in obj:
            output_grid[top_corner[0]+1, top_corner[1]] = 1
        elif (top_corner[0]+2, top_corner[1]+1) in obj:
            output_grid[top_corner[0]+1, top_corner[1]] = 1


    return output_grid
```

