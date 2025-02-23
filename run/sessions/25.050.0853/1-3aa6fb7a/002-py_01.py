"""
The transformation rule is: Find all azure areas. For each distinct azure region,
place a single blue pixel adjacent to it. The direction seems to be the opposite
of the 'direction' of the azure object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of sets, where each set contains the coordinates of an object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = set()
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule: For each azure (8) object,
    place a blue (1) pixel adjacent to it.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      #find object centroid
      centroid_row = 0
      centroid_col = 0

      for cell in obj:
          centroid_row += cell[0]
          centroid_col += cell[1]
      
      obj_len = len(obj)
      centroid_row = round(centroid_row/obj_len)
      centroid_col = round(centroid_col/obj_len)

      #find the azure object "direction" (vertical/horizontal)
      rows = []
      cols = []
      for cell in obj:
        rows.append(cell[0])
        cols.append(cell[1])
      
      # blue placement based on object analysis
      if(min(rows) == centroid_row):
        output_grid[centroid_row, centroid_col -1 ] = 1
      elif(max(rows) == centroid_row):
        output_grid[centroid_row, centroid_col + 1] = 1
      elif(min(cols) == centroid_col):
        output_grid[centroid_row -1, centroid_col] = 1
      elif(max(cols) == centroid_col):
        output_grid[centroid_row +1, centroid_col] = 1

    return output_grid