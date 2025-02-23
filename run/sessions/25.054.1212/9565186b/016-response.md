# 9565186b • 016 • refine_coder

---
```python
"""
The transformation rule is: Replace all azure (8) pixels in the input grid with gray (5) pixels. Keep all other color pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Replace azure (8) with gray (5), keep all other colors unchanged.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through all pixels
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Replace all instances of 8 (azure) with 5 (gray).
            if output_grid[i, j] == 8:
                output_grid[i, j] = 5

    return output_grid
```
