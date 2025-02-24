# a3df8b1e • 002 • example_1 • investigate_coder

---
```python
"""
Replaces the input grid with a checkerboard pattern of 0s and 1s, starting with 0 at the top-left corner.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid with the same dimensions as the input
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # change output pixels to create a checkerboard pattern
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 1:  # Check if the sum of row and column indices is odd
                output_grid[i][j] = 1

    return output_grid
```
