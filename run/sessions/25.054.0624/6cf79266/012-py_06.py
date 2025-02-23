"""
1.  **Initialization:** Create a copy of the input grid to serve as the output grid.
2.  **Iteration:** Examine every possible 3x3 sub-grid within the input grid.
3.  **White Region Identification:** For each 3x3 sub-grid:
    *   Check if *all* nine pixels within the sub-grid are white (color code 0).
4.  **Color Transformation:** If a 3x3 sub-grid is identified as being entirely white:
    * Change the color of *all* pixels within that sub-grid to blue (color code 1).
5.  **Preservation:** Pixels that are not part of any all-white 3x3 sub-grid are not modified.
6. **Output:** Return the modified copy of the input.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through all possible 3x3 subgrids
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Check if the current 3x3 subgrid is all white
            is_white = True
            for i in range(3):
                for j in range(3):
                    if input_grid[r + i, c + j] != 0:
                        is_white = False
                        break  # Exit inner loops if a non-white pixel is found
                if not is_white:
                    break  # Exit outer loop if a non-white pixel is found

            # Change color to blue if it's an all-white 3x3 subgrid
            if is_white:
                for i in range(3):
                    for j in range(3):
                        output_grid[r + i, c + j] = 1

    return output_grid