# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Copies azure (color 8) objects from the input grid to the output grid.
For each azure object, a blue (color 1) pixel is placed immediately to the right of the top-left corner of the object.
All other pixels are set to white (color 0).
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_left_corner(object_coords):
    min_row = min(coord[0] for coord in object_coords)
    min_col = min(coord[1] for coord in object_coords)

    #find the coordinate that has min_row and min_col
    for row,col in object_coords:
        if row == min_row and col == min_col:
          return (row,col)
    return None #should never happen


def transform(input_grid):
    # Initialize output_grid with zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Copy azure objects to output and place blue pixels
    for obj in azure_objects:
        for row, col in obj:
            output_grid[row, col] = 8  # Copy azure pixel
        top_left = get_top_left_corner(obj)

        #place to the right
        blue_row, blue_col = top_left
        blue_col +=1

        #check boundaries
        if blue_col < output_grid.shape[1]:
          output_grid[blue_row, blue_col] = 1  # Place blue pixel

    return output_grid
```

