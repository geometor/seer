"""
1.  **Identify the central column:** Locate the middle column of the input grid.
2.  **Remove the central column:** Exclude the central column from further
    processing.
3.  **Copy the reduced grid**. Copy the value of columns at each location.
4. **Replace colors**: if a pixel is 9 change to 8, all other pixels will be 0.
5.  **Output:** Return this new grid as the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # identify and remove the central column (conceptually)
    # since we are creating the new output, we are just not using the center

    # copy first and last column and replace
    for r in range(rows):
        # first column
        if input_grid[r,0] == 9:
            output_grid[r,0] = 8

        # last column
        if input_grid[r,-1] == 9:
           output_grid[r,-1] = 8

        c = cols // 2
        if input_grid[r, c] == 9:
            output_grid[r,1] = 8

    return output_grid.tolist()