# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
Identifies single-celled azure (8) objects in the input grid and replaces them with blue (1) objects in the output grid. All other azure colored objects, and other cells, are preserved.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous objects of the same color in a grid.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    visited = set()
    objects = []

    def dfs(row, col, color, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, color, current_object)
        dfs(row - 1, col, color, current_object)
        dfs(row, col + 1, color, current_object)
        dfs(row, col - 1, color, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if (row, col) not in visited:
                current_object = []
                dfs(row, col, grid[row, col], current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule: single-cell azure objects
    are replaced with blue, while multi-celled azure objects and background are preserved.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Get all objects in the grid
    objects = get_objects(input_grid)

    # Iterate through the objects
    for obj in objects:
        # Check if the object is azure (color 8) and has a size of 1
        if len(obj) == 1 and input_grid[obj[0][0], obj[0][1]] == 8:
            # Replace the single-cell azure object with blue (color 1)
            output_grid[obj[0][0], obj[0][1]] = 1

    return output_grid
```

