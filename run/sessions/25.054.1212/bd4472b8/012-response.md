# bd4472b8 • 012 • refine_coder

---
```python
"""
1.  **Copy First Two Rows:** Copy the first two rows of the `input_grid` directly to the `output_grid`.

2.  **Element-wise Column Repetition:** For each element (pixel value) in the first row of the `input_grid`, create a column in the `output_grid` starting from the third row.  Each column consists of the element repeated.

3.  **Number of Added rows**: Two sets of rows equal in height of the input grid, minus two, are added below the copied rows.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input_grid
    output_grid = np.copy(input_grid)

    # Get the first row of the input grid
    first_row = input_grid[0]
    num_rows_to_add = input_grid.shape[0] - 2

    # Iterate through each element in the first row and create new rows
    for i in range(len(first_row)):
        for j in range(num_rows_to_add):
            output_grid[2 + j, i] = first_row[i]
        for j in range(num_rows_to_add):
            output_grid[2 + num_rows_to_add + j, i] = first_row[i]

    return output_grid
```
