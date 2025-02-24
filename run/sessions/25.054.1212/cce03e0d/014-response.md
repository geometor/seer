# cce03e0d • 014 • example_3 • investigate_coder

---
```python
"""
The program takes a 3x3 input grid and creates a 9x9 output grid. The output consists of tiling the input grid in a 3x3 formation and using '0' for every other cell.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((9, 9), dtype=int)

    # get input grid dimensions
    input_height, input_width = input_grid.shape

    # tile the input grid in a 3x3 formation
    for i in range(3):
        for j in range(3):
            output_grid[i * input_height:(i + 1) * input_height, j * input_width:(j + 1) * input_width] = input_grid

    return output_grid
```
