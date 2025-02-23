# 3e980e27 • 004 • example_2 - CODE

---
```python
"""
The transformation rule involves identifying blue and red objects, preserving red objects, and copying, mirroring, and translating the blue objects based on the position of the bottom-right red object.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def mirror_object(object_coords, red_coords):
    """Mirrors the object coordinates with respect to the red object coordinates."""
    mirrored_coords = []
    r_ref, c_ref = red_coords
    for r, c in object_coords:
        mirrored_coords.append((r + 2 * (r_ref - r), c + 2 * (c_ref - c)))
    return mirrored_coords

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find red objects
    red_objects = find_objects(input_grid, 2)
    # Find blue objects
    blue_objects = find_objects(input_grid, 1)

    # Assume the translation reference is the last red object (bottom-right)
    if red_objects:
        red_ref_row, red_ref_col = red_objects[-1][0]

        for blue_object in blue_objects:
            # Mirror the blue object
            mirrored_blue_object = mirror_object(blue_object, (red_ref_row, red_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_blue_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 1

    return output_grid.tolist()
```

