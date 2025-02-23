"""
1.  **Identify Objects:** Find all contiguous clusters of non-zero pixels in the input grid. Each cluster is an object.
2.  **Object Expansion:** Each object attempts to expand.
3.  **Expansion Rules:**
    *   An object expands horizontally and/or vertically into adjacent (including diagonally) background (0-colored) pixels.
    *   If an object is adjacent to another object, it may take on some of other objects color during expansion, as long as the color is adjacent. The color will extend in alternating lines.
"""

import numpy as np
from collections import deque

def find_objects(grid):
    """Finds contiguous objects in the grid."""
    visited = set()
    objects = []

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        object_pixels = []
        color = grid[start_r, start_c]

        while queue:
            r, c = queue.popleft()
            object_pixels.append((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and (nr, nc) not in visited:
                    if grid[nr,nc] == color or grid[nr, nc] == 0:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        return object_pixels, color

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0 and (r, c) not in visited:
                objects.append(bfs(r, c))

    return objects

def get_neighbors(grid, r, c):
    """Gets the valid neighbors (including diagonals) of a pixel."""
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
            neighbors.append((nr, nc))
    return neighbors


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # find objects
    objects = find_objects(input_grid)
    
    # expand the object
    expanded_objects = []
    for obj_pixels, color in objects:
        new_pixels = obj_pixels.copy()
        for r,c in obj_pixels:
            neighbors = get_neighbors(input_grid, r, c)
            for nr, nc in neighbors:
                if input_grid[nr,nc] == 0:
                   new_pixels.append((nr,nc))
        expanded_objects.append( (new_pixels, color) )

    # apply identified object changes and expansion to output
    for obj_pixels, color in expanded_objects:
      for (r,c) in obj_pixels:
        output_grid[r,c] = color

    # apply identified object changes with alternating adjacent object colors
    for obj_pixels, color in expanded_objects:
        for r, c in obj_pixels:
            neighbors = get_neighbors(output_grid, r, c)
            neighbor_colors = [output_grid[nr, nc] for nr, nc in neighbors if output_grid[nr, nc] != 0 and output_grid[nr,nc] != color]
            if neighbor_colors:
                # Simple alternation - could be more sophisticated based on row/col
                alt_color = neighbor_colors[0]
                if (r + c) % 2 == 0:  # Alternate based on row+col parity
                  for nr,nc in neighbors:
                    if output_grid[nr,nc] == 0:
                      output_grid[nr, nc] = alt_color

    return output_grid