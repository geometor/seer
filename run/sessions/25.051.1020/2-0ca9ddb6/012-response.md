# 2-0ca9ddb6 • 012 • refine_code - CODE

---
```python
"""
The transformation preserves the positions of existing red, blue, and magenta pixels. It introduces new yellow pixels diagonally adjacent to each red pixel and orange pixels cardinally adjacent to each blue pixel.  All other pixels remain unchanged.
"""

import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all occurrences of a specific color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all red (2) and blue (1) pixels
    red_positions = find_all_pixels(input_grid, 2)
    blue_positions = find_all_pixels(input_grid, 1)

    # Add yellow (4) pixels around each red pixel
    for row, col in red_positions:
        # Diagonally adjacent positions
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = row + dr, col + dc
            # Check boundary conditions
            if 0 <= new_row < rows and 0 <= new_col < cols:
                output_grid[new_row, new_col] = 4

    # Add orange (7) pixels around each blue pixel
    for row, col in blue_positions:
        # Cardinally adjacent positions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            # Check boundary conditions
            if 0 <= new_row < rows and 0 <= new_col < cols:
                output_grid[new_row, new_col] = 7

    return output_grid
```

