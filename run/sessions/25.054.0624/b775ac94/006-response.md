# b775ac94 • 006 • refine_coder

---
```python
"""
1.  **Object Identification:** Identify all contiguous regions of non-zero pixels in the input grid. Each region is an object.

2.  **Flood Fill Expansion:** Each object expands outwards using a flood-fill algorithm. The flood fill expands to all adjacent (including diagonal) cells that are either background (color 0) or are part of the object's initial region.

3.  **Color Mixing during Flood Fill:** During the flood fill, the expanding object uses its original color. If a cell occupied by the object is adjacent to another object, then it may absorb the adjacent object's color.  When the color is absorbed, the absorbed color is flood-filled, from that cell outward, using the flood fill expansion rule.
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
                    if grid[nr, nc] == color:  # Only visit same-colored non-background pixels
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

def flood_fill(grid, start_r, start_c, color, visited, original_object_pixels):
    """Performs a flood fill, handling color absorption."""
    queue = deque([(start_r, start_c)])
    
    # if grid[start_r,start_c] == 0: # Check that starting with background
    grid[start_r, start_c] = color

    while queue:
        r, c = queue.popleft()

        neighbors = get_neighbors(grid, r, c)
        for nr, nc in neighbors:
            if (nr, nc) not in visited:
                # Expand to background or original object pixels
                if (nr, nc) in original_object_pixels or grid[nr,nc] == 0:
                    grid[nr, nc] = color
                    queue.append((nr, nc))
                    visited.add((nr,nc))


def transform(input_grid):
    """Transforms the input grid according to the flood fill and color absorption rules."""
    output_grid = np.zeros_like(input_grid)
    objects = find_objects(input_grid)
    visited = set() # global visited set for all flood fills

    # Perform flood fill for each object
    for object_pixels, color in objects:
      # add the initial object pixels to visited
      for r,c in object_pixels:
        visited.add((r,c))

    for object_pixels, color in objects:
      # Find contact point between different object for color absorbtion
        contact_points = []
        for r, c in object_pixels:
          output_grid[r,c] = color
          neighbors = get_neighbors(input_grid, r, c)
          for nr, nc in neighbors:
            if input_grid[nr,nc] != 0 and input_grid[nr,nc] != color:
                contact_points.append( (nr,nc,input_grid[nr,nc]) ) # store contact points

        # expand object's own color
        for r,c in object_pixels:
          flood_fill(output_grid,r,c, color, visited, object_pixels)

        # expand object's with adjacent object's color if exists
        for r, c, absorbed_color in contact_points:
          flood_fill(output_grid, r, c, absorbed_color, visited, object_pixels) # pass object

    return output_grid
```
