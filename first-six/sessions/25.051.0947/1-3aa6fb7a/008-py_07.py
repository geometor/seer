"""
1. Preserve Azure: Copy all azure (color 8) objects from the input grid to the output grid without changes.

2. Add Blue - Top: Find the uppermost azure object. Determine the row and column indices of its rightmost cell. Add a blue pixel (color 1) to the output grid at the position immediately to the right of this rightmost cell, keeping the row.

3. Add Blue - Bottom: Find the lowermost azure object. Determine the row and column indices of its leftmost cell. Add a blue pixel (color 1) to the output grid at the position immediately to the left of this leftmost cell, keeping the row.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Find uppermost object
    if azure_objects:
      uppermost_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      rightmost_cell = max(uppermost_object, key=lambda cell: cell[1])
      if rightmost_cell[1] + 1 < output_grid.shape[1]:
        output_grid[rightmost_cell[0], rightmost_cell[1] + 1] = 1

    # Find lowermost object
      lowermost_object = max(azure_objects, key=lambda obj: (max(r for r, c in obj), min(c for r, c in obj)))
      leftmost_cell = min(lowermost_object, key=lambda cell: cell[1])
    
      if leftmost_cell[1] -1 >= 0:
        output_grid[leftmost_cell[0], leftmost_cell[1] - 1] = 1

    return output_grid