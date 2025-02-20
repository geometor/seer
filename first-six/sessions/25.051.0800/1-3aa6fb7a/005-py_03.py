"""
The blue square changes its color to red.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color and returns them as a list of objects.
       For simplicity, an object is a list of (row, col) tuples.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def _explore(row, col, color, current_object):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Check 4-connectivity
            _explore(row + dr, col + dc, color, current_object)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                current_object = []
                _explore(row, col, color, current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def change_color(grid, object_coords, new_color):
    """Changes the color of all cells in an object to the new color."""
    for row, col in object_coords:
        grid[row, col] = new_color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the rule: blue square becomes red."""
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)

    # find all objects
    objects = find_objects(output_grid)

    # change color of blue objects to red
    for obj_coords in objects:
        if output_grid[obj_coords[0]] == 1: #if the color of first pixel of the object is blue
            output_grid = change_color(output_grid, obj_coords, 2) #change the object color to red

    return output_grid