# 0e206a2e • 010 • refine_coder

---
```python
"""
Colored objects from the input grid are reconstructed in the output grid.
The reconstruction maintains the shape, size, and color of each distinct object,
but changes their position. Objects are positioned based on their original
color, creating an abstract shape that depends on objects found in the input.
"""

import numpy as np

def find_objects(grid):
    """
    Finds and returns a dictionary of colored objects in the grid.
    Each object is a list of (row, col) coordinates.
    """
    objects = {}
    visited = set()

    def dfs(row, col, color, obj):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            color = grid[row, col]
            if color != 0 and (row, col) not in visited:
                obj = []
                dfs(row, col, color, obj)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj)
    return objects

def transform(input_grid):
    # Initialize output grid with zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Reconstruct objects in output grid
    for color, object_list in objects.items():
        for obj in object_list:
            for r, c in obj:
                output_grid[r,c] = color

    return output_grid
```
