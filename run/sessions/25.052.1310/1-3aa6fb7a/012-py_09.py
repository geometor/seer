"""
The transformation involves identifying azure (color 8) objects in the input grid and adding a blue (color 1) pixel adjacent to each azure object, prioritizing the available directions in this order: Left, Right, Down, Up. Only one blue pixel should added adjacent to the object. The positioning of the blue pixel should be relative to the object.
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
                objects.append(current_object)
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for azure_object in azure_objects:
        added = False  # Flag to track if a blue pixel has been added for the current object
        # Priority 1: Left
        for r, c in azure_object:
            if c > 0 and output_grid[r, c - 1] == 0:
                output_grid[r, c - 1] = 1
                added = True
                break  # Stop after adding one blue pixel for this object
        if added:
            continue

        # Priority 2: Right
        for r, c in azure_object:
            if c + 1 < output_grid.shape[1] and output_grid[r, c + 1] == 0:
                output_grid[r, c + 1] = 1
                added = True
                break  # Stop after adding one blue pixel for this object
        if added:
            continue

        # Priority 3: Down
        for r, c in azure_object:
            if r + 1 < output_grid.shape[0] and output_grid[r + 1, c] == 0:
                output_grid[r + 1, c] = 1
                added = True
                break  # Stop after adding one blue pixel for this object

        if added:
            continue

        # Priority 4: Up
        for r, c in azure_object:
            if r - 1 >= 0 and output_grid[r - 1, c] == 0:
                output_grid[r - 1, c] = 1
                added = True
                break  # Stop after adding one blue pixel for this object
        if added:
            continue
    return output_grid