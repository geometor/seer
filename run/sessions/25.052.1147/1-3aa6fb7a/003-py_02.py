"""
The transformation preserves all existing azure (8) objects. It adds a blue (1) pixel immediately to the left or to the right of the azure rectangle.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find the azure (8) objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the found azure objects
    for obj in azure_objects:
        # Sort the coordinates to find top-left and dimensions
        sorted_coords = sorted(obj, key=lambda x: (x[0], x[1]))
        top_left = sorted_coords[0]
        
        # Determine placement based on object position
        
        #Vertical segment
        if len(obj) > 1 and obj[0][1] == obj[1][1]:
            output_grid[top_left[0], top_left[1] + 1] = 1
        
        #horizontal segment
        elif len(obj) > 1 and obj[0][0] == obj[1][0]:
            output_grid[top_left[0], top_left[1] - 1] = 1
        
        #Single pixel segments, determine position
        else:
            if top_left[0] < input_grid.shape[0] / 2 :
                output_grid[top_left[0], top_left[1] - 1] = 1
            
            else:
                rightmost = max(obj, key=lambda x: x[1])[1]
                output_grid[top_left[0], rightmost] = 1
    return output_grid