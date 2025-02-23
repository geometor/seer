# 5-150deff5 • 005 • example_3 - NLP

---
**Natural Language Program:**

The transformation applied to the input grid is based on the column index of each cell. The steps are as follows:

1. **Iterate through each cell:** Examine every cell in the input grid, row by row, column by column.

2. **Check for gray color:** For each cell, check if its color is gray (color code 5).

3. **Apply column-based recoloring:**
    - If the cell's color is gray (5) and its **column index is 4 or greater** (considering 0-based indexing), change the cell's color to **azure** (color code 8).
    - If the cell's color is gray (5) and its **column index is less than 4**, change the cell's color to **red** (color code 2).

4. **Maintain other colors:** If the cell's color is not gray (5), leave it unchanged.

In essence, gray cells in columns 0, 1, 2, and 3 are transformed to red, and gray cells in columns 4 and onwards are transformed to azure.  Non-gray cells remain unchanged.

```python
"""
The transformation applied to the input grid is based on the column index of each cell.

1. **Iterate through each cell:** Examine every cell in the input grid.
2. **Check for gray color:** For each cell, check if its color is gray (color code 5).
3. **Apply column-based recoloring:**
    - If gray and column index is 4 or greater, change to azure (color code 8).
    - If gray and column index is less than 4, change to red (color code 2).
4. **Maintain other colors:** If not gray, leave unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid based on column index and gray color."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 5: # If the cell is gray
                if j >= 4:
                    output_grid[i, j] = 8 # Azure if column index is 4 or greater
                else:
                    output_grid[i, j] = 2 # Red if column index is less than 4
    return output_grid
```
