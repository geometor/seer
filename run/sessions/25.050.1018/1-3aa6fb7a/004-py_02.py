"""
The transformation rule involves identifying azure (color 8) L-shaped objects in the input grid and adding a blue (color 1) pixel adjacent to each object. The position of the blue pixel depends on the orientation of the "L". If the L-shape's longer part is vertical, the blue pixel is placed to the right of the top pixel of the L.  If the longer part is horizontal, the blue pixel is placed to the left of the bottom pixel of the L.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    An object is defined as a contiguous region of the same color.
    Uses Depth First Search (DFS).
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)


    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Find azure L-shapes and place a blue pixel relative to it.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid, 8)

    for obj in objects:
      # Sort the object coordinates to help determine orientation
      obj.sort()

      # Determine the orientation of the L-shape and add the blue pixel
      if (obj[0][0] == obj[1][0]): #check for relative position (horizontal)
        # Add blue to the left of bottom
        output_grid[obj[2][0],obj[2][1]-1] = 1
      else:
        # Add blue to the right of top.
        output_grid[obj[0][0],obj[0][1]+1] = 1
    return output_grid