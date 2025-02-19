# 2c608aff • 004 • example_2 - CODE

---
```python
"""
A single azure block extends vertically upwards to a fixed row. All other objects remain unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Return None if no object of the specified color is found
    return coords

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule:
    A single azure block extends vertically upwards to a fixed row.
    All other objects remain unchanged.
    """
    output_grid = np.copy(input_grid)
    azure_coords = find_object(input_grid, 8)

    #find single azure object
    if azure_coords is not None:
        #get x coordinate
        x = azure_coords[0][1]

        #modify cells from row of azure to up, until row 5
        row_start = azure_coords[0][0]
        row_end = 2  #inclusive, that is 3rd row from top, that is, 5 in index

        for i in range(row_start, row_end-1, -1):
          output_grid[i][x] = 8

    return output_grid
```

