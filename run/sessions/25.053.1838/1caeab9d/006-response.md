# 1caeab9d • 006 • refine_coder

---
```python
"""
The transformation aligns colored objects (red, blue, yellow) vertically while maintaining their relative horizontal positions. Objects move down as far as possible, stacking on top of objects of the same color, and being blocked by objects of other colors.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    objects = []

    def dfs(r, c, color, obj_coords):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        obj_coords.append((r, c))
        dfs(r + 1, c, color, obj_coords)
        dfs(r - 1, c, color, obj_coords)
        dfs(r, c + 1, color, obj_coords)
        dfs(r, c - 1, color, obj_coords)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                obj_coords = []
                dfs(r, c, color, obj_coords)
                # Find top-left and dimensions
                min_r = min(coord[0] for coord in obj_coords)
                min_c = min(coord[1] for coord in obj_coords)
                max_r = max(coord[0] for coord in obj_coords)
                max_c = max(coord[1] for coord in obj_coords)
                objects.append({
                    'color': color,
                    'position': (min_r, min_c),
                    'shape': (max_r - min_r + 1, max_c - min_c + 1),
                    'pixels': obj_coords
                })
    return objects

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find objects
    objects = find_objects(input_grid)

    # Sort objects by bottom row, then by top row (to handle cases with same bottom row)
    objects.sort(key=lambda obj: (max(r for r, c in obj['pixels']), min(r for r, c in obj['pixels'])), reverse=True)

    # Apply transformation rules
    for obj in objects:
        color = obj['color']
        max_drop = 0
        blocked = False

        # Check for blockage below
        for drop in range(1, input_grid.shape[0]): #check all the possible drop rows
            for r, c in obj['pixels']:
                new_r = r + drop #potential new row

                if new_r >= input_grid.shape[0]: #check if we hit the bottom
                    blocked = True
                    break

                if output_grid[new_r,c] != 0 and output_grid[new_r,c] != color:
                    blocked = True
                    break

            if blocked: #we're blocked, don't drop any further
                break
            else: #if we haven't been blocked, we can go one further.
                max_drop = drop

        # Update output grid
        for r, c in obj['pixels']:
            output_grid[r + max_drop, c] = color

    return output_grid
```
