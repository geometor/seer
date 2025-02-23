# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
The input features azure squares. These objects do not move.
The corner of azure shapes should be converted to blue.
"""

import numpy as np

def find_objects(grid, color):
    # Find objects of a specific color in the grid
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects
def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Azure shapes should be converted blue.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)
    
    # change the color
    for obj in azure_objects:
      if len(obj) > 1:
        obj.sort()
        if obj[0][0] == obj[1][0]: # Vertical shape
          output_grid[obj[1][0],obj[1][1]] = 1

        elif obj[0][1] == obj[1][1]:
          output_grid[obj[0][0],obj[0][1]] = 1
    return output_grid
```

