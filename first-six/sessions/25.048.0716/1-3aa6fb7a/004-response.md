# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
Copies azure (color 8) objects from the input to the output grid. Then, it finds empty cells (color 0) that are immediately to the right of or below an azure cell, and changes those cells to blue (color 1).
"""

import numpy as np

def is_part_of_2x1_or_1x2(grid, r, c, color):
    #check 2x1
    if r+1 < grid.shape[0] and grid[r+1,c] == color:
        return True

    # Check 1x2
    if c + 1 < grid.shape[1] and grid[r,c+1] == color:
          return True

    if r-1 >= 0 and grid[r-1,c] == color:
        return True

    # Check 1x2
    if c - 1 >= 0 and grid[r,c-1] == color:
          return True
    return False

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate over the input grid
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 8:  # Check for azure cells
                # Check the cell to the right
                if c + 1 < input_grid.shape[1] and input_grid[r, c + 1] == 0:
                    if not is_part_of_2x1_or_1x2(input_grid,r,c,8):
                        output_grid[r, c + 1] = 1
                # Check the cell below
                if r + 1 < input_grid.shape[0] and input_grid[r + 1, c] == 0:
                    if not is_part_of_2x1_or_1x2(input_grid,r,c,8):
                        output_grid[r + 1, c] = 1

    return output_grid
```

