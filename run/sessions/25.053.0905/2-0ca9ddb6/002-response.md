# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
1. Preserve: Keep all original red and blue pixels in their original locations.
2. Add Yellow: For the red pixel, add a yellow pixel one step above, one step below and on each side.
3. Add Orange: For the blue pixel, add a orange pixel one step above, one step below and on each side.
"""

import numpy as np

def find_pixels_by_color(grid, color_value):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color_value)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find red and blue pixels
    red_pixels = find_pixels_by_color(input_grid, 2)
    blue_pixels = find_pixels_by_color(input_grid, 1)

    # Add yellow around red
    for r, c in red_pixels:
        # output_grid[r, c] = 2  # Keep original red (already done by copy)
        if r > 0:
            output_grid[r - 1, c] = 4  # Above
        if r < rows - 1:
            output_grid[r + 1, c] = 4  # Below
        if c > 0:
            output_grid[r, c - 1] = 4  # Left
        if c < cols - 1:
            output_grid[r, c + 1] = 4  # Right

    # Add orange around blue
    for r, c in blue_pixels:
        # output_grid[r, c] = 1  # Keep original blue (already done by copy)
        if r > 0:
            output_grid[r - 1, c] = 7  # Above
        if r < rows - 1:
            output_grid[r + 1, c] = 7  # Below
        if c > 0:
            output_grid[r, c - 1] = 7  # Left
        if c < cols - 1:
            output_grid[r, c + 1] = 7  # Right

    return output_grid
```

