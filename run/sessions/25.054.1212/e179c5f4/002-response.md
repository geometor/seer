# e179c5f4 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to create an output grid of the same dimensions as the input grid, 
where the cells alternate between azure (8) and blue (1) colors in a checkerboard pattern. 
The top-left cell is always azure.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # change output pixels 
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                output_grid[i][j] = 8  # Azure
            else:
                output_grid[i][j] = 1  # Blue

    return output_grid
```

