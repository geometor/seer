# 0d3d703e • 002 • example_1 - CODE

---
```python
"""
The program takes a 3x3 input grid of digits and transforms it into a 3x3 output grid. For each cell in the input grid, increment the digit value by 1. The resulting value is placed in the corresponding cell of the output grid. The dimensions and arrangement of cells is unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.  We use numpy for easier manipulation.
    output_grid = np.array(input_grid).copy()

    # Iterate through each cell of the output_grid.
    for row_index in range(output_grid.shape[0]):
        for col_index in range(output_grid.shape[1]):
            # Increment the value of the cell by 1.
            output_grid[row_index, col_index] += 1

    return output_grid.tolist()
```
