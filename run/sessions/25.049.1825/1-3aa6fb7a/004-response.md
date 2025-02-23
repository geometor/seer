# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
1.  **Identify Azure Objects:** Locate all objects (contiguous regions) of color 8 (azure) in the input grid.
2.  **Preserve Azure Objects:** The shape, size, and location of all azure colored objects are kept the same in the output grid.
3.  **Change color to blue:** Go over the cells of the azure objects one by one, starting from top to bottom. For each azure object, locate the azure color cell that is highest and furthest to the *left*. Change the color of this cell from 8 (azure) to 1 (blue).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of sets, where each set contains the coordinates of an object.
    """
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        """
        Depth-First Search helper to find connected cells of the same color.
        """
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.add((row, col))
        # Check adjacent cells (up, down, left, right)
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = set()
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the highest (min row) and *leftmost* (min col) cell
        top_left_cell = None
        for row, col in obj:
            if top_left_cell is None:
                top_left_cell = (row, col)
            else:
                if row < top_left_cell[0] or (row == top_left_cell[0] and col < top_left_cell[1]):
                    top_left_cell = (row,col)


        # Change the color of the top-left cell to blue (1)
        output_grid[top_left_cell] = 1

    return output_grid
```

