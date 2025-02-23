"""
The transformation rule is as follows:
1. Copy the input grid to the output grid.
2. Find all azure (color 8) objects.
3. For each azure object, insert a blue pixel (color 1) adjacent to it. The exact position relative to the azure object varies (left, top, corner) and needs to be determined for each object based on its shape and surrounding pixels.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous objects of a specified color in the grid.
    Returns a list of object coordinates, where each object is represented by a list of (row, col) tuples.
    """
    objects = []
    visited = set()

    def is_valid(row, col):
        return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

    def dfs(row, col, current_object):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))

        # Explore adjacent cells
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

def determine_blue_pixel_position(azure_object, grid):
    """
    Determines where to place the blue pixel based on the azure object's shape and position.
    It prioritizes, in order:
    1. Left
    2. Top.
    3. Upper-left, upper-right, bottom-left, bottom-right corner.

    """
    rows, cols = zip(*azure_object)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    # Try left
    if min_col > 0:
        if all(grid[row, min_col-1] != 1 for row in range(min_row, max_row+1)):
          for row in range(min_row, max_row + 1):
            if grid[row,min_col-1] == 0:
              return (row, min_col - 1)


    #Try Top
    if min_row > 0 :
      if all(grid[min_row-1, col] != 1 for col in range(min_col,max_col+1)):
        for col in range(min_col,max_col+1):
          if grid[min_row-1,col] == 0:
            return (min_row - 1, col)
    
    # Try upper-left
    if min_row > 0 and min_col > 0 and grid[min_row-1,min_col-1] == 0:
      return (min_row - 1, min_col - 1)
    
    #try upper-right
    if min_row > 0 and max_col < grid.shape[1] - 1 and grid[min_row-1,max_col+1] == 0:
      return (min_row-1,max_col+1)

    #try bottom-left
    if max_row < grid.shape[0] - 1 and min_col > 0 and grid[max_row+1, min_col-1] == 0:
      return (max_row+1, min_col-1)

    # Try bottom-right
    if max_row < grid.shape[0]-1 and max_col < grid.shape[1]-1 and grid[max_row+1,max_col+1] == 0:
      return(max_row + 1,max_col+1)

    return None

def transform(input_grid):
    # Initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Insert blue pixels
    for azure_object in azure_objects:
        blue_pixel_pos = determine_blue_pixel_position(azure_object, output_grid)
        if blue_pixel_pos:
            output_grid[blue_pixel_pos] = 1

    return output_grid