# 3af2c5a8 • 004 • example_2 - CODE

---
```python
"""
The transformation rule scales the input grid by a factor of 2 in both dimensions.
It replicates 2x2 squares of the input color (3, green) wherever two pixels were orthogonally adjacent.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    for i in range(rows):
        for j in range(cols):
            output_grid[2*i, 2*j] = input_grid[i,j]
            output_grid[2*i+1, 2*j] = input_grid[i,j]
            output_grid[2*i, 2*j+1] = input_grid[i,j]
            output_grid[2*i+1, 2*j+1] = input_grid[i,j]
    return output_grid.tolist()

```

