# 0d3d703e • 004 • example_2 - CODE

---
```python
"""
The input grid consists of three columns, each of a single color.
The transformation rule is a color mapping, equivalent to adding a number which may depend on the input color.
In the available examples:
- if the value is 2, add 4
- if the value is 3, add 1
- if the value is 8, add 1
- if the value is 1, add 4
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on a color mapping rule.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell of the output grid.
    for i in range(rows):
        for j in range(cols):
            # Apply the color mapping based on the input value.
            if input_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif input_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif input_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif input_grid[i,j] == 1:
                output_grid[i,j] = 5
            else:
                output_grid[i,j] = input_grid[i,j] #add this in case we have not defined mapping

    return output_grid
```

