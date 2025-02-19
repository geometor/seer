# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule is to change the color of the top-right azure pixel of each azure shape to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds and returns a list of objects of a specific color.
    An object is defined as a contiguous region of the same color.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_top_right(obj):
    """Finds the top-right pixel of a given object."""
    # Sort by column (ascending) then by row (ascending)
    sorted_obj = sorted(obj, key=lambda x: (x[1],x[0]))
    top_right = sorted_obj[-1]

    return top_right
def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure (8) shape, change the color of the top-right pixel to blue (1).
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)
    
    # Iterate through each azure object
    for obj in azure_objects:
      #find top right corner of the object
      top_right = find_top_right(obj)
      # Change the color of the top-right pixel to blue
      output_grid[top_right[0],top_right[1]] = 1
    
    return output_grid
```

