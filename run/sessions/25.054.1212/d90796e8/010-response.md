# d90796e8 • 010 • refine_coder

---
```python
"""
1.  **Iterate:** Examine each pixel in the input grid.
2.  **Locate Green and Red:** Identify pixels that are green (3) or red (2).
3.  **Horizontal Adjacency Check (Green then Red):** If a pixel is green (3) and the pixel immediately to its *right* is red (2), change the green pixel to azure (8). Red pixel remains unchange.
4.  **Horizontal Adjacency Check (Red then Green):** If a pixel is red (2) and the pixel immediately to its *right* is green (3), change both the red pixel and the green pixel to azure (8).
5.  **Preservation:** All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid based on adjacency rules for green and red pixels."""

    output_grid = np.copy(input_grid)  # Initialize output as a copy of input
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            # Check for Green then Red
            if c + 1 < cols and output_grid[r, c] == 3 and output_grid[r, c + 1] == 2:
                output_grid[r, c] = 8  # Change green to azure

            # Check for Red then Green
            elif c + 1 < cols and output_grid[r, c] == 2 and output_grid[r, c + 1] == 3:
                output_grid[r, c] = 8      # Change red to azure
                output_grid[r, c + 1] = 8  # Change green to azure

    return output_grid
```

