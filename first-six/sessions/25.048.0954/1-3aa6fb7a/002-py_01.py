"""
The transformation rule identifies separate regions of color '8' (azure) in the input grid. 
It changes the color of the top cell of the 2x1 vertical azure shapes and the left cell of the 1x2 horizontal shape from '8' to '1' (blue).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of tuples, where each tuple contains the coordinates of cells in an object.
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

        # Check adjacent cells (up, down, left, right)
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

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Find azure (color 8) objects.
    - Change the top cell of vertical 2x1 shapes to blue (color 1).
    - Change the left cell of horizontal 1x2 shapes to blue (color 1).
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the object coordinates by row and column
        sorted_obj = sorted(obj, key=lambda x: (x[0], x[1]))

        # Check for 2x1 vertical shape
        
        if len(sorted_obj) == 2 :
            #check if it's vertical
            if sorted_obj[0][1] == sorted_obj[1][1]:
                output_grid[sorted_obj[0]] = 1  # Change top cell to blue
            else:
                output_grid[sorted_obj[0]] = 1  # Change left cell to blue
            

    return output_grid