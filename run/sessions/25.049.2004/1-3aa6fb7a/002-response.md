# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule is the following.
1. Identify the rightmost cell of color 8 in the left object, and change it to color 1 (blue).
2. Identify the leftmost cell of color 8 in the rigth object, and change it to color 1 (blue).
All other cells remain the same.
"""

import numpy as np

def find_objects(grid, color):
    # Find all cells matching the specified color.
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def dfs(r, c, current_object):
        # Depth-first search to find contiguous regions of the same color.
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Handle edge case: No azure object
    if not azure_objects:
      return output_grid

    # Sort objects by leftmost x coordinate.
    azure_objects.sort(key=lambda obj: min(cell[1] for cell in obj))

    # Ensure there are at least two objects
    if len(azure_objects) < 2:
      return output_grid
    
    # Find the rightmost cell of the leftmost object (first object)
    left_object = azure_objects[0]
    rightmost_cell = max(left_object, key=lambda cell: cell[1])

    # Find the leftmost cell of the rightmost object (second object).
    right_object = azure_objects[-1]
    leftmost_cell = min(right_object, key=lambda cell: cell[1])

    # Change the identified cells to color 1 (blue)
    output_grid[rightmost_cell[0], rightmost_cell[1]] = 1
    output_grid[leftmost_cell[0], leftmost_cell[1]] = 1
    
    return output_grid
```
