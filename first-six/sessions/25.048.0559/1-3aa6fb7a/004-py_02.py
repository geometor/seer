"""
The transformation identifies azure (8) colored objects in the input grid.
It then checks for specific white (0) colored cells adjacent to these azure objects based on their shape.
If the conditions are met, it changes these white cells to blue (1).

Specifically:
- For a horizontal 2x1 azure object, it checks the cell below the left cell.
- For a corner-shaped azure object (specifically, an L shape), it checks the cell to the right of the top-left cell of the corner.
- For a vertical 2x1 azure object, it checks the cell to the left of the bottom cell.
"""

import numpy as np

def get_objects(grid, color):
    """
    Find connected components of a specific color.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color and (r,c) not in visited:
          current_object = []
          dfs(r,c, current_object)
          objects.append(current_object)
    return objects
    

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = get_objects(input_grid, 8)

    # Iterate through found azure objects
    for obj in azure_objects:
        # Sort the object positions to easily identify top-left and bottom-right cells.
        obj.sort()

        # Check for horizontal 2x1 object
        if len(obj) == 2 and obj[0][0] == obj[1][0] and obj[0][1] == obj[1][1] - 1:
            # Check cell below the left cell
            target_r, target_c = obj[0][0] + 1, obj[0][1]
            if 0 <= target_r < output_grid.shape[0] and 0 <= target_c < output_grid.shape[1] and output_grid[target_r, target_c] == 0:
                output_grid[target_r, target_c] = 1

        # Check for corner object (L shape)
        elif len(obj) == 3:
            if obj[0][0] == obj[1][0] -1 and obj[0][1] == obj[1][1] and obj[1][0] == obj[2][0] and obj[1][1] == obj[2][1]-1:
              # Check cell to the right of the top-left cell of the corner.
              target_r, target_c = obj[0][0], obj[0][1] + 1
              if 0 <= target_r < output_grid.shape[0] and 0 <= target_c < output_grid.shape[1] and output_grid[target_r, target_c] == 0:
                output_grid[target_r, target_c] = 1

        # Check for vertical 2x1 object
        elif len(obj) == 2 and obj[0][0] == obj[1][0] - 1 and obj[0][1] == obj[1][1]:
            # Check cell to the left of the bottom cell
            target_r, target_c = obj[1][0], obj[1][1] - 1
            if 0 <= target_r < output_grid.shape[0] and 0 <= target_c < output_grid.shape[1] and output_grid[target_r, target_c] == 0:
                output_grid[target_r, target_c] = 1

    return output_grid