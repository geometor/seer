# 6ecd11f4 • 010 • refine_coder

---
```python
"""
1.  **Locate Target Region:** Scan the input grid from the bottom up. Find a rectangular region of non-zero colored pixels. This region is likely bordered by zero-colored pixels, at least above it. The region can vary in size like 3x3 or 4x4.
2.  **Extract Region:** Once the region defined above is found. Copy all pixels values from the target region cells.
3.  **Create Output Grid:** Construct an output grid with the same shape and size as the target region.
4.  **Arrange:** Place the colors in order into the output grid.
"""

import numpy as np

def find_target_region(grid):
    """Finds the rectangular region of non-zero pixels at the bottom."""
    rows, cols = grid.shape
    bottom_row = rows - 1

    # Find the bottom-most non-zero row
    while bottom_row >= 0 and np.all(grid[bottom_row] == 0):
        bottom_row -= 1

    if bottom_row < 0:  # No non-zero pixels found
        return None, None, None, None

    # Find top of the region
    top_row = bottom_row
    while top_row >= 0 and np.any(grid[top_row] != 0):
        top_row -=1
    top_row += 1 #the previous iteration has all 0

    # Find leftmost and rightmost columns
    left_col = 0
    while left_col < cols and np.all(grid[top_row:bottom_row+1,left_col] == 0):
      left_col +=1
    right_col = cols -1
    while right_col > 0 and np.all(grid[top_row:bottom_row+1,right_col] == 0):
      right_col -= 1

    return top_row, bottom_row, left_col, right_col

def transform(input_grid):
    """Transforms the input grid by extracting a multi-colored region at the bottom."""
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the target region
    top_row, bottom_row, left_col, right_col = find_target_region(input_grid)

    if top_row is None:  # Handle case where no region is found
        return []

    # Extract the region
    output_grid = input_grid[top_row:bottom_row+1, left_col:right_col+1].copy()

    return output_grid.tolist()
```
