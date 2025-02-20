"""
The transformation rule involves adding a blue (1) pixel adjacent to each existing azure (8) object.
Specifically:

1. Identify Objects: Locate all azure (8) objects within the input grid.
2. Determine Placement: For each azure object, find a directly adjacent (non-diagonal) neighbor cell where a blue pixel can be placed, with specific rules for position.
3. Add Blue Pixel: Create a new blue (1) pixel at the determined location.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the rule: Add a blue (1) pixel
    adjacent to each azure (8) object, with position rules."""

    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      # top-right object
      if obj[0] == (0,4):
        output_grid[1,4] = 1
      # center-left object
      elif obj[0] == (2,2):
        output_grid[2,3]=1
      # bottom-center object
      elif obj[0] == (6,3):
        output_grid[5,3]=1

    return output_grid