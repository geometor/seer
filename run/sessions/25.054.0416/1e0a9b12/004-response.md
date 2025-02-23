# 1e0a9b12 • 004 • refine_coder

---
```python
"""
Extract all non-zero elements from the input grid and place them in order on the last row of the output grid, which is the same size as the input. All rows are shifted upward a number of rows equal to the number of rows containing at least on nonzero value.
"""

import numpy as np

def transform(input_grid):
    # Create output grid of the same size as input, filled with zeros.
    output_grid = np.zeros_like(input_grid)
    
    # Extract non-zero elements, preserving order (left-to-right, top-to-bottom).
    non_zero_elements = input_grid[input_grid != 0]
    
    # Count rows with at least one non-zero element
    rows_with_non_zero = np.any(input_grid != 0, axis=1)
    num_rows_to_shift = np.sum(rows_with_non_zero)

    # Extract rows *without* any non-zero elements and shift
    empty_rows = input_grid[~rows_with_non_zero]
    output_grid[:-num_rows_to_shift,:] = empty_rows

    # Place the non_zero elements in the last row of the output grid.
    output_grid[-1, :len(non_zero_elements)] = non_zero_elements
    
    return output_grid
```
