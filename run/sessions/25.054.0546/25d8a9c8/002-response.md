# 25d8a9c8 • 002 • example_1 • investigate_coder

---
```python
"""
Iterate through each cell of the input grid.
Check the color value of the current cell.
Map input color to output color
    If the input cell color is yellow (4), change it to gray (5) in the output grid.
    If the input cell color is red (2) or green(3), change it to white (0) in the output grid.
Place mapped value into the corresponding cell in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # change output pixels 
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == 4:
                output_grid[i, j] = 5
            elif input_grid[i, j] == 2 or input_grid[i, j] == 3:
                output_grid[i, j] = 0
    return output_grid
```
