# 1f0c79e5 • 008 • example_2 - CODE

---
```python
"""
The transformation rule takes the green pixels in the input and uses them as seeds to "grow" rectangular regions of green, filling the grid downwards and to the right, and replacing any single red object.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding green pixels downwards and to the
    right, overwriting red pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid to find green pixels (value 3).
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 3:
                # Expand the green pixel downwards and to the right.
                for x in range(i, rows):
                    for y in range(j, cols):
                        output_grid[x, y] = 3
            if input_grid[i,j] == 2:
                output_grid[i,j] = 3

    return output_grid
```

