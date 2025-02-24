# 995c5fa3 • 016 • refine_coder

---
```python
"""
1.  **Input Analysis:** Examine the input grid to determine if there is a white pixel in any column.

2.  **Column-Row Mapping:**
    *   If there's *any* white pixel in column 4 (index 4) of the input, fill the *first* row of the output grid with azure (8).
    *   If there's *any* white pixel in column 8 (index 8) of the input, fill the *second* row of the output grid with red (2).
    *   If there's *any* white pixel in column 9 (index 9) of the input, fill the *third* row of the output grid with yellow (4).

3.  **Output Construction:** Create a 3x3 output grid. Apply the mappings specified in step 2. It's important to apply all applicable rules - check columns 4, 8, and 9 regardless of the others.

4. Note - if a column is not present or there are no white pixels present in that column, then that output row will be all black (0).
"""

import numpy as np

def check_column_for_white(grid, col_index):
    # Check if any pixel in the specified column is white (0)
    return 0 in grid[:, col_index]

def transform(input_grid):
    # Initialize a 3x3 output grid with all zeros (black)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check column 4 for white pixels and fill row 0 with azure (8) if found
    if input_grid.shape[1] > 4 and check_column_for_white(input_grid, 4):
        output_grid[0, :] = 8

    # Check column 8 for white pixels and fill row 1 with red (2) if found
    if input_grid.shape[1] > 8 and check_column_for_white(input_grid, 8):
        output_grid[1, :] = 2

    # Check column 9 for white pixels and fill row 2 with yellow (4) if found
    if input_grid.shape[1] > 9 and check_column_for_white(input_grid, 9):
        output_grid[2, :] = 4

    return output_grid
```
