# 1-3aa6fb7a • 006 • refine_code - CODE

---
```python
"""
This transformation identifies azure objects, classifies them into a "vertical line" and a "reversed L" shape, and adds a blue pixel inside each of them. The position of the blue pixel depends on the object's shape.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

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

def classify_object(object_pixels):
    """Classifies an object as 'vertical line' or 'reversed L' or 'other'."""
    rows = [p[0] for p in object_pixels]
    cols = [p[1] for p in object_pixels]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    if max_row - min_row > max_col - min_col and max_col == min_col: # Check for vertical line
        return "vertical line"
    elif len(object_pixels) == 4:
       if max_row - min_row == 1 and max_col - min_col == 1:
           return "reversed L"
    return "other"

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find azure objects
    azure_objects = find_objects(input_grid, 8)  # 8 is for azure
    
    for obj in azure_objects:
        object_type = classify_object(obj)

        if object_type == "vertical line":
            obj.sort()  # Sort by row, then column
            row = obj[1][0]
            col = obj[1][1]
            output_grid[row, col + 1] = 1  # Add blue pixel to the right
        
        elif object_type == "reversed L":
            obj.sort() # Sort to find top-left
            row = obj[0][0]
            col = obj[0][1]
            output_grid[row + 1, col] = 1  # Add a blue pixel one row down
    
    return output_grid
```
