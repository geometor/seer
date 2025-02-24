# 794b24be • 036 • refine_coder

---
```python
"""
1.  **Identify Blue Pixels:** Find all blue (value 1) pixels in the input grid.
2.  **Propagate Red:** Iterate through all of the blue pixels. Change the color of the first found blue pixel to red (value 2). Then change all connected blue pixels to red. A connected blue pixel is defined as being directly adjacent (up, down, left, or right) to a red pixel.
3. All other pixels retain their original colors.
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

    # 1. & 2. Identify Blue Pixels and start propagation, for all blues.
    for i in range(rows):
        for j in range(cols):
            if input_grid[i,j] == 1: #must check input grid.
                propagate_red(i, j)


    return output_grid
```

