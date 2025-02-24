# 995c5fa3 • 018 • refine_coder

---
```python
"""
1.  **Input:**  We are given a 2D grid ( `input_grid`) of colored pixels.

2.  **Output:** We will create a 3x3 output grid (`output_grid`), initially filled with black (0).

3. **Column Checks and Row Filling:**
    *   Examine column 4 (index 4) of the `input_grid`. If *any* pixel in this column is white (0), fill the first row (index 0) of the `output_grid` with azure (8). If no white, that row should be black(0)
    *   Examine column 8 (index 8) of the `input_grid`. If *any* pixel in this column is white (0), fill the second row (index 1) of the `output_grid` with red (2). If no white, that row should be black(0)
    *   Examine column 9 (index 9) of the `input_grid`. If *any* pixel in this column is white (0), fill the third row (index 2) of the `output_grid` with yellow (4). If no white, that row should be black(0)

4.  **Output:** The final `output_grid` (3x3) is the result of the transformation. The critical aspect is that the *presence* of a white pixel in the specified *input* column determines the color of the corresponding *output* row. If there is not a white pixel, then the output row should be black(0). If the input column doesn't exist, then the output row should be black(0).
"""

import numpy as np

def check_column_for_white(grid, col_index):
    """Checks if a given column contains any white pixels."""
    if grid.shape[1] <= col_index:
        return False  # Column doesn't exist
    return 0 in grid[:, col_index]

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    # Initialize a 3x3 output grid with all zeros (black)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check column 4 for white pixels and fill row 0 with azure (8) if found
    if check_column_for_white(input_grid, 4):
        output_grid[0, :] = 8

    # Check column 8 for white pixels and fill row 1 with red (2) if found
    if check_column_for_white(input_grid, 8):
        output_grid[1, :] = 2

    # Check column 9 for white pixels and fill row 2 with yellow (4) if found
    if check_column_for_white(input_grid, 9):
        output_grid[2, :] = 4

    return output_grid
```

