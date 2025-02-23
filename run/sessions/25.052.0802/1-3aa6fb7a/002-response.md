# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves the azure (8) objects and adds a blue cell (1) next to it, to its right if it is a vertical line, and to its left if it is a horizontal line.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(x + dx, y + dy, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def is_vertical_line(obj, grid):
    #Checks if an object is a vertical line.

    if len(obj) < 2:
        return False

    xs = [p[0] for p in obj]
    ys = [p[1] for p in obj]

    if len(set(ys)) == 1: #all in the same column
        return True
    return False

def is_horizontal_line(obj, grid):
   # Checks if an object is a horizontal line

    if len(obj) < 2:
        return False

    xs = [p[0] for p in obj]
    ys = [p[1] for p in obj]

    if len(set(xs)) == 1:  # All in the same row
        return True
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    # Find all objects with color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        if is_vertical_line(obj, input_grid):
          #add blue to the right
          obj_sorted_by_row = sorted(obj, key = lambda p: p[0])
          highest_row_point = obj_sorted_by_row[-1]
          new_x = highest_row_point[0]
          new_y = highest_row_point[1] + 1
          if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
            output_grid[new_x, new_y] = 1

        elif is_horizontal_line(obj, input_grid):
          # add blue to the left
          obj_sorted_by_col = sorted(obj, key=lambda p: p[1])
          lowest_col_point = obj_sorted_by_col[0]

          new_x = lowest_col_point[0]
          new_y = lowest_col_point[1] - 1
          if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
             output_grid[new_x, new_y] = 1

    return output_grid
```
