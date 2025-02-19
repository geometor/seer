# 1-3aa6fb7a • 002 • example_1 - CODE

---

*text:*

```python
"""
This program transforms an input grid by identifying two L-shaped objects of color 8 (azure),
and changing the color of the corner pixel of each L-shape to color 1 (blue).

1. Find the azure (8) colored objects in the grid.
2. Find the corners of the two L-shapes. The coordinates are (1, 2) and (5,5).
3. Paint the corner cells of the azure shapes to blue (1).
4. Keep other azure pixels.
5. Keep other grid colors.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))

        # Check all 8 neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                dfs(x + dx, y + dy, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def find_l_corners(obj):
    # Find the corner of an L-shape object
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    coords = {}
    for x,y in obj:
      if (x,y) in coords:
        coords[(x,y)] += 1
      else:
        coords[(x,y)] = 1

    corners = []
    for key in coords.keys():
      if coords[key] > 1:
        corners.append(key)

    if len(corners) > 0:
      if len(obj) == 3:
         return corners[0]

    return None

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Find and change L-shape corners to blue
    for obj in azure_objects:
        corner = find_l_corners(obj)
        if corner:
            output_grid[corner[0], corner[1]] = 1

    return output_grid
```
