# e9afcf9a • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to alternate the colors of the input grid's rows in the output grid. The first row of the output grid starts with the color of the first row of the input grid, and the second row of the output grid starts with the color of the second row of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by alternating colors in each row of the output grid.
    """
    # Get the dimensions of the input grid
    rows, cols = input_grid.shape

    # Initialize the output grid with the same dimensions
    output_grid = np.zeros_like(input_grid)

    # Get the colors from the first and second rows of the input grid
    color1 = input_grid[0, 0]
    color2 = input_grid[1, 0]

    # Transform the first row, starting with color1
    for j in range(cols):
        output_grid[0, j] = color1 if j % 2 == 0 else color2

    # Transform the second row, starting with color2
    for j in range(cols):
        output_grid[1, j] = color2 if j % 2 == 0 else color1

    return output_grid
```
