# 25d8a9c8 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule consolidates colors. If the pixel is red or maroon, it becomes white. If it is yellow, it becomes gray.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the color mapping rule.
    """
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel of the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color mapping
            if input_grid[i, j] == 2 or input_grid[i, j] == 9:
                output_grid[i, j] = 0
            elif input_grid[i, j] == 4:
                output_grid[i, j] = 5
            else:
                output_grid[i,j] = input_grid[i,j] # in case a color is not in the rule, defualt is no change

    return output_grid
```

