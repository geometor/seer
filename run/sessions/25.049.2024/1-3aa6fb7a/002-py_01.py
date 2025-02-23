"""
The transformation rule identifies single azure (color 8) cells in the input grid and changes their color to blue (color 1) in the output grid. Other azure cells, forming connected components, remain unchanged.
"""

import numpy as np

def get_objects(grid):
    """
    Finds and groups contiguous regions of the same color.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(r, c, color, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, color, current_object)
        dfs(r - 1, c, color, current_object)
        dfs(r, c + 1, color, current_object)
        dfs(r, c - 1, color, current_object)
        dfs(r+1, c+1, color, current_object)
        dfs(r-1, c-1, color, current_object)
        dfs(r-1, c+1, color, current_object)
        dfs(r+1, c-1, color, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c]:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                if current_object:
                    objects.append(current_object)
    return objects
def transform(input_grid):
    """
    Transforms the input grid by changing isolated azure cells to blue.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    objects = get_objects(input_grid)

    # Iterate through the identified objects
    for obj in objects:
      if input_grid[obj[0]] == 8:
        if len(obj) == 1:
          output_grid[obj[0]] = 1

    return output_grid