# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
The transformation rule consists of adding a blue pixel (color 1) to the right side of the top-left pixel of each separate region of azure pixels (color 8).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected regions of the specified color in the grid.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        """Depth-First Search helper function."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))

        # Explore adjacent cells
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_top_left(object_coords):
    """
    Finds the top-left coordinate of an object.
    """
    min_row = float('inf')
    min_col = float('inf')
    for row, col in object_coords:
        if row < min_row:
            min_row = row
            min_col = col
        elif row == min_row and col < min_col:
            min_col = col
    return (min_row, min_col)

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Add a blue pixel (color 1) to the right of the top-left pixel of each separate region of azure pixels (color 8).
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # For each azure object, place a blue pixel to the right of its top-left pixel
    for obj in azure_objects:
        top_left = find_top_left(obj)
        blue_pixel_row = top_left[0]
        blue_pixel_col = top_left[1] + 1

        # Check boundaries before placing the blue pixel
        if 0 <= blue_pixel_row < output_grid.shape[0] and 0 <= blue_pixel_col < output_grid.shape[1]:
            output_grid[blue_pixel_row, blue_pixel_col] = 1

    return output_grid
```

