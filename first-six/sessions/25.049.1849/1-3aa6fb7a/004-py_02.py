"""
The transformation identifies objects of color 8. If the object has color 8, insert color 1 in the next position. If there are multiple objects made with color 8, insert at left and right, according to their position, starting from top left.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the given color.
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
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
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    output_grid = np.copy(input_grid)
    objects_8 = find_objects(input_grid, 8)

    # Iterate through objects of color 8 and insert color 1
    
    if len(objects_8)>0:
      #object 1 (top-left)
      #find right position
      row_obj1 = objects_8[0][0][0] #first element, first element, row
      col_obj1 = objects_8[0][0][1] #first element, first element, col

      #check it is not out of boundaries, and insert value 1
      if col_obj1+1<output_grid.shape[1]:
        output_grid[row_obj1, col_obj1+1] = 1
    if len(objects_8)>1:
      #object 2
      #find left element
      row_obj2 = objects_8[1][0][0]
      col_obj2 = objects_8[1][0][1]
      
      #insert value
      output_grid[row_obj2, col_obj2-1] = 1

    return output_grid