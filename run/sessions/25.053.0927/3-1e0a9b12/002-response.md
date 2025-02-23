# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
Transforms a 4x4 grid by moving all non-zero pixels to the last row,
maintaining their original column-based order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.zeros_like(input_grid)
    # Extract non-zero elements and their column indices
    non_zero_elements = []
    for col_index in range(input_grid.shape[1]):
      for row_index in range(input_grid.shape[0]):
        value = input_grid[row_index, col_index]
        if value != 0:
          non_zero_elements.append( (value, col_index))

    # Sort the elements based on column then row
    # non_zero_elements.sort(key=lambda x: (x[0],x[1])) not needed

    # Place the non-zero elements in the last row of the output grid
    last_row_index = 0
    for element, col in non_zero_elements:
        output_grid[3, last_row_index] = element
        last_row_index += 1

    return output_grid
```
