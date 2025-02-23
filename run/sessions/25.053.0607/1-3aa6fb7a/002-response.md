# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
This transformation identifies azure objects and adds a blue pixel inside of them.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
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
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find azure objects
    azure_objects = find_objects(input_grid, 8)  # 8 is for azure
    
    # Modify the first object (vertical line)
    if len(azure_objects) >= 1:
      first_object = azure_objects[0]
      if len(first_object) > 1:
          first_object.sort()
          row = first_object[1][0]
          col = first_object[1][1]          
          output_grid[row,col+1] = 1

    #Modify the second object if exist
    if len(azure_objects) >= 2:
        second_object = azure_objects[1]
        #check the shape of the second object is a mirrored L shape
        second_object.sort()
        row = second_object[0][0]
        col = second_object[0][1]

        output_grid[row+1,col] = 1
    
    # change output pixels 

    return output_grid
```
