# 890034e9 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule is: For each green object that is related to an azure block, move the azure block from its existing location to overlap or be contained by the green object. If there is already an azure block inside the green object, the move operation consists of a translation only.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find contiguous regions (objects) of a specific color in the grid.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

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

def find_adjacent_objects(grid, objects, target_color):
    """Find the location and count the adjacent blocks given a target color"""
    adjacencies = []

    for obj in objects:
      for cell in obj:
        row,col = cell

        #check neighbors
        neighbors = [
            (row -1, col),
            (row + 1, col),
            (row, col-1),
            (row, col + 1)
        ]

        for neighbor_row, neighbor_col in neighbors:
            if (0 <= neighbor_row < grid.shape[0] and
                0 <= neighbor_col < grid.shape[1] and
                grid[neighbor_row, neighbor_col] == target_color):
                adjacencies.append( (neighbor_row, neighbor_col) )

    return adjacencies

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find green (3) objects
    green_objects = find_objects(output_grid, 3)
    #print(f"{green_objects=}")

    # Find azure (8) objects
    azure_objects = find_objects(output_grid, 8)
    #print(f"{azure_objects=}")

    #iterate through azure objects
    for azure_object in azure_objects:

      # find green objects adjacent to this azure
      adjacent_greens = find_adjacent_objects(output_grid, [azure_object], 3)
      #print(f"{adjacent_greens=}")

      if adjacent_greens:

        # find yellow objects, need to move the 8s to be closer to them
        yellow_adjacencies = find_adjacent_objects(output_grid, [azure_object], 4)
        #print(f"{yellow_adjacencies=}")

        #clear current azure object
        for row, col in azure_object:
          output_grid[row, col] = input_grid[row,col]

        # determine where to move the 8s
        if yellow_adjacencies:
          # use the yelolow as a target location
          target_row, target_col = yellow_adjacencies[0] #just choose the first yellow
        else:
          #default to the first green if no yellow is close
          target_row, target_col = adjacent_greens[0]


        #attempt to move the 8s, based on relative location to the target
        #we want to "line up" 8s next to target
        for i in range(len(azure_object)):
            row_offset = azure_object[i][0] - azure_object[0][0]
            col_offset = azure_object[i][1] - azure_object[0][1]

            new_row = target_row + row_offset
            new_col = target_col + col_offset -1 #try to shift them left, towards the target

            #make sure it is valid move
            if (0 <= new_row < output_grid.shape[0] and
                0 <= new_col < output_grid.shape[1] ):

              #check if spot is available, prioritize green
              if output_grid[new_row, new_col] == 3:
                output_grid[new_row, new_col] = 8
              elif output_grid[new_row, new_col] == 0:
                output_grid[new_row,new_col] = 8


    return output_grid
```
