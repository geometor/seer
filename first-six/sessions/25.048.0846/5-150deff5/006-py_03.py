"""
The transformation recolors a gray object based on the presence of a left neighbor within the object.  If a gray cell has another gray cell to its immediate left, it becomes azure; otherwise, it becomes red.
"""

import numpy as np

def get_objects(grid):
    """
    Identify contiguous regions of the same color as objects.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, current_object):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, color, current_object)
        dfs(row - 1, col, color, current_object)
        dfs(row, col + 1, color, current_object)
        dfs(row, col - 1, color, current_object)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                if color != 0:  # Ignore background color
                    current_object = []
                    dfs(row, col, color, current_object)
                    objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    gray_objects = get_objects(input_grid)

    for object_coords in gray_objects:
        for row, col in object_coords:
            if input_grid[row,col] == 5: #check if it is gray
                if col > 0 and input_grid[row, col - 1] == 5: # Check left neighbor
                    output_grid[row, col] = 8
                else:
                    output_grid[row, col] = 2

    return output_grid