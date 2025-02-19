# 3af2c5a8 • 002 • example_1 - CODE

---
```python
"""
The transformation rule scales the input grid by a factor of 2 in both dimensions,
replicating the pattern of color 8 (azure) pixels while maintaining the 0 (white) background.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Iterate through the input grid and replicate the pattern.
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 8:
                # Copy the '8' to the corresponding scaled positions.
                output_grid[2*i, 2*j] = 8
                output_grid[2*i, 2*j+1] = 8
                output_grid[2*i+1, 2*j] = 8
                output_grid[2*i+1, 2*j+1] = 8

    return output_grid.tolist()
```

