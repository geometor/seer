# 1-3aa6fb7a • 004 • refine_code - CODE

---
```python
"""
1. Identify Azure (color 8) Objects: Find all connected components of azure-colored pixels.
2. Filter L-Shapes: From the azure objects, select only those that form an "L" shape. An "L" shape is defined as a set of 3 pixels, where two pixels share an edge, and the third pixel shares an edge with only *one* of the first two.
3. Identify Corner point for each L shape. Corner point is the pixel that has two neighbors with the same color.
4. Change Pixel Colors at Corner Points: For *every* identified "L" shape, change the color of its corner point to blue (color 1).
5. Copy everything. The output is the input grid, with the color modification.
"""

import numpy as np

def is_l_shape(pixels, grid):
    """Checks if a set of pixels forms an L-shape."""
    if len(pixels) != 3:
        return False, None

    # Convert list of tuples to numpy array for easier manipulation
    pixels_arr = np.array(pixels)

    # Find the pixel that has two neighbors
    for i, (x, y) in enumerate(pixels):
        neighbors = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) in pixels:
                neighbors += 1
        if neighbors == 2:
            return True, (x, y)
    return False, None

def find_objects(grid, color):
    """Finds connected components of a specific color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_object.append((x, y))

        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    azure_objects = find_objects(output_grid, 8)

    for obj in azure_objects:
        is_l, corner_pixel = is_l_shape(obj, output_grid)
        if is_l:
            output_grid[corner_pixel] = 1

    return output_grid
```

