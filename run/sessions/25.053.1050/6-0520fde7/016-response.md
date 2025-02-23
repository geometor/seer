# 6-0520fde7 • 016 • refine_coder

---
```python
"""
1.  **Central Column Identification:** Find the vertical column in the *input* grid that consists only of gray (5) pixels. This column serves as a reference.

2.  **Output Grid Initialization:** Create a 3x3 output grid filled with white (0) pixels.

3.  **Blue Pixel Detection:** Examine the *input* grid for blue (1) pixels that are directly adjacent (horizontally) to the central gray column.

4.  **Conditional Red Pixel Placement:**
    *   For each blue pixel found in step 3:
        *   If the blue pixel is one cell to the *left* of the central gray column, place a red (2) pixel in the *first* column (index 0) of the *output* grid. The row of the red pixel in the output grid is the *same* as the row of the blue pixel in the input grid.
        *   If the blue pixel is one cell to the *right* of the central gray column, place a red (2) pixel in the *third* column (index 2) of the *output* grid.  The row of the red pixel in the output grid is the *same* as the row of the blue pixel in the input grid.

5.  The central column (index 1) of the output grid always remains white (0).
"""

import numpy as np

def find_central_gray_column(input_grid):
    """Finds the index of the central gray column."""
    height, width = input_grid.shape
    for x in range(width):
        if np.all(input_grid[:, x] == 5):
            return x
    return -1  # Should not happen in valid cases

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the central gray column
    center_col_index = find_central_gray_column(input_grid)

    # Iterate through the input grid and find relevant blue pixels
    height, width = input_grid.shape
    for y in range(height):
        for x in range(width):
            if input_grid[y, x] == 1:
                # Check if the blue pixel is one step left of the center
                if x == center_col_index - 1:
                    output_grid[y, 0] = 2  # First column, same row
                # Check if the blue pixel is one step right of the center
                elif x == center_col_index + 1:
                    output_grid[y, 2] = 2  # Third column, same row

    return output_grid
```

