"""
The azure color 8 objects are preserved. A blue (1) cell is placed on top or at the right of the uppermost and leftmost azure cell, in each azure object (L-shaped or single cell). If placing to the right is not within bounds, placing on top is selected.
"""

import numpy as np

def get_objects(grid, color):
    """ Get all separated objects of a given color."""
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

def find_top_left_cell(object_cells):
    """Finds the uppermost and leftmost cell of an object."""
    if not object_cells:
        return None

    min_row = min(cell[0] for cell in object_cells)
    min_col_candidates = [cell[1] for cell in object_cells if cell[0] == min_row]
    min_col = min(min_col_candidates)
    return (min_row, min_col)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    objects = get_objects(input_grid, 8)

    for obj in objects:
        # Find top-left of the object
        top_left = find_top_left_cell(obj)

        # Place blue cell to the right or on top of the top-left cell
        if top_left[1] + 1 < output_grid.shape[1]:
            output_grid[top_left[0], top_left[1] + 1] = 1
        elif top_left[0] - 1 >= 0:
            output_grid[top_left[0] - 1, top_left[1]] = 1

    return output_grid