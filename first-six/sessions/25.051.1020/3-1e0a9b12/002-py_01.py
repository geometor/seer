"""
1. Consider the objects that are not color 0 (the background).
2. Maintain the position of all objects in the bottom row.
3. For any object not in the bottom row:
  - Consider its current column.
  - Move object the lowest available cell in its same column.
"""

import numpy as np

def find_objects(grid):
    """Finds all objects in the grid. Returns as dict {color: [(y,x)]}"""
    objects = {}
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            color = grid[y, x]
            if color != 0:
                if color not in objects:
                    objects[color] = []
                objects[color].append((y, x))
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    #find objects different to background color (0)
    objects = find_objects(input_grid)

    # Iterate through the objects
    for color, positions in objects.items():
      for y,x in positions:
        #if the object is in the last row
        if y == input_grid.shape[0]-1:
          #maintain current possition
          output_grid[y,x] = color
        else:
          #else, find lowest empty position at same column
          for row in range(input_grid.shape[0]-1, -1, -1):
            if output_grid[row,x] == 0:
              output_grid[row,x] = color
              break;

    return output_grid