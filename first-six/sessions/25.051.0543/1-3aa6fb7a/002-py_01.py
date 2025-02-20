"""
The transformation rule is as follows:
1. Identify two azure (color 8) objects in the input grid.
2. Introduce blue (color 1) pixels adjacent to the identified azure objects.
    -  Place the new pixel (with value = 1) to the right of the top azure object.
    -  Place the new pixel (with value = 1) to the left of the bottom azure object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color in the grid.
    Returns a list of lists, each sublist containing coordinates of an object.
    """
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects
def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Assuming the first object is on the upper side and the second is on the lower side of grid
    if len(azure_objects) >= 2:
       
        #sort object by top-left coordinate
        sorted_objects = sorted(azure_objects, key=lambda obj: (min(y for x, y in obj), min(x for x, y in obj)))
        top_object = sorted_objects[0]
        bottom_object = sorted_objects[1]

        # Place blue pixel to the right of the top object
        top_rightmost = max(top_object, key=lambda coord: coord[1])
        output_grid[top_rightmost[0], top_rightmost[1] + 1] = 1

        # place a blue pixel to the left of the bottom object.
        bottom_leftmost = min(bottom_object, key=lambda coord: coord[1])
        output_grid[bottom_leftmost[0] , bottom_leftmost[1] -1] = 1
    
    return output_grid