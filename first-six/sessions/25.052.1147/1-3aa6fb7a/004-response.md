# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation preserves all existing azure (8) objects and adds a blue (1) pixel adjacent to each azure object, either to the left or right.  The placement appears to follow a pattern: if the azure object is in the upper half of the grid, the blue pixel is placed to the right or left; if it is in the lower half, the blue pixel seems to appear to the left, although this rule doesn't perfectly describe the second example. A more precise rule is that a blue pixel is added adjacent to the *rightmost* column of any azure object segment and/or adjacent to the *leftmost* column.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds all contiguous objects of a given color in the grid.
    Returns a list of lists, where each inner list contains the (row, col) coordinates of an object.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the leftmost and rightmost columns of the object
        min_col = min(obj, key=lambda x: x[1])[1]
        max_col = max(obj, key=lambda x: x[1])[1]

        # Add a blue pixel to the left of the leftmost column, if possible
        if min_col > 0:
            # Find a cell in this object that is in the leftmost column
            for r, c in obj:
                if c == min_col:
                    output_grid[r, min_col - 1] = 1
                    break  # Only add one blue pixel per object

        # Add a blue pixel to the right of the rightmost column, if possible
        if max_col < input_grid.shape[1] - 1:
            # Find a cell in this object that is in the rightmost column
            for r, c in obj:
                if c == max_col:
                    output_grid[r, max_col + 1] = 1
                    break # Only add one blue pixel per object


    return output_grid
```

