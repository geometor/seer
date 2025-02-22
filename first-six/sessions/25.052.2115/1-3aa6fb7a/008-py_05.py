"""
The transformation identifies azure (8) objects in the input grid. It preserves 2x2 azure objects,
splits 1x2 and 2x1 azure objects into two 1x1 objects, changing the left pixel to blue (1) for 1x2 objects and
the top pixel to blue (1) for 2x1 objects. For 1x1 azure objects, it checks for left or top neighbors; if present,
the pixel becomes blue, otherwise, it remains azure. All other cells in the grid remain unchanged (white, 0).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous blocks (objects) of a specified color in the grid.
    Returns a list of bounding box coordinates, each as (min_row, min_col, max_row, max_col).
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        """Depth-First Search helper to find contiguous pixels."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
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
                if current_object:
                    min_row, min_col = np.min(current_object, axis=0)
                    max_row, max_col = np.max(current_object, axis=0)
                    objects.append((min_row, min_col, max_row, max_col))

    return objects

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      min_row, min_col, max_row, max_col = obj
      height = max_row - min_row + 1
      width = max_col - min_col + 1

      if height == 2 and width == 2: # copy 2x2 objects
        for r in range(min_row, max_row+1):
          for c in range(min_col, max_col+1):
            output_grid[r,c] = 8
      elif (height == 1 and width == 2): # Split and change 1x2 object
        output_grid[min_row, min_col] = 1
        output_grid[max_row, max_col] = 8
      elif (height == 2 and width == 1): # Split and change 2x1 object
        output_grid[min_row, min_col] = 1
        output_grid[max_row, max_col] = 8
      elif height == 1 and width == 1: # check 1x1 object
        if (min_col > 0 and input_grid[min_row, min_col-1] == 8) or (min_row>0 and input_grid[min_row-1, min_col] == 8):
          output_grid[min_row, min_col] = 1
        else:
          output_grid[min_row, min_col] = 8
    return output_grid