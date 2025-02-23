# 2-0ca9ddb6 • 008 • refine_coder

---
```python
"""
1.  **Initialize:** Create an output grid of the same dimensions as the input grid, filled with zeros (white).

2.  **Red Pixel Expansion:** For each red (2) pixel in the input grid:
    *   Copy the red pixel to the same position in the output grid.
    *   If a position directly above the red pixel is within the grid bounds, place a yellow (4) pixel there.
    *   If a position directly below the red pixel is within the grid bounds, place a yellow (4) pixel there.

3.  **Blue Pixel Expansion:** For each blue (1) pixel in the input grid:
    *   Copy the blue pixel to the same position in the output grid.
    *   If a position directly above the blue pixel is within the grid bounds, place an orange (7) pixel there.
    *   If a position directly below the blue pixel is within the grid bounds, place an orange (7) pixel there.
    *   If a position directly to the left of the blue pixel is within the grid bounds, place an orange (7) pixel there.
    *   If a position directly to the right of the blue pixel is within the grid bounds, place an orange (7) pixel there.

4. **Ignore Other Colors:** Pixels of any color other than red or blue in the input grid do not directly cause any changes in the output grid (although they can be overwritten by red/blue expansions).
"""

import numpy as np

def get_colored_pixels(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == color:
                pixels.append((r, c))
    return pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Red Pixel Expansion
    red_pixels = get_colored_pixels(input_grid, 2)
    for r, c in red_pixels:
      output_grid[r,c] = 2 # transfer original
      if r > 0:
          output_grid[r - 1, c] = 4  # Above
      if r < output_grid.shape[0] - 1:
          output_grid[r + 1, c] = 4  # Below

    # Blue Pixel Expansion
    blue_pixels = get_colored_pixels(input_grid, 1)
    for r, c in blue_pixels:
        output_grid[r,c] = 1 # transfer original
        if r > 0:
            output_grid[r - 1, c] = 7  # Above
        if r < output_grid.shape[0] - 1:
            output_grid[r + 1, c] = 7  # Below
        if c > 0:
            output_grid[r, c - 1] = 7  # Left
        if c < output_grid.shape[1] - 1:
            output_grid[r, c + 1] = 7  # Right

    return output_grid
```
