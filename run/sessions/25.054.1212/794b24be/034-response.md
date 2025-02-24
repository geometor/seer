# 794b24be • 034 • refine_coder

---
```python
"""
1.  **Identify Seed Pixels:** Find all blue (value 1) pixels in the first row of the input grid. These are the "seed" pixels.
2.  **Propagate Red:** From each seed pixel, change its color to red (value 2). Then, iteratively change the color of any directly adjacent (up, down, left, or right) blue pixel to red. Continue this propagation until no more connected blue pixels can be found.
3.  **Handle other Blues:** Iterate through all of the remaining blue pixels. If a pixel is blue and was never changed to red, change it to white.
4.  **Preserve Other Colors:** All other pixels in the input grid that are not blue retain their original color in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Helper function to check if a pixel is within grid bounds.
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Helper function for Depth-First Search (DFS) propagation.
    def propagate_red(r, c):
        if not is_valid(r, c) or output_grid[r, c] != 1:
            return
        output_grid[r, c] = 2  # Change to red
        # Recursively check adjacent pixels
        propagate_red(r + 1, c)
        propagate_red(r - 1, c)
        propagate_red(r, c + 1)
        propagate_red(r, c - 1)

    # 1. Identify Seed Pixels and start propagation.
    for j in range(cols):
        if output_grid[0, j] == 1:
            propagate_red(0, j)

    # 3. Handle Remaining Blue Pixels (convert to white)
    for i in range(rows):
      for j in range(cols):
        if output_grid[i,j] == 1:
          output_grid[i,j] = 0

    return output_grid
```
