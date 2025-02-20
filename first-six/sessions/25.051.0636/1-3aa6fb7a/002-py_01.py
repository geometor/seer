"""
The transformation preserves the azure (8) objects and adds blue (1) cells immediately to the right of the first azure element of a vertical line, and to the left of the second element of a horizontal line.
"""

import numpy as np

def find_objects(grid, color):
    # Find objects of a specific color in the grid.
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

        # Check all 4 directions (up, down, left, right)
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

def check_line_orientation(obj):

    if len(obj) < 2:
        return "point"  # Not a line

    # Extract row and column coordinates
    rows, cols = zip(*obj)

    if len(set(rows)) == 1:
        return "horizontal"  # All rows are the same
    elif len(set(cols)) == 1:
        return "vertical"  # All columns are the same
    else:
        return "diagonal"


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Preserve azure objects and add blue cells based on their positions
    for obj in azure_objects:
        orientation = check_line_orientation(obj)

        if orientation == "vertical":
            first_element = obj[0]
            r, c = first_element
            if c + 1 < cols and output_grid[r, c + 1] != 8:
                 output_grid[r, c + 1] = 1  # Paint blue to the right

        elif orientation == "horizontal":

            second_element = obj[1]
            r,c = second_element
            if c - 1 >= 0 and output_grid[r, c - 1] != 8:
                 output_grid[r, c-1] = 1 # Paint blue to the left
    return output_grid