# AboveBelow8 • 016 • refine_coder

---
```python
"""
Retain azure pixels if and only if they belong to a horizontal line of two or more connected, adjacent azure pixels. Otherwise, replace the pixel with white.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Iterate through the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # If the pixel is azure (8), check its horizontal neighbors.
            if input_grid[i, j] == 8:
                # Check for at least one horizontal neighbor (left or right) that is also azure.
                if (j > 0 and input_grid[i, j - 1] == 8) or \
                   (j < input_grid.shape[1] - 1 and input_grid[i, j + 1] == 8):
                    output_grid[i, j] = 8

    return output_grid
```
