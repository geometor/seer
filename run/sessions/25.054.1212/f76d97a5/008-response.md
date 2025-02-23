# f76d97a5 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Initialization:** Start with an input grid of size 5x5.
2.  **Gray Replacement:** Iterate through every pixel in the input grid. If a pixel is gray (5), change it to white (0).
3.  **Magenta Replacement (Conditional):** Iterate through the grid again.
    *   Examine the color magenta (6)
    *   For each pixel that has the color magenta (6) replace with white (0) if the pixel meets *any* of the following conditions:
        *   The pixel is located in either the top-left, top-right, bottom-left, or bottom-right corner.
        *   If the pixel directly to its left *and* the pixel directly above it have a magenta (6) color.
        *    If the pixel directly to its right *and* the pixel directly above it have a magenta (6) color.
        *   If the pixel directly to its left *and* the pixel directly below it have a magenta (6) color.
        *    If the pixel directly to its right *and* the pixel directly below it have a magenta (6) color.

4.  **Output:** The resulting grid is the output.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Gray Replacement
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                output_grid[r, c] = 0

    # Magenta Replacement
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 6:
                # Corner Cases
                if (r == 0 and c == 0) or \
                   (r == 0 and c == cols - 1) or \
                   (r == rows - 1 and c == 0) or \
                   (r == rows - 1 and c == cols - 1):
                    output_grid[r, c] = 0
                # L-shape Cases
                else:
                    if r > 0 and c > 0 and output_grid[r-1, c] == 6 and output_grid[r, c-1] == 6:
                        output_grid[r, c] = 0
                    elif r > 0 and c < cols - 1 and output_grid[r-1, c] == 6 and output_grid[r, c+1] == 6:
                        output_grid[r,c] = 0
                    elif r < rows - 1 and c > 0 and output_grid[r+1, c] == 6 and output_grid[r, c-1] == 6:
                        output_grid[r,c] = 0
                    elif r < rows - 1 and c < cols -1 and output_grid[r+1, c] == 6 and output_grid[r, c+1] == 6:
                        output_grid[r,c] = 0
    return output_grid
```
