"""
The transformation preserves the two azure L-shaped objects. It adds two blue pixels. The first is placed next to the right of the vertical segment of the first L-shaped object. The second is put at the mirrored position with respect to a horizontal axis across the center of the grid.
"""

import numpy as np

def find_objects(grid, color):
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
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find the azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the found objects to identify the L-shapes and their positions
    for obj in azure_objects:
      if len(obj) == 3:
        # Sort to make easier identification
        sorted_obj = sorted(obj)

        # Insertion logic
        # First L shape
        if (sorted_obj[0][0] + 1 == sorted_obj[1][0]
          and sorted_obj[1][0] + 1 == sorted_obj[2][0]
          and sorted_obj[0][1] == sorted_obj[1][1]
          and sorted_obj[1][1] + 1 == sorted_obj[2][1]):

            insert_pos = (sorted_obj[0][0] , sorted_obj[0][1] + 1)
            output_grid[insert_pos] = 1

        # Mirrored, inverse L Shape
        elif (sorted_obj[0][0] + 1 == sorted_obj[1][0]
          and sorted_obj[1][0] + 1 == sorted_obj[2][0]
          and sorted_obj[0][1] == sorted_obj[1][1]
          and sorted_obj[1][1] - 1 == sorted_obj[2][1]):
            insert_pos = (sorted_obj[0][0] , sorted_obj[0][1] - 1)
            output_grid[insert_pos] = 1


    return output_grid