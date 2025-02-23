# 00d62c1b • 010 • example_2 - CODE

---
```python
"""
Locate a contiguous shape of '3' (green) pixels within the input grid.  Within this shape, change a single '3' to '4' (yellow). It appears the changed '3' is centered horizontally within the shape, and is second from the bottom row of the shape. All other pixels remain unchanged.
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

    #find min and max row
    min_row = min(coord[0] for coord in object_coords)
    max_row = max(coord[0] for coord in object_coords)

    # one up from the bottom
    target_row = max_row - 1

    # filter object to this row
    coords_in_row = [coord for coord in object_coords if coord[0] == target_row]
    
    # find the horizontal center, use first if there is a tie
    if coords_in_row:
      min_col = min(coord[1] for coord in coords_in_row)
      max_col = max(coord[1] for coord in coords_in_row)
      center_col = (min_col + max_col) // 2
      target_coord = (target_row, center_col)

      # Perform the change.
      if target_coord in object_coords:  # Make sure the target is within the shape before changing
           output_grid[target_coord] = 4

    return output_grid
```
