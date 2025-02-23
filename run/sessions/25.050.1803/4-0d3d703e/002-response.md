# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a simple color replacement. For each cell in the input grid, perform the following color mapping:
change color 3 (green) to color 4 (yellow), color 1 (blue) to color 5 (gray), and color 2 (red) to color 6 (magenta).
In essence, each distinct color present in the input grid is replaced by a new, distinct color in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    3 (green) -> 4 (yellow)
    1 (blue) -> 5 (gray)
    2 (red) -> 6 (magenta)
    """
    # Initialize the output grid as a copy of the input grid to avoid modifying the original.
    output_grid = np.copy(input_grid)

    # Apply the color mapping.  Iterate through each cell and change the color according to the defined rule.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6

    return output_grid
```

