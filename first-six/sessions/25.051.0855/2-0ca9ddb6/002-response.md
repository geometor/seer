# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The transformation rule preserves two single cells (colors 2 and 1), and two groups of objects appear around them.
For the object of color 2, insert, in the previous row, two objects of color 4, located on the left and on the right of the imaginary vertical line containing the object of color 2. Copy those two objects in the row below the object.
For the object of color 1, insert, in the previous row, a single object of color 7.
Insert objects of color 7 in all positions of the 3x3 subgrid centered on color 1, except for the position of the object of color 1 itself.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find the objects of color 2 and 1.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        output_grid[row - 1, col - 1] = 4
        output_grid[row - 1, col + 1] = 4
        output_grid[row + 1, col - 1] = 4
        output_grid[row + 1, col + 1] = 4
    
    # Apply rules for object of color 1
    for obj_1 in objects_1:
        row, col = obj_1
        output_grid[row-1, col] = 7
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i,j) != (row, col):
                     output_grid[i,j] = 7


    return output_grid
```

