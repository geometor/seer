# 0d3d703e • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule can be described as follows:

1.  Iterate through each cell in the input grid.
2.  Add 4 to the original value of each cell. If new value is greater than 9 then take the modulo 10. Assign the new value to the same position in output grid.
3.  Output will be the result of adding 4 to each cell value.

Effectively, every value in the grid has 4 added to its original value. Modulo 10 is taken if result is greater than 9.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Add 4 to the original value of the cell and assign the new value to the output grid.
            output_grid[i, j] = (output_grid[i,j] + 4) % 10

    return output_grid
```
