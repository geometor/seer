# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
The input grid is transformed into the output grid by adding 4 to the value of each pixel. If resulting value is more than 9, take the modulo 10 of the value. The structure of the grid and the position of the pixels do not change.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid
    rows, cols = output_grid.shape

    # Iterate through each pixel of the grid
    for i in range(rows):
        for j in range(cols):
            # Add 4 to the pixel value and take modulo 10
            output_grid[i, j] = (output_grid[i, j] + 4) % 10

    return output_grid
```
