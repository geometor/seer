# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Locates azure (color 8) components in the input grid and places a blue pixel (color 1) to the right of the top-left azure object and to the left of the bottom-right azure object. All other pixels remain unchanged (color 0).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specified color in the grid.
    Returns a list of positions where the color is found.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                objects.append((r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Find top-left azure object (assuming it's the one with the smallest row and col)
    if azure_objects:

      # Sort by row and then by column
      azure_objects.sort()

      top_left_object = []
      center_right_object = []

      #assume the azure objects appear at the top-left first
      if (azure_objects[0][0] + 1, azure_objects[0][1]) in azure_objects:
        #we have a vertical object at top-left
        top_left_object.append(azure_objects[0])
        top_left_object.append((azure_objects[0][0] + 1, azure_objects[0][1]))

        output_grid[top_left_object[0][0], top_left_object[0][1] + 1] = 1

      #now find the horizontal object at bottom-right
      for obj in azure_objects:
          if (obj[0], obj[1]+1) in azure_objects:
            center_right_object.append(obj)
            center_right_object.append((obj[0], obj[1]+1))
            break
      if(len(center_right_object) > 0):
          output_grid[center_right_object[0][0]+1, center_right_object[0][1]] = 1

    return output_grid
```
