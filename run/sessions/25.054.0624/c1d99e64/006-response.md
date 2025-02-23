# c1d99e64 • 006 • refine_coder

---
```python
"""
1. Copy: Create a copy of the input grid.
2. Calculate Center: Determine the center row and center column indices of the grid.
    *   Center row index = number of rows // 2
    *   Center column index = number of columns // 2
3. Draw Red Row: Change all cell values in the center row of the copied grid to 2 (red).
4. Draw Red Column: Change all cell values in the center column of the copied grid to 2 (red).
5. Return: The modified grid is the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find the center row index.
    center_row = rows // 2
    
    # Overwrite all pixels in center_row with red (2)
    output_grid[center_row, :] = 2

    # find the center column index
    center_col = cols // 2

    # Overwrite all pixels in the center column with red
    output_grid[:, center_col] = 2
    
    return output_grid
```

