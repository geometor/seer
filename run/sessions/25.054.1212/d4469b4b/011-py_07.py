"""
1.  **Resize:** The output grid is always 3x3.
2.  **Center Pixel:** The center pixel (1,1) of the output grid defaults to 0.
3. **Row and Column Checks**
    *   Iterate through each row of the *input* grid. If *any* pixel in that row is non-zero, set output[x,1] = 5 for every row x.
    *   Iterate through each column of the *input* grid. If *any* pixel in that column is non-zero, set output[1,y] = 5 for every column y.
4. **Combine** If there is any row and any column that have a non-zero entry, they will cross at [1,1].
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as 3x3 and filled with 0
    output_grid = np.zeros((3, 3), dtype=int)

    # Row Checks: Iterate through input rows
    for row in input_grid:
        if np.any(row != 0):  # Check if any pixel in the row is non-zero
            output_grid[:, 1] = 5  # set every row in column 1 to 5
            break

    # Column Checks: Iterate through input columns
    for col in input_grid.T:  # Use transpose to iterate through columns
        if np.any(col != 0): # Check if any pixel in the column is non-zero
            output_grid[1, :] = 5   # set every column in row 1 to 5
            break

    return output_grid