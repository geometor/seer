# 3befdf3e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is an expansion of both the outer yellow rectangle and the inner magenta cell. The yellow rectangle expands outwards by one cell in all directions, and the magenta cell expands to a 3x3 rectangle.
"""

import numpy as np

def get_objects(grid):
    """Finds distinct objects in the grid based on color contiguity."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                object_coords = []
                queue = [(r, c)]
                visited[r, c] = True

                while queue:
                    curr_r, curr_c = queue.pop(0)
                    object_coords.append((curr_r, curr_c))

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r, new_c] and grid[new_r, new_c] == color:
                            queue.append((new_r, new_c))
                            visited[new_r, new_c] = True

                objects.append((color, object_coords))
    return objects
def transform(input_grid):
    """Transforms the input grid according to the expansion rule."""

    # Initialize output grid with zeros
    output_grid = np.zeros_like(input_grid)

    # Get objects from the input grid
    objects = get_objects(input_grid)

    yellow_object = None
    magenta_object = None

    for color, coords in objects:
        if color == 4:
            yellow_object = coords
        elif color == 6:
            magenta_object = coords

    # Expand yellow object
    if yellow_object:
        min_r = min(r for r, c in yellow_object)
        max_r = max(r for r, c in yellow_object)
        min_c = min(c for r, c in yellow_object)
        max_c = max(c for r, c in yellow_object)

        for r in range(min_r - 1, max_r + 2):
            for c in range(min_c - 1, max_c + 2):
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 4

    # Expand magenta object
    if magenta_object:
        center_r = magenta_object[0][0]  # Assuming it's a single cell
        center_c = magenta_object[0][1]

        for r in range(center_r - 1, center_r + 2):
            for c in range(center_c - 1, center_c + 2):
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 6

    return output_grid
```
