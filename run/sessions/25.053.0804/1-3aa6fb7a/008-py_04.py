"""
Identifies azure (8) colored objects and replaces some of their pixels with blue (1) based on adjacency to empty spaces within the object.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color in the grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Iterate through each pixel within the object
        for r, c in obj:
            # Check for empty space to the right
            if c + 1 < cols and input_grid[r, c + 1] == 0:
                output_grid[r, c] = 1  # Replace azure with blue
            # Check for empty space below
            elif r + 1 < rows and input_grid[r + 1, c] == 0:
                output_grid[r, c] = 1  # Replace azure with blue

    return output_grid