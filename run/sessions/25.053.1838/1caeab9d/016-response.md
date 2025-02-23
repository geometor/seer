# 1caeab9d • 016 • refine_coder

---
```python
"""
1.  **Identify Objects:** Scan the input grid to identify contiguous blocks of pixels with the same color. Each contiguous block is an object.
2.  **Merge Vertically Adjacent Objects:**
    *   Iterate through the grid, from top to bottom.
    *   For each column, identify vertically adjacent pixels that have the same color.
    *   Merge vertically adjacent pixels of the same color into a single object that occupies the rows of all merged pixels. Other tiles of different colors should be eliminated.
    *   Consolidate all merged objects to the left side of the row.
3.  **Maintain Grid Height:** Add an empty row to the top of the grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid based on vertical merging and shifting."""

    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Merge Vertically Adjacent Objects and shift
    merged_row = np.zeros(cols, dtype=int)
    merged_col_idx = 0

    for c in range(cols):
      for r in range(rows - 1):
        if input_grid[r,c] == input_grid[r+1,c] and input_grid[r,c]!=0:
          merged_row[merged_col_idx] = input_grid[r,c]
          merged_col_idx+=1
          break # move onto the next column after a merge

    # Place merged row into output
    for r in range(rows - 1):
      output_grid[r+1] = output_grid[r]
    
    output_grid[0] = merged_row
    

    return output_grid.tolist()
```
