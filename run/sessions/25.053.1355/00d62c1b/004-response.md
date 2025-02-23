# 00d62c1b • 004 • refine_coder

---
```python
"""
1.  **Identify Crosses:** Locate "cross-shaped" objects within the input grid. These are contiguous regions of green (3) pixels. A cross-shape must have at least one green pixel with green neighbors above and below, or to the left and right, or both.

2.  **Identify Interior Pixels:** Within each cross, identify "interior" green pixels. A green pixel is considered "interior" if it has at least two green neighbors *in opposing directions*. This means:
    *   A green neighbor above AND a green neighbor below.
    *   OR, a green neighbor to the left AND a green neighbor to the right.
    *   OR, Both of the above conditions are met.

3.  **Transform Interior Pixels:** Change the color of all identified interior green pixels to yellow (4).

4. **Leave Other Pixels Unchanged**: All pixels not meeting the above conditions are unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    def is_interior(i, j):
        """Checks if a green pixel is interior to a cross."""
        if input_grid[i, j] != 3:
            return False

        up = i > 0 and input_grid[i-1, j] == 3
        down = i < rows - 1 and input_grid[i+1, j] == 3
        left = j > 0 and input_grid[i, j-1] == 3
        right = j < cols - 1 and input_grid[i, j+1] == 3

        return (up and down) or (left and right)

    # Iterate through each cell of the grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is an interior green pixel.
            if is_interior(i, j):
                # Change the color of the current cell to yellow (4).
                output_grid[i, j] = 4

    return output_grid
```
