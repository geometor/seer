# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule identifies all azure (color 8) objects and changes the color of the uppermost-leftmost cell of each object to blue (color 1).
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.

    Args:
        grid: The input grid.
        color: The color to search for.

    Returns:
        A list of lists, where each inner list contains the coordinates of
        contiguous cells of the specified color.
    """
    visited = set()
    objects = []

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = input_grid.copy()
    azure_objects = get_objects(input_grid, 8)

    # Iterate through each identified azure object.
    for obj in azure_objects:
        # Find the uppermost-leftmost cell within the current object.
        top_left_cell = min(obj, key=lambda cell: (cell[0], cell[1]))
        # Change the color of the identified cell to blue (color 1).
        output_grid[top_left_cell[0], top_left_cell[1]] = 1

    return output_grid
```

