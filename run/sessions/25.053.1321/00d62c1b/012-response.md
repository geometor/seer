# 00d62c1b • 012 • refine_coder

---
```python
"""
Locate all contiguous regions (objects) of '3' (green) pixels in the input grid. Within each identified green object, change all pixels that were originally '3' to '4' (yellow). Pixels not part of a green object remain unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return []

    # Start with the first coordinate as the seed.
    seed = tuple(coords[0])
    object_coords = set()
    object_coords.add(seed)
    queue = [seed]

    # Perform a breadth-first search to find all connected pixels.
    while queue:
        current = queue.pop(0)
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # 4-connectivity
        for nx, ny in neighbors:
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == color:
                neighbor_coord = (nx, ny)
                if neighbor_coord not in object_coords:
                    object_coords.add(neighbor_coord)
                    queue.append(neighbor_coord)
    return list(object_coords)

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the object with color '3' (green).
    object_coords = find_object(output_grid, 3)

    if not object_coords:
        return output_grid # no green object

    # change all '3's in object to '4'
    for coord in object_coords:
      output_grid[coord] = 4

    return output_grid
```
