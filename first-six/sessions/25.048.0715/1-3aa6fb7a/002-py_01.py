"""
The transformation identifies isolated azure (8) colored, change the color to blue (1) for the most top-right element, and the most bottom-left element. All of this while preserving other elements.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color
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
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find all azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Find the most top-right azure object
    if azure_objects:
        top_right_object = min(azure_objects, key=lambda obj: (min(pos[0] for pos in obj), -max(pos[1] for pos in obj)) )
        # Change the color of the top right position
        top_right_position = min(top_right_object, key=lambda pos: (pos[0], -pos[1]))
        output_grid[top_right_position] = 1

    # Find the most bottom-left azure object
    if azure_objects:
      bottom_left_object = min(azure_objects, key=lambda obj: (-max(pos[0] for pos in obj), min(pos[1] for pos in obj)))
      # Change the color of the bottom left positon
      bottom_left_position = min(bottom_left_object, key=lambda pos: (-pos[0], pos[1]))
      output_grid[bottom_left_position] = 1
    return output_grid