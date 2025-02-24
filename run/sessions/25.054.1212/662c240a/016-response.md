# 662c240a • 016 • refine_coder

---
```python
"""
1.  **Iterate upwards:** Start from the bottom of the input grid and move upwards, row by row.
2.  **Identify Blocks**: look at groups of rows, and compare this to the group of rows immediately above.
3.  **Check for complete row differences**: compare to find adjacent rows with all colors are different.
4.  **Extract Block:** Once a change is identified, select all rows *below* it.
5.  **Output**: Return the selected section
"""

import numpy as np

def _rows_all_different(row1, row2):
    """Helper function to check if all elements in two rows are different."""
    return not np.any(row1 == row2)

def transform(input_grid):
    """
    Transforms the input grid by extracting the bottom-most block of rows
    that is different from the block above it.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape
    
    if rows <= 1: # Handle edge case with a single-row input, or empty
        return grid.tolist()

    for i in range(rows - 1, 0, -1):
        #compare the current row with row above
        if _rows_all_different(grid[i], grid[i-1]):
            output_grid = grid[i:]
            return output_grid.tolist()

    return grid.tolist() #return entire thing if no change found
```
