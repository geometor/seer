# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
The non-zero digits are extracted from the input, preserved, and then placed in the last row of the output grid, ordered from left to right. All other cells become 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Extract non-zero elements and their original positions.
    non_zero_elements = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] != 0:
                non_zero_elements.append(input_grid[r][c])

    # Place the non-zero elements in the last row.
    last_row_index = 0
    for val in non_zero_elements:
        output_grid[rows - 1][last_row_index] = val
        last_row_index += 1

    return output_grid
```
