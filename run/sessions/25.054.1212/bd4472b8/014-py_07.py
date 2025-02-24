"""
1.  **Initialization:** Obtain the input grid, which is a 2D array of integers.
2.  **Preserve top:** The first two rows of the input will maintain it's value to the output.
3. **Iterate:** Iterate through each of the next two rows, from row index 2 and row index 3.
4.  **Replacement:** For each pixel within the current row, if the pixel's value is 0 (white): check the position.
5. **Next Two Rows**: Iterate over row index 4 and 5.
6. Replace zero with the value of the first cell (0,0).
7. **Next Two Rows**: Iterate over row index 6 and 7.
8. Replace zero with the value of the second cell (0,1).
9.  **Output:** Return the modified grid as the output grid.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Preserve top two rows
    # No change needed as output_grid is initialized with input_grid

    # Iterate through rows 2 and 3 (index 2 and 3)
    for i in range(2, 4):
        for j in range(cols):
            if output_grid[i, j] == 0:
              output_grid[i,j] = output_grid[0,0]

    # Iterate through rows 4 and 5 (index 4 and 5)
    for i in range(4, min(6,rows)):  #added min() for edge case
        for j in range(cols):
             if output_grid[i, j] == 0:
              output_grid[i,j] = output_grid[0,1]
    
    return output_grid