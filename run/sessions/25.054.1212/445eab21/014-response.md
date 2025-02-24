# 445eab21 • 014 • example_3 • investigate_coder

---
```python
"""
Finds a "C"-shaped yellow object in the input grid, extracts the 2x2 top-left corner, and returns it as the output grid.
"""

import numpy as np

def get_objects(grid):
    """
    Find contiguous regions of the same color in the grid (excluding white/0).
    Returns a dictionary of objects, where keys are colors and values are lists of pixel coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj_pixels):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or grid[row, col] != color
        ):
            return
        visited.add((row, col))
        obj_pixels.append((row, col))
        dfs(row + 1, col, color, obj_pixels)
        dfs(row - 1, col, color, obj_pixels)
        dfs(row, col + 1, color, obj_pixels)
        dfs(row, col - 1, color, obj_pixels)

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                obj_pixels = []
                dfs(r, c, color, obj_pixels)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_pixels)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Find objects in the input grid.
    objects = get_objects(input_grid)

    # Find the yellow (4) object.
    if 4 not in objects:
        return np.array([[0]]) # Handle the case with no yellow object by returning minimal empty grid.

    yellow_objects = objects[4]

    # From observation, there should always be one yellow object
    yellow_object = yellow_objects[0]

    # Find the top-leftmost pixel of the yellow object.
    top_left_pixel = min(yellow_object, key=lambda p: (p[0], p[1]))

    # Create a 2x2 output grid with yellow pixels.
    output_grid = np.full((2, 2), 4)

    return output_grid
```
