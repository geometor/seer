# 794b24be • 044 • example_8 • investigate_coder

---
```python
"""
Change all 1s to 2s. Leave 0s as they are.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1s become 2s, and 0s remain 0s.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through the grid and apply the transformation.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 1:
                output_grid[i, j] = 2
            # elif output_grid[i,j] == 0: # not necessary, values are already initialized.
            #     output_grid[i,j] = 0

    return output_grid
```

