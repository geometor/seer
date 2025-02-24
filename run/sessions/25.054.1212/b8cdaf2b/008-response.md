# b8cdaf2b • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Preserve the Bottom Row**: Copy the entire bottom row of the input grid directly to the output grid.
2.  **Preserve other colors**: Copy all non-zero color values, except the green '3', to the output grid in the same locations
3.  **Green Expansion:**.
    - Find the green (3) pixel in the bottom row
    - Create additional green pixels up and to either side in a cross shape, from row 1 to row 2
"""

import numpy as np

def find_object(grid, color):
    positions = []
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == color:
                positions.append([row_idx, col_idx])
    return positions

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    #get height for bounds checking
    height = len(input_grid)

    # copy non green colors
    for row in range(height):
      for col in range(len(input_grid[0])):
        if input_grid[row][col] != 3:
          output_grid[row][col] = input_grid[row][col]

    # find the green objects
    green_objects = find_object(input_grid, 3)

    # green cross expansion.
    for green in green_objects:

        row, col = green

        #check it is on the last row
        if row != height-1: continue

        #expand to cross on rows 1 and 2 (index 0 and 1)
        output_grid[1,0] = 3
        output_grid[1,4] = 3
        output_grid[2,1] = 3
        output_grid[2,3] = 3

    return output_grid
```
