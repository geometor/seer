# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule identifies two azure L-shaped objects and paints the uppermost-leftmost cell blue of the top L-shaped object and the leftmost-uppermost blue of the bottom one.
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

    # change color of uppermost-leftmost azure cell of top object
    if len(azure_objects) >= 1:
      top_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      top_left_cell = min(top_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[top_left_cell[0], top_left_cell[1]] = 1

    # change color of leftmost-uppermost azure cell of bottom object
    if len(azure_objects) >= 2:
      # find bottom-right object by minimum row and then minimum col
      bottom_object = max(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r,c in obj)))
      bottom_left_cell = min(bottom_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[bottom_left_cell[0],bottom_left_cell[1]] = 1
    
    return output_grid
```
