# dae9d2b5 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is a simple color substitution: green and yellow pixels are replaced by magenta pixels, while white pixels remain unchanged. The spatial arrangement of pixels is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by replacing green (3) and yellow (4) pixels with magenta (6) pixels,
    while keeping white (0) pixels unchanged.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel in the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color substitution rules.
            if output_grid[i, j] == 3 or output_grid[i, j] == 4:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 0:
                output_grid[i, j] = 0  # Redundant, but kept for clarity.

    return output_grid
```
