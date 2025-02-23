"""
1.  **Iterate through the grid:** Examine every possible 3x3 sub-grid within the input grid.
2.  **Identify White Regions:** For each 3x3 sub-grid, check if all nine pixels are white (0).
3.  **Change Color:** If a 3x3 sub-grid is entirely white, change all of its pixels to blue (1).
4. **Preserve Other Pixels** All pixels not part of any all-white 3x3 regions retain their original colors.
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