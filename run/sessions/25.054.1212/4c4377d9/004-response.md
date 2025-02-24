# 4c4377d9 • 004 • refine_coder

---
```python
"""
The input grid is duplicated. The order of rows is reversed.  The reversed copy is placed at the top of the output, then the original input is added to the bottom.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_np = np.array(input_grid)
    rows, cols = input_np.shape
    output_grid = np.zeros((rows * 2, cols), dtype=int)

    # Reverse and stack the input grid in the top half.
    reversed_input = input_np[::-1]  # Reverse the rows
    output_grid[:rows, :] = reversed_input

    # Copy original input to bottom half
    output_grid[rows:, :] = input_np
    
    return output_grid.tolist()
```
