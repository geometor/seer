# 0d3d703e • 002 • example_1 - CODE

---
```python
"""
The program takes a 3x3 input grid of integers and transforms it into a 3x3 output grid of integers. For each cell in the input grid, add a constant value of 1 to obtain new value. The spatial configuration is not changed.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Add 1 to each element of the input grid to get the output grid.
    output_grid = output_grid + 1

    return output_grid
```
