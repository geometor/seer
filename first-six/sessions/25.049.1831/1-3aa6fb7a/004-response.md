# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
The transformation rule identifies azure objects and adds a blue pixel adjacent to each, with the position of the new pixel (right or down) depending on the row index of the upper-leftmost pixel of the azure object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous objects of the specified color in the grid.
    Returns a list of lists, where each sublist contains the coordinates of an object's pixels.
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
        # Check adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_topmost_leftmost(obj):
    """
    Find the topmost, then leftmost coordinate of an object
    """
    return min(obj, key=lambda x: (x[0], x[1]))

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1. Identify azure (color 8) objects.
    2. Find the topmost and leftmost pixel for each azure object.
    3. Change cells to blue based on orientation.
    4. Preserve other objects in the output.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)
    
    # Iterate over the azure objects
    for obj in azure_objects:
        # Get topmost, leftmost pixel of each object
        topmost_leftmost = get_topmost_leftmost(obj)

        # Apply changes based on their locations
        r, c = topmost_leftmost
        
        if r <= 3:
           if c + 1 < output_grid.shape[1]: output_grid[r,c+1] = 1
        else:
           if r + 1 < output_grid.shape[0]: output_grid[r+1,c] = 1

    return output_grid
```

