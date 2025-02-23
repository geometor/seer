# 2-0ca9ddb6 • 006 • Response

---

*text:*

```python
"""
The transformation preserves the position and color of the initial red and blue cells and frames those cells with a cross of the same size. The cross surrounding the red cell is color 4, while the cross surrounding the blue cell is color 7. The magenta object (color 6) is also preserved.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    objects = []
    for i in range(len(coords[0])):
        objects.append((coords[0][i], coords[1][i]))  # return row, col
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the red objects (color 2).
    red_objects = find_objects(input_grid, 2)
    for red_pos in red_objects:
        row, col = red_pos
        # Frame the red object with yellow (color 4).
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 4

    # Find the blue objects (color 1).
    blue_objects = find_objects(input_grid, 1)
    for blue_pos in blue_objects:
        row, col = blue_pos
        # Frame the blue object with orange (color 7).
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 7

    return output_grid
```

