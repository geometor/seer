"""
The transformation rule is:
Iterate through each separate azure (8) object in the input grid.
For each azure object, find the cell with the smallest row number (the topmost azure pixel).
Place a blue (1) pixel in the cell immediately to the left of this topmost azure pixel.
All other cells keep its value.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the specified color.
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return

        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule: For each azure (8)
    object, add a blue (1) pixel to the left of its topmost pixel.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the topmost pixel (smallest row number).
        topmost_pixel = min(obj, key=lambda p: p[0])
        # Add a blue pixel to the left.
        row, col = topmost_pixel
        if col - 1 >= 0:  # Check bounds
          output_grid[row, col - 1] = 1

    return output_grid