"""
1. **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case there two separated objects, one vertical and another one horizontal.
2. **Blue Pixel Insertion at Top-Left:** For each separate azure objects, insert a blue pixel (color 1) to the right of the topmost-leftmost pixel of the azure object. If the top consists of multiple pixels, it goes with the left one.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
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

def top_left(object_coords):
    """
    Finds the top-leftmost coordinate of an object.
    """
    min_row = float('inf')
    min_col = float('inf')
    for r, c in object_coords:
        if r < min_row:
            min_row = r
            min_col = c
        elif r == min_row:
             if c < min_col:
                min_col = c

    return (min_row, min_col)
def transform(input_grid):
    """
    Transforms the input grid according to the defined rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        top_left_coord = top_left(obj)
        # Insert blue pixel to the right of top-left
        insert_row = top_left_coord[0]
        insert_col = top_left_coord[1] + 1

        if 0<= insert_row < output_grid.shape[0] and 0 <= insert_col < output_grid.shape[1]:
            output_grid[insert_row, insert_col] = 1
    
    return output_grid