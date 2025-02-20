"""
The transformation rule involves inserting a blue cell (color 1) to the right of the top cell of the leftmost azure object, and another one immediately to the left of the bottom cell of the rightmost azure object. The azure objects and the background remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []
        
        visited.add((row, col))
        object_cells = [(row, col)]
        
        object_cells.extend(dfs(row + 1, col))
        object_cells.extend(dfs(row - 1, col))
        object_cells.extend(dfs(row, col + 1))
        object_cells.extend(dfs(row, col - 1))
        
        return object_cells

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Sort objects by their leftmost x coordinate.
    azure_objects.sort(key=lambda obj: min(c for r, c in obj))

    if len(azure_objects) >= 1:
        # Find the top cell of the leftmost object.
        first_object = sorted(azure_objects[0], key=lambda x: (x[0], x[1]))
        top_cell = first_object[0]
        output_grid[top_cell[0], top_cell[1] + 1] = 1  # Insert blue cell to the right

    if len(azure_objects) >= 2:
        #find bottom cell of the rightmost object.
        second_object = sorted(azure_objects[-1], key=lambda x: (-x[0], x[1]))
        bottom_cell = second_object[0]

        output_grid[bottom_cell[0], bottom_cell[1] - 1] = 1 # Insert blue cell to the left.

    return output_grid