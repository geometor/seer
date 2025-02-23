# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
Identifies connected regions of color 8 (azure) in the input grid, sorts them horizontally, and changes the color of specific adjacent cells to 1 (blue) based on the object's position.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected components of the specified color in the grid.
    Uses depth-first search (DFS).
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def sort_objects(objects):
    """
    Sorts objects based on their leftmost column (minimum column index).
    """
    return sorted(objects, key=lambda obj: min(col for _, col in obj))

def get_topmost_cell(object_cells):
    """Returns the topmost cell (minimum row index) of an object."""
    return min(object_cells, key=lambda cell: cell[0])

def get_bottommost_cell(object_cells):
    """Returns the bottommost cell (maximum row index) of an object."""
    return max(object_cells, key=lambda cell: cell[0])


def transform(input_grid):
    """
    Transforms the input grid: finds azure objects, sorts them, and modifies adjacent cells.
    """
    output_grid = np.copy(input_grid)  # Initialize output as a copy of input

    # Find objects of color 8
    objects = find_objects(output_grid, 8)

    # Sort objects from left to right
    sorted_objects = sort_objects(objects)

    # Process leftmost object: change cell to the right of its topmost cell to blue
    if sorted_objects:
        leftmost_object = sorted_objects[0]
        topmost_cell = get_topmost_cell(leftmost_object)
        right_neighbor = (topmost_cell[0], topmost_cell[1] + 1)
        if 0 <= right_neighbor[1] < output_grid.shape[1]:
            output_grid[right_neighbor] = 1

    # Process rightmost object: change cell to the left of its bottommost cell to blue
    if len(sorted_objects) > 0: # changed from >= to >
        rightmost_object = sorted_objects[-1]
        bottommost_cell = get_bottommost_cell(rightmost_object)
        left_neighbor = (bottommost_cell[0], bottommost_cell[1] - 1)
        if 0 <= left_neighbor[1] < output_grid.shape[1]:
            output_grid[left_neighbor] = 1

    return output_grid
```
