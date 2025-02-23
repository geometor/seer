# AboveBelow7 • 010 • refine_coder

---
```python
"""
1. Identify Objects: Find all contiguous regions of azure (8) and red (2) pixels. These are considered distinct objects.
2. Azure Object Movement: Move all azure objects to the bottom of the grid.
3. Relative Horizontal Order: Maintain the relative horizontal order of the azure objects. If an azure object was left of another in the input, it should remain left of it in the output.
4. Vertical Positioning: Place the azure objects as low as possible in the grid, without overlapping any other non-background color (non-zero) objects.
5.  Red Object Stationary: The red object remains in its original position.
6. Background: Consider the background (0 color) pixels. The background must be considered and moved when required to allow other operations.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of a specified color in the grid.
    Returns a list of object bounding boxes (min_row, min_col, max_row, max_col) and a list of the object coordinates.
    """
    visited = set()
    objects = []
    object_coords = []

    def dfs(row, col, current_object, current_coords):
        if (row, col) in visited or row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        current_coords.append((row,col))
        dfs(row + 1, col, current_object, current_coords)
        dfs(row - 1, col, current_object, current_coords)
        dfs(row, col + 1, current_object, current_coords)
        dfs(row, col - 1, current_object, current_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                current_coords = []
                dfs(row, col, current_object, current_coords)
                # calculate bounding box
                min_row = min(current_object, key=lambda x: x[0])[0]
                min_col = min(current_object, key=lambda x: x[1])[1]
                max_row = max(current_object, key=lambda x: x[0])[0]
                max_col = max(current_object, key=lambda x: x[1])[1]
                objects.append( (min_row, min_col, max_row, max_col) )
                object_coords.append(current_coords)
    return objects, object_coords

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find azure (8) objects
    azure_objects, azure_coords = find_objects(input_grid, 8)

    # Find red (2) object
    red_objects, red_coords = find_objects(input_grid, 2) # bounding boxes not currently used

    # Clear initial positions of azure objects in the output grid
    for obj_coords in azure_coords:
        for row, col in obj_coords:
            output_grid[row, col] = 0

    # Sort azure objects by their leftmost coordinate (min_col) to maintain relative order
    azure_objects_sorted = sorted(zip(azure_objects, azure_coords), key=lambda x: x[0][1])

    # Calculate destination positions for azure objects
    for (min_row, min_col, max_row, max_col), obj_coords in azure_objects_sorted:
      obj_height = max_row - min_row + 1
      obj_width = max_col - min_col + 1
      dest_row = output_grid.shape[0] - obj_height # start with bottom most

      # check for collisions and adjust dest_row upwards if necessary
      collision = True
      while collision and dest_row >= 0:
        collision = False
        for r in range(dest_row, dest_row + obj_height):
          for c in range(min_col, min_col+obj_width): # use the original min_col
              if r < output_grid.shape[0] and c < output_grid.shape[1] and output_grid[r,c] != 0: # check for collisions
                collision = True
                dest_row -= 1 #move up one row
                break
          if collision:
              break

      # move object to the destination row in output, adjusted for x position
      x_offset = min_col
      for row,col in obj_coords:
        output_grid[dest_row + (row - min_row) , x_offset + (col - min_col)] = 8

    return output_grid
```
