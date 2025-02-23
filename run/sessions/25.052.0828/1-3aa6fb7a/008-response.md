# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
1. Identify Azure Objects: Locate all connected regions (objects) of color 8 (azure) in the input grid.

2. Process Each Azure Object: For each identified azure object:
   - Check for Vertical Line: Determine if the object is a vertical line. A vertical line has all its cells in the same column. Also, a vertical line has a length of 2.
   - Vertical Line Action: If it's a vertical line of length 2, place a blue (color 1) pixel immediately to the *right* of the *top-most* cell of the azure line.
   - Other Shapes (Horizontal Line and others): if the object is not vertical, place a blue pixel immediately *to the left* of the *right-most* cell of the azure object.
   - Boundary condition: Check that after calculating the position where a blue pixel will be added, this new position is inside the boundaries of the image.

3. Preserve Other Colors: All other cells in the input grid that are not part of the processed azure objects remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected components of a specific color in the grid.
    Returns a list of lists, where each inner list contains the coordinates of an object.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return []

        visited.add((x, y))
        object_coords = [(x, y)]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            object_coords.extend(dfs(x + dx, y + dy))

        return object_coords

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color:
                found_object = dfs(x, y)
                if found_object:
                    objects.append(found_object)

    return objects

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort by x and then y to find top-most point
        sorted_by_x = sorted(obj, key=lambda p: (p[0], p[1]))
        top_most = sorted_by_x[0]

        # Sort by y in reverse order to find right-most point
        sorted_by_y_desc = sorted(obj, key=lambda p: p[1], reverse=True)
        right_most = sorted_by_y_desc[0]

        # Check if it's a vertical line (all y-coordinates are the same) and length is 2
        if all(p[1] == sorted_by_x[0][1] for p in sorted_by_x) and len(obj) == 2:
            # Place blue to the right of the top-most cell
            new_x, new_y = top_most[0], top_most[1] + 1
            if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
                output_grid[new_x, new_y] = 1
        else:
            # Place blue to the left of the right-most cell
            new_x, new_y = right_most[0], right_most[1] - 1
            if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
                output_grid[new_x, new_y] = 1

    return output_grid
```

