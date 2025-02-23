# 6ecd11f4 • 018 • refine_coder

---
```python
"""
Extract a subgrid from the lower-right of the input, based on where non-zero
colors are located, then shift the rows. The subgrid can be 3x3 or 4x4.

1. **Determine output size:** Based on example 1 and 2, the output size should be 3x3 if the non-zero pixels in the lower-right are arranged in such way. Otherwise, it will be 4x4.
2. **Locate Subgrid:** Find a 3x3 or 4x4 area in the input grid's lower-right section. This will not require containing ALL non-zero colors, just the ones appearing in the output.
3. **Extract Rows:** Get the rows within this subgrid.
4. **Circular Shift Right:** Shift each extracted row to the right circularly.
5. **Construct Output Grid:** Build the output from the shifted rows.
"""

import numpy as np

def get_subgrid(grid):
    rows, cols = grid.shape
    
    # Try to find a 3x3 subgrid first
    for r in range(rows - 3, -1, -1):
        for c in range(cols - 3, -1, -1):
            subgrid = grid[r:r+3, c:c+3]
            if np.count_nonzero(subgrid) > 0: # Found non empty 3x3, check surrounding for 4x4
               
                # Check for non zero pixels around the identified 3x3 area
                
                up_row = r - 1
                down_row = r + 3
                left_col = c - 1
                right_col = c + 3

                
                non_zero_found = False
                if up_row >= 0:
                    if np.count_nonzero(grid[up_row, max(0, c):min(cols,c+3)]) > 0:
                        non_zero_found = True

                if down_row < rows:
                    if np.count_nonzero(grid[down_row, max(0, c):min(cols, c+3)]) > 0:
                         non_zero_found = True

                if left_col >= 0:
                    if np.count_nonzero(grid[max(0,r):min(rows, r+3), left_col]) > 0:
                        non_zero_found = True

                if right_col < cols:
                    if np.count_nonzero(grid[max(0, r):min(rows, r+3), right_col]) > 0:
                        non_zero_found = True

                # also consider diagonals

                if up_row >= 0 and left_col >= 0:
                    if grid[up_row, left_col] > 0:
                        non_zero_found = True

                if up_row >= 0 and right_col < cols:
                    if grid[up_row, right_col] > 0:
                        non_zero_found = True
                        
                if down_row < rows and left_col >= 0:
                    if grid[down_row, left_col] > 0:
                         non_zero_found = True
                
                if down_row < rows and right_col < cols:
                    if grid[down_row, right_col] > 0:
                         non_zero_found = True

                if non_zero_found:
                    # try 4x4
                  for r4 in range(rows - 4, -1, -1):
                    for c4 in range(cols - 4, -1, -1):
                        subgrid4 = grid[r4:r4+4, c4:c4+4]
                        if np.count_nonzero(subgrid4) > 0:
                            return subgrid4, 4
                  
                return subgrid, 3  # return 3x3
    
    
    return np.zeros((3,3), dtype=int), 3  # fallback

def circular_shift_right(row):
    return [row[-1]] + row[:-1]

def transform(input_grid):
    grid = np.array(input_grid)

    # 1. & 2. Locate and Extract Subgrid
    subgrid, size = get_subgrid(grid)

    # 3. Extract Rows
    rows = [list(row) for row in subgrid]

    # 4. Circular Shift
    shifted_rows = [circular_shift_right(row) for row in rows]

    # 5. Construct Output
    output_grid = shifted_rows
    
    return output_grid
```
