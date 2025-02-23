# a85d4709 • 004 • refine_coder

---
```python
"""
Transforms the input grid according to the following rules:

1. If the input pixel is 0, change it to 3.
2. If the input pixel is 5, change it to 2.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Apply the transformation rules
            if input_grid[i][j] == 0:
                output_grid[i][j] = 3
            elif input_grid[i][j] == 5:
                output_grid[i][j] = 2
            else:
                output_grid[i][j] = input_grid[i][j] # Keep original value if not 0 or 5

    return output_grid
```

