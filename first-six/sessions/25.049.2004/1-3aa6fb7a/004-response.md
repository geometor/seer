# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule can be summarized as follows:

1.  Identify the three distinct objects of azure color.
2. For the top-left object, turn to blue the rightmost cell.
2. For the middle object, turn to blue the leftmost cell.
2. For the bottom-left object, turn to blue the rightmost cell.
4. All other cells remain unchanged.
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

    # Sort objects by leftmost x coordinate, then topmost y coordinate.
    azure_objects.sort(key=lambda obj: (min(cell[1] for cell in obj), min(cell[0] for cell in obj)))

    # Ensure there are at least three objects
    if len(azure_objects) < 3:
        return output_grid

    # Find the rightmost cell of the top-left object (first object)
    top_left_object = azure_objects[0]
    rightmost_cell_top_left = max(top_left_object, key=lambda cell: cell[1])

    # Find the leftmost cell of the middle object (second object).
    middle_object = azure_objects[1]
    leftmost_cell_middle = min(middle_object, key=lambda cell: cell[1])

   # Find the rightmost cell of the bottom-left object (third object)
    bottom_left_object = azure_objects[2]
    rightmost_cell_bottom_left = max(bottom_left_object, key=lambda cell: cell[1])
    
    # Change the identified cells to color 1 (blue)
    output_grid[rightmost_cell_top_left[0], rightmost_cell_top_left[1]] = 1
    output_grid[leftmost_cell_middle[0], leftmost_cell_middle[1]] = 1
    output_grid[rightmost_cell_bottom_left[0], rightmost_cell_bottom_left[1]] = 1

    return output_grid
```

