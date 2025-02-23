# 4c4377d9 • 006 • refine_coder

---
```python
"""
1.  **Initialization:** Begin with the input grid.
2.  **Duplication:** Duplicate the entire input grid vertically. This doubles the height.
3.  **Row Reordering:** Reorder the rows of this new grid such that the order of rows, using the *original* row indices before duplication, is 3, 2, 1, 3, 2, 1 (using 1-based indexing) or:
    - The first row of the input grid becomes the *third* row of the output.
    - The second row of the input grid becomes the *second* row of the output.
    - The third row of the input grid becomes the *first* row of the output.
    - The first row of the *duplicated part* becomes the *fourth* row.
    - The second row of the *duplicated part* becomes the *fifth* row.
    - The third row of the *duplicated part* becomes the *sixth* row.

There are no color swaps.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid by duplicating the input
    output_grid = np.concatenate((input_grid, input_grid), axis=0)

    # Get the original rows
    original_rows = [input_grid[i].copy() for i in range(input_grid.shape[0])]

    # Reorder the rows according to rule 3, 2, 1, 3, 2, 1.
    new_order = [2, 1, 0, 2, 1, 0]  # Use 0-based indexing.
    
    row_index = 0
    for i in new_order:
        output_grid[row_index] = original_rows[i]
        row_index += 1

    return output_grid
```

