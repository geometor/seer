"""
The transformation preserves the two azure L-shaped objects, maintaining their original positions and shapes. Additionally, it adds a single blue pixel (color 1) to the right of each object's corner, in both cases.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_l_shape_corner(object_coords):
    # Find the bounding box
    min_r = min(r for r, c in object_coords)
    max_r = max(r for r, c in object_coords)
    min_c = min(c for r, c in object_coords)
    max_c = max(c for r, c in object_coords)

    # Check all four corners of the bounding box to determine which one is part of the object
    if (min_r, min_c) in object_coords:
      return min_r, min_c
    elif (min_r, max_c) in object_coords:
      return min_r, max_c
    elif (max_r, min_c) in object_coords:
       return max_r, min_c
    else:
      return max_r, max_c

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      corner = find_l_shape_corner(obj)

      # check which corner is the L
      if (corner[0]+1,corner[1]) in obj and (corner[0], corner[1]+1) in obj: # topleft
        output_grid[corner[0], corner[1] + 2] = 1 # add blue at right
      elif (corner[0]-1,corner[1]) in obj and (corner[0], corner[1]+1) in obj: # bottomleft
        output_grid[corner[0] , corner[1] + 2] = 1 # add blue at right
      elif (corner[0]-1,corner[1]) in obj and (corner[0], corner[1]-1) in obj: # bottomnright
        output_grid[corner[0] , corner[1]] = 1 # add blue at right
      else: # topright
        output_grid[corner[0], corner[1] ] = 1


    return output_grid