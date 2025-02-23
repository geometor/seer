# 2-0ca9ddb6 • 006 • example_3 - CODE

---
```python
"""
1.  **Identify Key Object:** The blue object (value 1) at position [7, 3] in the input grid is the primary actor.
2.  **Yellow Replication:** Four yellow objects (value 4) are created.  These new yellow objects are positioned two rows above and two rows below the blue object, and also two columns to the left and two columns to the right.
3.  **Orange Surround:** Orange objects (value 7) are created around the blue object, occupying all the directly adjacent cells (up, down, left, right).
4.  **Other Objects**:  Objects that were not the blue object (objects 2 and 6) are unchanged.
"""

import numpy as np

def find_objects(grid, value):
    # find the row,col coordinates of all pixels of the given value
    objects = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel == value:
                objects.append((row_index, col_index))
    return objects

def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = input_grid.copy()

    # find blue object
    blue_objects = find_objects(input_grid, 1)
    if not blue_objects:
        return output_grid  # no blue = no transformation
    
    blue_row, blue_col = blue_objects[0] # only expect 1

    # create yellow objects (2-away)
    for row_offset in [-2, 2]:
        for col_offset in [-2, 2]:
           new_row = blue_row + row_offset
           new_col = blue_col + col_offset
           if 0<= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]: # keep in grid
               output_grid[new_row, new_col] = 4

    # create orange objects (adjacent)
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
                continue # skip same cell
            new_row = blue_row + row_offset
            new_col = blue_col + col_offset
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                 output_grid[new_row,new_col] = 7

    return output_grid
```
