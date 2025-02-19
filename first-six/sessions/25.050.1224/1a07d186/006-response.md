# 1a07d186 • 006 • example_3 - CODE

---
```python
"""
The transformation rule is as follows:
1. There is one main persistent object: an azure horizontal line (color 8) on row 6.
2. Copy, move and change color:
    *   If single cells are color 8, and are not on row 6, then copy that cell one row above and one row below row 6.
    *   Any single cell not being color 8 is deleted.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.zeros_like(input_grid)

    # Find the azure line row
    azure_line_row = -1
    for r in range(input_grid.shape[0]):
        if np.all(input_grid[r] == 8):
            azure_line_row = r
            break

    # Keep the azure line
    if azure_line_row != -1:
      output_grid[azure_line_row, :] = 8

    # Iterate the input
    for r in range(input_grid.shape[0]):
      for c in range(input_grid.shape[1]):
        # Move other single cells
        if input_grid[r,c] == 8 and r != azure_line_row and azure_line_row!=-1:
          output_grid[azure_line_row -1, c] = 8
          output_grid[azure_line_row + 1, c] = 8

    return output_grid
```

