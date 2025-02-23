"""
The transformation rule is simple, a color 1 is placed, relative to each object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    An object is defined as a contiguous region of the same color.
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
    Transforms the input grid according to the rule.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid, 8)

    for obj in objects:
      #find the relative position for the current object
      if (obj[0][0] == obj[1][0]): #check for relative position
        #add blue to the input
        output_grid[obj[0][0],obj[0][1]+1] = 1
      else:
        output_grid[obj[2][0],obj[2][1]-1] = 1
    return output_grid