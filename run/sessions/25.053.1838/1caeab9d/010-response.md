# 1caeab9d • 010 • refine_coder

---
```python
"""
The transformation takes the separate colored rectangles and places them side-by-side in a single row, preserving the original left-to-right order. The row is chosen to be large enough to contain the largest object in the grid.
"""

import numpy as np

def find_objects(grid):
    """
    Finds rectangular blocks of uniform color (excluding white/0) in the grid.
    Returns a list of dictionaries, each representing an object.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                # Start BFS to find the extent of the object
                queue = [(r, c)]
                visited[r, c] = True
                min_row, max_row = r, r
                min_col, max_col = c, c

                while queue:
                    curr_row, curr_col = queue.pop(0)
                    min_row = min(min_row, curr_row)
                    max_row = max(max_row, curr_row)
                    min_col = min(min_col, curr_col)
                    max_col = max(max_col, curr_col)

                    # Check neighbors
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_row, new_col = curr_row + dr, curr_col + dc
                        if 0 <= new_row < rows and 0 <= new_col < cols and \
                           not visited[new_row, new_col] and grid[new_row, new_col] == color:
                            queue.append((new_row, new_col))
                            visited[new_row, new_col] = True

                objects.append({
                    'color': color,
                    'top_left': (min_row, min_col),
                    'bottom_right': (max_row, max_col)
                })

    return objects


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    input_height = input_grid.shape[0]

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Sort objects by their leftmost column
    objects.sort(key=lambda obj: obj['top_left'][1])

    # change output pixels
    # Concatenate objects horizontally
    current_col = 0
    max_height = 0
    for obj in objects:
      obj_height = obj['bottom_right'][0] - obj['top_left'][0] + 1
      max_height = max(max_height, obj_height)
    target_row = max(input_height // 2 - max_height // 2, 0)

    for obj in objects:
      obj_height = obj['bottom_right'][0] - obj['top_left'][0] + 1
      obj_width =  obj['bottom_right'][1] - obj['top_left'][1] + 1
      for r in range(obj_height):
        for c in range(obj_width):
            output_grid[target_row + r, current_col + c] = obj['color']
      current_col += obj_width

    return output_grid
```
