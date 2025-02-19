# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule identifies two azure (8) L-shaped objects in the input grid.
It changes the color of the white cell (0) to the right of the top cell of the top-left object to blue (1).
It also changes the color of the white cell (0) to the left of the bottom cell of the bottom-right object to blue (1).
The rest of the grid remains unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds connected regions of the specified color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-first search to find connected cells."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
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

def get_top_cell(obj):
    """Returns the cell with the smallest row value (top-most)."""
    return min(obj, key=lambda cell: cell[0])

def get_bottom_cell(obj):
    """Returns the cell with the largest row value."""
    return max(obj, key=lambda cell:cell[0])
def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Sort objects based on top-left corner's row, then column
    azure_objects.sort(key=lambda obj: (get_top_cell(obj)[0], get_top_cell(obj)[1]))

    if len(azure_objects) >= 2:

        top_left_object = azure_objects[0]
        bottom_right_object = azure_objects[-1] #select the object in the bottom-right

        #process top-left object
        top_cell = get_top_cell(top_left_object)
        right_cell = (top_cell[0], top_cell[1] + 1)

        if (
            0 <= right_cell[0] < output_grid.shape[0]
            and 0 <= right_cell[1] < output_grid.shape[1]
            and output_grid[right_cell] == 0
        ):
            output_grid[right_cell] = 1

        #process bottom-right
        bottom_cell = get_bottom_cell(bottom_right_object)
        left_cell = (bottom_cell[0], bottom_cell[1]-1)

        if (
            0 <= left_cell[0] < output_grid.shape[0]
            and 0 <= left_cell[1] < output_grid.shape[1]
            and output_grid[left_cell] == 0
            ):
                output_grid[left_cell] = 1

    return output_grid
```
