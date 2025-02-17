"""
The transformation rule takes the azure colored object in the input grid and creates a blue pixel next to its upmost pixel.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
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

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)
    
    # For each azure object
    for obj in azure_objects:
      # Find the topmost pixel
      topmost_pixel = min(obj, key=lambda x: x[0])

      # Calculate the position for the new blue pixel (one row below)
      new_blue_pixel_row = topmost_pixel[0]
      new_blue_pixel_col = topmost_pixel[1] +1
      
      # check bounds
      if(new_blue_pixel_row < output_grid.shape[0] and new_blue_pixel_col < output_grid.shape[1]):
        output_grid[new_blue_pixel_row, new_blue_pixel_col] = 1 # Set to blue

    return output_grid