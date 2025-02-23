# 5c2c9af4 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation identifies isolated green pixels in the input grid.  For each isolated green pixel, it extends green pixels horizontally and vertically, creating lines.  These lines stop when they encounter a non-white pixel or the edge of the grid.
"""

import numpy as np

def is_isolated(grid, row, col):
    """Checks if a green pixel is isolated (not adjacent to other green pixels)."""
    if grid[row, col] != 3:
        return False

    height, width = grid.shape
    for i in range(max(0, row - 1), min(height, row + 2)):
        for j in range(max(0, col - 1), min(width, col + 2)):
            if (i, j) != (row, col) and grid[i, j] == 3:
                return False  # Found an adjacent green pixel
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(height):
        for col in range(width):
            # Check for isolated green pixels
            if is_isolated(input_grid, row, col):
                # Horizontal expansion (left)
                for j in range(col - 1, -1, -1):
                    if input_grid[row, j] == 0:
                        output_grid[row, j] = 3
                    else:
                        break
                # Horizontal expansion (right)
                for j in range(col + 1, width):
                    if input_grid[row, j] == 0:
                        output_grid[row, j] = 3
                    else:
                        break
                # Vertical expansion (up)
                for i in range(row - 1, -1, -1):
                    if input_grid[i, col] == 0:
                        output_grid[i, col] = 3
                    else:
                        break
                # Vertical expansion (down)
                for i in range(row + 1, height):
                    if input_grid[i, col] == 0:
                        output_grid[i, col] = 3
                    else:
                        break

    return output_grid
```
