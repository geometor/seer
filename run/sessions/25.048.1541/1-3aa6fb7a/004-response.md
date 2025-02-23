# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
For each disconnected azure (color 8) object, place a blue pixel (color 1) to the immediate right of the highest azure pixel in that object. If the position is not empty (occupied by another color), do not apply the change.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds disconnected objects of a given color in the grid.
    Returns a list of lists, where each inner list contains the coordinates of an object's pixels.
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
    Transforms the input grid according to the rule: For each disconnected azure (color 8) object,
    place a blue pixel (color 1) to the immediate right of the highest azure pixel in that object.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(output_grid, 8)

    for obj in azure_objects:
        # Find the highest pixel (lowest row index)
        highest_pixel = min(obj, key=lambda x: x[0])

        # Calculate the position to the right
        right_position = (highest_pixel[0], highest_pixel[1] + 1)

        # Check bounds and if the position is empty (color 0)
        if 0 <= right_position[0] < output_grid.shape[0] and 0 <= right_position[1] < output_grid.shape[1] and output_grid[right_position[0], right_position[1]] == 0:
            output_grid[right_position[0], right_position[1]] = 1

    return output_grid
```

