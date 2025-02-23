# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule can be summarized by the following process. For each colored cell $c$ located at coordinate $(x,y)$, the output cell is defined by adding the integer 1 to the original color value.

output[x,y] = input[x,y] + 1
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by adding 1 to each cell's color value.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell in the grid.
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            # Add 1 to the color value of each cell.
            output_grid[x, y] = (output_grid[x, y] + 1) % 10

    return output_grid
```

