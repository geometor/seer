# 4c4377d9 • 004 • refine_coder

---
```python
"""
1.  **Input:** Take the input grid, which is a 3x4 grid of colored pixels.
2.  **Reorder and Duplicate Rows:** Create a new grid by reordering and duplicating the rows of the input grid. The new row order is determined by the following sequence of original row indices: 2, 1, 0, 0, 1, 2. This means:
    *   The first row of the output grid is the *third* row of the input grid.
    *   The second row of the output grid is the *second* row of the input grid.
    *   The third row of the output grid is the *first* row of the input grid.
    *   The fourth row of the output grid is the *first* row of the input grid (duplicated).
    *   The fifth row of the output grid is the *second* row of the input grid (duplicated).
    *   The sixth row of the output grid is the *third* row of the input grid (duplicated).
3.  **Output:** The resulting 6x4 grid is the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = []

    # get the rows using the mapping [2, 1, 0, 0, 1, 2]
    row_indices = [2, 1, 0, 0, 1, 2]
    for i in row_indices:
        output_grid.append(input_grid[i].tolist())

    return output_grid
```
