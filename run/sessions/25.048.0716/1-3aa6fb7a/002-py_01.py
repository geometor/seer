"""
Copies azure (color 8) objects from the input to the output grid. Then, it finds empty cells (color 0) that are immediately to the right of or below a single azure cell and are not part of other 2x1 or 1x2 shapes, it turns those into blue (color 1).
"""

import numpy as np

def find_objects(grid, color):
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
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def is_part_of_2x1_or_1x2(grid, r, c, color):
    #check 2x1
    if r+1 < grid.shape[0] and grid[r+1,c] == color:
        return True

    # Check 1x2
    if c + 1 < grid.shape[1] and grid[r,c+1] == color:
          return True

    if r-1 >= 0 and grid[r-1,c] == color:
        return True

    # Check 1x2
    if c - 1 >= 0 and grid[r,c-1] == color:
          return True
    return False

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find azure objects in input_grid
    azure_objects = find_objects(input_grid, 8)

    # Iterate over the input grid to find potential positions for blue cells
    for r in range(input_grid.shape[0]):
      for c in range(input_grid.shape[1]):
        if input_grid[r,c] == 8: #skip already colored squares
              continue
        if input_grid[r,c] == 0: # Check only blank cells
            # Check cell above
            if r > 0 and input_grid[r-1, c] == 8 and not is_part_of_2x1_or_1x2(input_grid,r-1,c,8):
                output_grid[r, c] = 1
                continue # process only one
            # Check cell to the left
            if c > 0 and input_grid[r, c-1] == 8 and not is_part_of_2x1_or_1x2(input_grid,r,c-1,8):
                output_grid[r, c] = 1
                
    return output_grid