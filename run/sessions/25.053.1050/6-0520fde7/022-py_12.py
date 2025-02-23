"""
1.  **Excise:** Remove the fourth column (the gray column) from the input grid.
2.  **Condense:** Create a 3x3 output grid. For each row, select the first three non-gray color values to create the corresponding row in the output grid.
3.  **Color Conversion:** Iterate through each cell of the *output* grid.
    *   If a cell is blue AND it is in the first column or third column change it to red.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)

    # 1. Excise Column: Remove the fourth column (index 3).
    grid = np.delete(grid, 3, axis=1)

    # 2. Condense: Create 3x3, taking first three non-gray values in each row.
    output_grid = np.zeros((3, 3), dtype=int)
    for i in range(3):
        non_gray_cols = [val for val in grid[i] if val != 5]
        output_grid[i] = non_gray_cols[:3]


    # 3. Color Conversion: Check for blue pixels and their column.
    for r in range(3):
        for c in range(3):
            if output_grid[r, c] == 1:
                if c == 0 or c==2:
                  output_grid[r,c] = 2

    return output_grid