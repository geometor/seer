# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule identifies azure (8) objects in the input grid and preserves them in the output grid. 
A blue (1) pixel is added adjacent to each azure object, following a specific rule based on the object's orientation:

1. Horizontal lines: A blue pixel is placed to the left of the left-most pixel.
2. Vertical lines: A blue pixel is placed above the top-most pixel.
The order is left for the first object, top for the second object and left for the third object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specified color in the grid.
    Returns a list of coordinates (row, col) for each object.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid based on the described rules.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    object_count = len(azure_objects)
    
    for i in range(min(object_count, 3)): # Limit processing to the first three objects
        if i == 0 or i == 2:  # Left for first and third
            obj = sorted(azure_objects[i], key=lambda x: x[1])
            left_pixel = obj[0]
            output_grid[left_pixel[0], left_pixel[1] - 1] = 1
        elif i == 1: # Up for the second
            obj = sorted(azure_objects[i], key=lambda x: x[0])
            top_pixel = obj[0]
            output_grid[top_pixel[0] - 1, top_pixel[1]] = 1
            
    return output_grid
```

