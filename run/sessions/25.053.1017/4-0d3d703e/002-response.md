# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a one-to-one mapping of input cell values to output cell values. Specifically, input value 3 maps to output value 4, 1 maps to 5, and 2 maps to 6. The dimensions of the grid remain unchanged. The program essentially adds 1 to each value.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the defined mapping: 3->4, 1->5, 2->6.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the grid and apply the mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6
    # alternatively using numpy
    # output_grid[output_grid == 3] = 4
    # output_grid[output_grid == 1] = 5
    # output_grid[output_grid == 2] = 6

    # or a generic +1
    # output_grid = input_grid + 1
    return output_grid
```
