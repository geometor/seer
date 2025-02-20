# 2-0ca9ddb6 • 006 • example_2 - CODE

---
```python
"""
The transformation rule preserves single cells of colors 2 and 1. It then introduces new objects based on the positions of these preserved cells.

For each cell of color 2:
- Two cells of color 4 are placed in the row above, one column to the left and right.
- Two cells of color 4 are placed in the row below, one column to the left and right.

For each cell of color 1:
- A cell of color 7 is placed in the row above.
- Cells of color 7 fill the 3x3 neighborhood around the original cell, excluding the cell itself.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid, but with all zeros.
    output_grid = np.zeros_like(input_grid)
    
    #Find single cells of color 8, and keep in output
    objects_8 = find_objects(input_grid, 8)
    for obj_8 in objects_8:
        row, col = obj_8
        output_grid[row, col] = 8
        
    # Find the objects of color 2 and 1.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)
    
    #Keep color 2 and 1 cells
    for obj_2 in objects_2:
        row, col = obj_2
        output_grid[row, col] = 2

    for obj_1 in objects_1:
        row, col = obj_1
        output_grid[row,col] = 1

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        if row - 1 >= 0:
            if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 4
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:    
                output_grid[row + 1, col + 1] = 4
    
    # Apply rules for object of color 1
    for obj_1 in objects_1:
        row, col = obj_1
        if row - 1 >= 0:
            output_grid[row-1, col] = 7
        for i in range(max(0, row - 1), min(row + 2, output_grid.shape[0])):
            for j in range(max(0, col - 1), min(col + 2, output_grid.shape[1])):
                if (i,j) != (row, col):
                     output_grid[i,j] = 7

    return output_grid
```

