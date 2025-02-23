"""
The transformation rule identifies "L" shaped objects of color 8 (azure) in the input grid. 
For each identified "L" shape, a pixel of color 1 (blue) is placed at the inner corner of the "L".
The rest of the grid remains unchanged.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the given color
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_l_shapes(obj):
    #rule to detect 2x2 L shapes from the object
    if len(obj) != 3: return []
    obj.sort()
    if (obj[1][0] == obj[0][0]+1 and obj[1][1] == obj[0][1] and
        obj[2][0] == obj[1][0] and obj[2][1] == obj[1][1]+1) or \
       (obj[1][0] == obj[0][0] and obj[1][1] == obj[0][1]+1 and
        obj[2][0] == obj[1][0]+1 and obj[2][1] == obj[1][1]):
            return obj
    else: return []

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)
    
    #detect L shapes
    l_shapes = []
    for obj in azure_objects:
      l = find_l_shapes(obj)
      if len(l) > 0: l_shapes.append(l)

    # Place blue (1) pixels inside detected "L" shapes
    for l_shape in l_shapes:
        #get coordinates
        l_shape.sort()
        #check the orientation and set the insertion point
        if l_shape[1][0] > l_shape[0][0]:
          output_grid[l_shape[0][0] + 1, l_shape[0][1] + 1] = 1
        else:
          output_grid[l_shape[2][0] -1, l_shape[2][1]-1] = 1  
    return output_grid