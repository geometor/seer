# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule is as follows:
1. Identify all azure (color 8) objects in the input grid.
2. Introduce blue (color 1) pixels adjacent to the identified azure objects.
3. Placement Rule:
    - Place a blue pixel (color 1) to the left of each azure object if the space to the left is empty (color 0).
    - Otherwise, if the space to the left is not empty, place a blue pixel to the right of the azure object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color in the grid.
    Returns a list of lists, each sublist containing coordinates of an object.
    """
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
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

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Get the leftmost coordinate of the object.
        leftmost_coord = min(obj, key=lambda coord: coord[1])

        # Try to place a blue pixel to the left.
        left_position = (leftmost_coord[0], leftmost_coord[1] - 1)
        if 0 <= left_position[1] < output_grid.shape[1] and output_grid[left_position] == 0:
            output_grid[left_position] = 1
        else:
            # If left placement is not possible, place to the right.
            rightmost_coord = max(obj, key=lambda coord: coord[1])
            right_position = (rightmost_coord[0], rightmost_coord[1] + 1)
            if 0 <= right_position[1] < output_grid.shape[1]:  # No need to check color, as right is only tried if left fails.
                output_grid[right_position] = 1
    
    return output_grid
```

