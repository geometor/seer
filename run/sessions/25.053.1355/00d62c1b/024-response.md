# 00d62c1b • 024 • refine_coder

---
```python
"""
1.  **Iterate through all pixels:** Examine each pixel in the input grid.

2.  **Check for Green:** If the current pixel is *not* green (color 3), move to the next pixel.

3.  **Check Neighbors:** If the current pixel *is* green, examine its four direct neighbors (up, down, left, and right).  *Diagonal* neighbors are *not* considered.

4.  **Interior Condition:** If *all* four direct neighbors are also green (color 3), then the current pixel is considered an "interior" pixel.

5.  **Change Color:** Change the color of any pixel identified as "interior" from green (3) to yellow (4).

6. **Preserve all other pixels:** All other pixels that don't meet the above criteria remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by changing interior green pixels to yellow."""
    output_grid = np.copy(input_grid)

    def is_interior(row, col, grid):
        """Checks if a pixel is an interior pixel (all 4 neighbors are the same color)."""
        color = grid[row, col]
        if color != 3:  # Only check green pixels
            return False

        # Check up, down, left, right neighbors
        neighbors = []
        if row > 0:
            neighbors.append(grid[row - 1, col])
        if row < grid.shape[0] - 1:
            neighbors.append(grid[row + 1, col])
        if col > 0:
            neighbors.append(grid[row, col - 1])
        if col < grid.shape[1] - 1:
            neighbors.append(grid[row, col + 1])

        return all(neighbor == color for neighbor in neighbors)

    # Iterate through all pixels and check for interior pixels
    for row in range(input_grid.shape[0]):
        for col in range(input_grid.shape[1]):
            if is_interior(row, col, input_grid):
                output_grid[row, col] = 4  # Change to yellow

    return output_grid
```
