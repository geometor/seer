# 2-0ca9ddb6 • 024 • refine_coder

---
```python
"""
1.  **Identify Seed Pixels:** Locate all non-white (non-0) pixels in the input grid. These are the "seed" pixels.

2.  **Initial Expansion (Seed Pixel Rules):**
    *   If a seed pixel is Blue (1): Add Orange (7) pixels to its immediate left, right, and below positions, *but only if* those positions are currently White (0) in the *output* grid.
    *   If a seed pixel is Red (2): Add Yellow (4) pixels to its immediate top, left, and right positions, *but only if* those positions are currently White (0) in the *output* grid.
    *   If a seed pixel is Magenta (6) or Azure (8): Do nothing.

3.  **Iterative Expansion (Layer-by-Layer):**
    *   **Step 1:** Consider *only* the Orange (7) and Yellow (4) pixels added in the *Initial Expansion*.
        * If an added pixel is Orange (7): add an Orange(7) pixel to its immediate left, right and below, *but only if* those positions are currently White(0) in the output grid.
        * If an added pixel is Yellow(4): add an Yellow(4) pixel to its immediate top, left, and right, *but only if* those positions are currently white(0) in the output grid.
    *  **Step 2 and beyond:** Repeat Step 1, but for each iteration, *only* consider the colored pixels added in the *immediately preceding* step. Continue until no new pixels are added.

4.  **Expansion Constraints:**
    *   New pixels can only be added to positions that are currently White (0) in the output grid.
    *   Colors *never* expand onto other non-white colors, whether those colors are from the original input or added during expansion.

5. **Preservation:**
  * White (0) pixels not modified remain white(0).
"""

import numpy as np

def get_seed_pixels(grid):
    """Finds all non-zero pixels and returns their coordinates and values."""
    seed_pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                seed_pixels.append(((r, c), value))
    return seed_pixels

def expand_around_pixel(grid, row, col, color, directions):
    """Expands around a given pixel with the specified color in the given directions."""
    new_pixels = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == 0:
            grid[nr, nc] = color
            new_pixels.append(((nr, nc), color))
    return new_pixels


def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    seed_pixels = get_seed_pixels(input_grid)

    # Initial Expansion (Seed Pixel Rules)
    new_pixels = []
    for (row, col), value in seed_pixels:
        if value == 1:  # Blue
            new_pixels.extend(expand_around_pixel(output_grid, row, col, 7, [(0, -1), (0, 1), (1, 0)]))
        elif value == 2:  # Red
            new_pixels.extend(expand_around_pixel(output_grid, row, col, 4, [(-1, 0), (0, -1), (0, 1)]))
        # Magenta (6) and Azure (8) do nothing

    # Iterative Expansion (Layer-by-Layer)
    while new_pixels:
        next_new_pixels = []
        for (row, col), value in new_pixels:
            if value == 7:  # Orange
                next_new_pixels.extend(expand_around_pixel(output_grid, row, col, 7, [(0, -1), (0, 1), (1, 0)]))
            elif value == 4:  # Yellow
                next_new_pixels.extend(expand_around_pixel(output_grid, row, col, 4, [(-1, 0), (0, -1), (0, 1)]))
        new_pixels = next_new_pixels

    return output_grid
```
