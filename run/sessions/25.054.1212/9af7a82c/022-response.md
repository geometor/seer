# 9af7a82c • 022 • refine_coder

---
```python
"""
Transforms an input grid into an output grid by:
1. Copying all columns except the last one.
2. Duplicating the first row.
3. Transforming the last column: The first element of the input's last column becomes the first element of the output's last column; the rest are 0.
4. Adding new rows: The number of added rows is one less than the input's row count.
5. Populating the first new row: The first element is the same as the input grid's first element, the rest are 0.
6. Zero-filling the remaining new rows.
"""

import numpy as np

def transform(input_grid):
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows + (input_rows - 1)
    output_cols = input_cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Duplicate the first row
    output_grid[0, :] = input_grid[0, :]

    # Copy all but the last column
    output_grid[1:input_rows, :-1] = input_grid[1:, :-1]

    # Transform the last column
    output_grid[1:input_rows, -1] = input_grid[1:,-1]
    output_grid[input_rows:, -1] = 0

    # Add and populate new rows. First element of first new row.
    output_grid[input_rows, 0] = input_grid[0,0]
    # all remaining values are 0

    return output_grid
```
