"""
The transformation rule identifies 'L' shaped objects of azure (color 8) in the input grid. For each L-shaped object, a single pixel is changed to blue (color 1) based on the orientation of the 'L'. The position of new blue pixel are:
- Vertical L:   If 'L' is vertical, the pixel to the left of upper azure pixel is changed to blue.
- Horizontal L: If 'L' is horizontal, the pixel above the left azure pixel is changed to blue.
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

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_l_shapes(objects):
    """
    Filter the identified L shapes.
    """
    l_shapes = []

    for obj in objects:
        if len(obj) == 3:
           #check if it is a L shape
           obj.sort()
           if (obj[0][0] == obj[1][0] and obj[1][0] == obj[2][0]-1 and obj[1][1] == obj[2][1] )  or \
              (obj[0][1] == obj[1][1] and obj[1][1] == obj[2][1]-1 and obj[1][0] == obj[2][0] )  :
                l_shapes.append(obj)

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    l_shapes = get_l_shapes(azure_objects)

    # Iterate through each identified L-shape
    for obj in l_shapes:
        obj.sort()  # Sort coordinates to identify orientation
        if obj[0][0] == obj[1][0]:  # Vertical L
            output_grid[obj[0][0], obj[0][1] - 1] = 1  # Change pixel to the left
        else:  # Horizontal L
            output_grid[obj[0][0] - 1, obj[0][1]] = 1  # Change pixel above

    return output_grid