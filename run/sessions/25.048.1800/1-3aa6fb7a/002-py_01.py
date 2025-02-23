"""
Identifies connected regions of color 8 (azure) in the input grid, sorts them horizontally, and changes the color of specific adjacent cells to 1 (blue).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected components of the specified color in the grid.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
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

def sort_objects(objects):
    """
    Sorts objects based on their leftmost column.
    """
    return sorted(objects, key=lambda obj: min(col for _, col in obj))

def get_topmost_cell(object_cells):
    """Returns the topmost cell (min row index) of an object."""
    return min(object_cells, key=lambda cell: cell[0])

def get_bottommost_cell(object_cells):
    """Returns the bottommost cell (max row index) of an object."""
    return max(object_cells, key=lambda cell: cell[0])

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8
    objects = find_objects(output_grid, 8)
    
    # Sort objects from left to right
    sorted_objects = sort_objects(objects)
    
    # Process leftmost object
    if sorted_objects:
        leftmost_object = sorted_objects[0]
        topmost_cell = get_topmost_cell(leftmost_object)
        right_neighbor = (topmost_cell[0], topmost_cell[1] + 1)
        if 0 <= right_neighbor[1] < output_grid.shape[1]:
            output_grid[right_neighbor] = 1
    
    # Process rightmost object
    if len(sorted_objects) >= 1:  #Corrected the condition
        rightmost_object = sorted_objects[-1]
        bottommost_cell = get_bottommost_cell(rightmost_object)
        left_neighbor = (bottommost_cell[0], bottommost_cell[1] - 1)
        if 0 <= left_neighbor[1] < output_grid.shape[1]:
            output_grid[left_neighbor] = 1

    return output_grid