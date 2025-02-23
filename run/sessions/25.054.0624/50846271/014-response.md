# 50846271 • 014 • example_3 • investigate_coder

---
```python
"""
Identify red (2) pixels and, for some, replace them and neighboring gray(5) pixels to azure(8).
Preserve the colors of all other pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing red pixels and some adjacent gray pixels with azure.
    """
    output_grid = np.copy(input_grid)
    red_pixels = np.argwhere(input_grid == 2)

    for r, c in red_pixels:
        output_grid[r,c] = 8
        # Check neighbors and conditionally replace gray with azure, based on output example
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
            #Diagonals:
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c-1),
            (r+1, c+1)
        ]
        for nr, nc in neighbors:
            if 0 <= nr < output_grid.shape[0] and 0 <= nc < output_grid.shape[1] and output_grid[nr, nc] == 5:
                output_grid[nr, nc] = 8

    return output_grid
```

