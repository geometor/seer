# 794b24be • 056 • example_10 • investigate_coder

---
```python
"""
1.  **Initialization:** Start with a 3x3 input grid filled with pixels of colors white (0) and blue (1).

2.  **Color Transformation:**
    *   Iterate through each pixel in the input grid.
    *   If a pixel is blue (1), change its color to red (2) on the first row, leave the blue pixel below to white (0), or to white (0) if not on the first row and it's a blue pixel.
    *   If a pixel is white (0), it remains white (0).

3.  **Output:** The result is a 3x3 output grid with pixels of colors white (0) and red (2).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # get dimensions of grid
    rows, cols = output_grid.shape

    # Iterate through each cell of the grid
    for i in range(rows):
        for j in range(cols):
            # If the pixel is blue (1)
            if input_grid[i, j] == 1:
              # Change it to red (2)
              if i == 0:
                output_grid[i,j] = 2
              elif i > 0:
                if input_grid[i,j] == 1:
                  output_grid[i,j] = 0

    return output_grid
```
