"""
Transformation Rule:

1. Identify Azure Objects: Locate all azure (color 8) objects in the input grid.  There are two separate azure objects.
2. Change corner to blue: If a corner piece of the object exists, change it to blue.
3. Preserve Other Azure Cells: All other azure cells that are not corner cells remain unchanged.
4. Preserve background: All white cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates.
    """
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
            if grid[r,c] == color and (r,c) not in visited:
                current_object = []
                dfs(r,c,current_object)
                objects.append(current_object)

    return objects

def find_corners(object_coords):
    """
    Finds the corner cells of a given object, as defined by its coordinates.
    For a 1x2 or 2x1 object a "corner" would be the end.
    """
    corners = []

    if len(object_coords) == 2:
        corners = object_coords
    
    return corners

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
      - Finds azure (color 8) objects.
      - Changes the color of identified corner cells to blue (color 1).
      - Keeps all other cells the same color.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      corners = find_corners(obj)
      for corner in corners:
          output_grid[corner] = 1

    return output_grid