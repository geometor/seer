"""
Transformation Rule:

1.  Locate all objects comprised of 2 pixels of color azure (8).
2.  For each horizontal object, insert a pixel of color white (1) in the row below the first pixel.
3. For each vertical object, insert a pixel of color white(1) in the column after the first pixel.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
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
                if len(current_object) == 2: # only look for objects with 2 pixels
                  objects.append(current_object)
    return objects

def is_horizontal(object_pixels):
    # object assumed to have only 2 pixels
    return object_pixels[0][0] == object_pixels[1][0]

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      if is_horizontal(obj):
        # insert white pixel (1) below first pixel of horizontal object
        output_grid[obj[0][0] + 1, obj[0][1]] = 1
      else:
        # insert white pixel (1) to the right of first pixel of the object
        output_grid[obj[0][0], obj[0][1] + 1] = 1

    return output_grid