# aabf363d • 004 • refine_coder

---
```python
"""
Identifies a contiguous object and a single isolated pixel in the input grid. Replaces the contiguous object with the color of the single isolated pixel and removes the original isolated pixel.
"""

import numpy as np

def find_contiguous_object(grid):
    """Finds a contiguous object in the grid."""
    visited = set()
    object_coords = []

    def dfs(row, col, color):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        object_coords.append((row, col))
        dfs(row + 1, col, color)
        dfs(row - 1, col, color)
        dfs(row, col + 1, color)
        dfs(row, col - 1, color)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] != 0 and (r,c) not in visited:
                color = grid[r, c]
                dfs(r, c, color)
                if len(object_coords) > 1: # ensure that it is more than a single pixel
                    return object_coords
                else:
                    object_coords = [] # reset if it is a single pixel

    return None

def find_single_pixel(grid):
    """Finds a single isolated pixel of any color."""
    counts = {}
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            color = grid[r,c]
            if color != 0:
              if color not in counts:
                counts[color] = 0
              counts[color] += 1

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            color = grid[r,c]
            if color != 0 and counts[color] == 1:
              return (r, c), color
    return None, None
    


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the contiguous object.
    object_coords = find_contiguous_object(input_grid)

    # Find the single isolated pixel and its color.
    pixel_coord, replacement_color = find_single_pixel(input_grid)

    # Change the color of the object to the replacement color in the output_grid.
    if object_coords and replacement_color is not None:
        for row, col in object_coords:
            output_grid[row, col] = replacement_color

    # Remove the original isolated pixel.
    if pixel_coord:
      output_grid[pixel_coord[0], pixel_coord[1]] = 0

    return output_grid
```
