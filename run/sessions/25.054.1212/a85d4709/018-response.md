# a85d4709 • 018 • refine_coder

---
```python
"""
Transforms a 3x3 input grid to a 3x3 output grid. The output grid's rows are each filled with a single color, determined by the row index: top row is green (3), middle row is yellow (4), and bottom row is red (2).
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same shape as the input
    output_grid = np.zeros_like(input_grid)

    # Fill the top row (index 0) with green (3)
    output_grid[0, :] = 3

    # Fill the middle row (index 1) with yellow (4)
    output_grid[1, :] = 4

    # Fill the bottom row (index 2) with red (2)
    output_grid[2, :] = 2

    return output_grid
```

