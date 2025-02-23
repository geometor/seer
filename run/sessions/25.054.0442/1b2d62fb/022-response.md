# 1b2d62fb • 022 • refine_coder

---
```python
"""
1.  **Identify Key Columns**: Locate the first, last and middle columns of the
    input grid.
2.  **Create Output Grid:** initialize a grid with dimensions (rows x 3).
3.  **Process Rows:** Iterate through each row of the input grid.
4. **First Column Check:**
    - Set first column of the output to 8 if color 9 is present in first column of input, otherwise set 0.
5. **Center Column Check**:
    - Set second (center) column of output to 8 if color 9 is present in the center column of input, otherwise set 0.
6.  **Last Column Check:**
    - Set third (last) column of the output to 8 if color 9 is present in last column of input, otherwise set 0.
7.  **Output:** Return the new grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # process each row
    for r in range(rows):
        # first column check
        if input_grid[r, 0] == 9:
            output_grid[r, 0] = 8

        # center column check
        center_col = cols // 2
        if input_grid[r, center_col] == 9:
            output_grid[r, 1] = 8

        # last column check
        if input_grid[r, -1] == 9:
            output_grid[r, 2] = 8

    return output_grid.tolist()
```
