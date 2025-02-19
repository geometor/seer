# 0d3d703e • 002 • example_1 - CODE

---
```python
"""
The input grid consists of three columns, each of a single color: green (3), blue (1), and red (2).
Each color is transformed: green (3) -> yellow (4), blue (1) -> gray (5), red (2) -> magenta (6).
The transformation rule is adding 1 to the value of input pixel.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by adding 1 to the color value of each cell.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell of the output grid.
    for i in range(rows):
        for j in range(cols):
            # Add 1 to the color value of the corresponding input cell.
            output_grid[i, j] = input_grid[i, j] + 1

    return output_grid
```

