# 0e206a2e • 012 • refine_coder

---
```python
"""
Colored objects from the input grid are reconstructed in the output grid.
The reconstruction maintains the shape, size, and color of each distinct object,
but changes their position. Objects are positioned based on their original
color, creating an abstract shape that depends on objects found in the input, placing them near the bottom.
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
    output_grid_height = input_grid.shape[0]
    output_grid_width = input_grid.shape[1]
    output_grid = np.zeros((output_grid_height, output_grid_width), dtype=int)

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Determine starting row for placement (start near the bottom)
    current_row = output_grid_height - 1

    # Reconstruct objects in output grid
    for color in sorted(objects.keys()):  # Iterate through colors in a consistent order
        for obj in objects[color]:
            object_height = max(r for r, c in obj) - min(r for r, c in obj) + 1
            
            # Check for enough space, move up if needed
            if current_row - object_height +1 < 0:
                current_row = output_grid_height-1 # reset to bottom if no more room at top
            
            # Find the bounding box of object
            min_row = min(r for r, c in obj)
            min_col = min(c for c, c in obj)

            # place object, using an offset for the new position            
            for r, c in obj:
                output_row = current_row - (max(r_temp for r_temp,c_temp in obj) - r)
                output_col = c - min_col  # maintain the original column order relative to min_col
                output_grid[output_row, output_col] = color
            current_row -= object_height # move 'cursor' up by object height


    return output_grid
```
