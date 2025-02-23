"""
1.  **Identify the center column:** In a square grid, find the central vertical column.
2.  **Examine the First Three Rows**: If colors 4 or 7 appear in the first three rows of the input grid, then
      - pixels with value 0 in the first three rows where columns are all 0, change to 7
      - All other pixels remain unchanged, including original 4 and 7.
3. **Otherwise**:
    *   If there is green (3) in the central column, change it to blue (1).
    *   If there is blue (1) *not* in the center column, change it to green (3).
4.  **All other pixels remain unchanged.**
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)  # Initialize output grid with the original values
    rows, cols = input_grid.shape
    center_col = cols // 2  # Integer division to find center column.

    # Check for 4 or 7 in the first three rows
    first_three_rows = input_grid[:3, :]
    if 4 in first_three_rows or 7 in first_three_rows:
        #change 0 to 7 in first three rows if the column contains only zeros
        for r in range(min(3, rows)):
            for c in range(cols):
                if output_grid[r,c] == 0:
                    col_values = output_grid[:, c]
                    if np.all(col_values[:3] == 0) or np.all(col_values[:3] == np.array([0,0,7])): #check first three rows
                        output_grid[r,c] = 7
        return output_grid

    # Iterate over each cell of input and apply rule if no 4 or 7 in first three rows
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3 and c == center_col:  # Green and in center column.
                output_grid[r, c] = 1
            elif input_grid[r, c] == 1 and c != center_col:  # Blue and not in center column.
                output_grid[r, c] = 3
    return output_grid