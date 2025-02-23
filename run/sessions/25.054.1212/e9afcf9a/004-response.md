# e9afcf9a • 004 • refine_coder

---
```python
"""
The transformation rule is to create an alternating pattern of the two colors present in the input grid. The top-left cell of the output grid has the same color as the top-left cell of the input grid. Adjacent cells (horizontal and vertical) cannot have the same color.
"""

import numpy as np

def transform(input_grid):
    # Identify the two distinct colors.
    rows, cols = input_grid.shape
    color1 = input_grid[0, 0]
    color2 = input_grid[1,0] if rows > 1 else input_grid[0,1]

    # Create the output grid.
    output_grid = np.zeros((rows, cols), dtype=int)

    # Populate the output grid with the alternating pattern.
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                output_grid[i, j] = color1
            else:
                output_grid[i, j] = color2

    return output_grid
```
