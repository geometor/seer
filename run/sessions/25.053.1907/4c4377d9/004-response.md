# 4c4377d9 • 004 • refine_coder

---
```python
"""
The input grid is duplicated vertically.  In the duplicated rows, all colors are cyclically shifted one position to the right.
"""

import numpy as np

def shift_row_right(row):
    """Shifts a row to the right by one, wrapping around."""
    return np.roll(row, 1)

def transform(input_grid):
    # Initialize output_grid with double the height
    output_grid = np.zeros((input_grid.shape[0] * 2, input_grid.shape[1]), dtype=int)

    # Duplicate the input grid into even rows
    for i in range(input_grid.shape[0]):
        output_grid[i*2] = input_grid[i]

    # Copy and shift the odd rows
    for i in range(input_grid.shape[0]):
        original_row = input_grid[i]
        shifted_row = shift_row_right(original_row)  # Use helper function
        output_grid[(i*2)+1] = shifted_row

    return output_grid
```
