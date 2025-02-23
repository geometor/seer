"""
1. Identify Azure Objects: Find all contiguous regions of azure (color 8) pixels in the input grid. Each of these regions is considered an object.

2. Extend Each Azure Object: For *each* azure object:
    *   Iterate through all the pixels composing each Azure Object
    *   For each pixel, check for adjacent pixels in all four directions (up, down, left, right).
    *   If any direct adjacent pixel is 0 (white/background), then change it to 1 (Blue)
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
    for obj in azure_objects:
        #Iterate through each pixel of the object
        for r, c in obj:
            # Check adjacent pixels and change 0 to 1
            if r > 0 and output_grid[r-1, c] == 0:
                output_grid[r-1, c] = 1
            if r < output_grid.shape[0] - 1 and output_grid[r+1, c] == 0:
                output_grid[r+1, c] = 1
            if c > 0 and output_grid[r, c-1] == 0:
                output_grid[r, c-1] = 1
            if c < output_grid.shape[1] - 1 and output_grid[r, c+1] == 0:
                output_grid[r, c+1] = 1
    return output_grid