# 1b2d62fb • 024 • refine_coder

---
```python
"""
1.  **Initialize Output:** Create an output grid with the same number of rows as the input grid and 3 columns. Initialize all cells to 0.
2.  **Identify Key Columns:** Determine the first (index 0), middle (index `cols // 2`), and last (index -1) columns of the input grid.
3.  **Check for Complete Maroon Stripes:** For each of the key columns (first, middle, last):
    *   Check if there's a *complete* vertical stripe of maroon (color 9) spanning the entire column. A complete stripe means that *all* cells in that column have the value 9.
4. **Process Each Row**: Iterate through each row of the input grid.
5.  **Generate Output Columns Based on Stripes:** For each row and for each of the key input columns (first, middle, last):
    *   If a *complete* maroon stripe exists in the corresponding key input column:
        *   Set the corresponding output column cell for the current row to 0.
    *   Otherwise (no complete stripe):
        * If the cell in the key input column and the row contains 9 set the output to 8, otherwise, set to 0.
6.  **Return:** Return the completed output grid.
"""

import numpy as np

def _check_complete_stripe(input_grid, col_index):
    """Checks for a complete vertical stripe of color 9."""
    input_grid = np.array(input_grid)
    rows = input_grid.shape[0]
    for r in range(rows):
        if input_grid[r, col_index] != 9:
            return False  # Not a complete stripe
    return True

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # Identify key columns
    key_columns = [0, cols // 2, -1]

    # Check for complete maroon stripes and generate output
    for i, col_index in enumerate(key_columns):
        complete_stripe = _check_complete_stripe(input_grid, col_index)

        for r in range(rows):
            if complete_stripe:
                output_grid[r, i] = 0
            else:
                # correct for negative index
                if col_index < 0:
                  col_index_use = cols + col_index
                else:
                  col_index_use = col_index
                
                if input_grid[r, col_index_use] == 9:
                    output_grid[r, i] = 8
                # else already 0 from initialization

    return output_grid.tolist()
```
