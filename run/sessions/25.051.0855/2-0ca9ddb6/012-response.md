# 2-0ca9ddb6 • 012 • refine_code - CODE

---
```python
"""
The transformation preserves single cells of colors 2, 1, and 6. It adds color 4 around color 2 cells and color 7 around color 1 cells based on specific rules.

For each cell of color 2:
- Place color 4 one cell above and to the left/right.
- Place color 4 one cell below and to the left/right.

For each cell of color 1:
- Place color 7 one cell above.
- Place color 7 in the immediate left, right, above and below cells.
- Place color 7 in the top-left, top-right, bottom-left and bottom-right corners
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the objects of color 2, 1 and 6.  These are all single cells.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)
    objects_6 = find_objects(input_grid, 6) # This line wasn't used in previous iterations, but kept for completeness.

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        # Color 4 above and to the sides
        if row - 1 >= 0:
            if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 4
        # Color 4 below and to the sides
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 4

    # Apply rules for object of color 1.
    for obj_1 in objects_1:
        row, col = obj_1
        # Place 7 above
        if row - 1 >= 0:
            output_grid[row - 1, col] = 7
        # Place 7 to the left and right.
        if col - 1 >= 0:
           output_grid[row,col-1] = 7
        if col + 1 < output_grid.shape[1]:
            output_grid[row,col+1] = 7
        # Place 7 below
        if row + 1 < output_grid.shape[0]:
            output_grid[row+1,col] = 7

        # Place 7 in the corners of the 3x3 neighborhood
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 7
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 7
        if row -1 >= 0:
             if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 7
             if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 7

    return output_grid
```

