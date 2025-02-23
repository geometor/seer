# 1e32b0e9 • 010 • refine_coder

---
```python
"""
1. **Identify Barrier Rows:** Find the two horizontal lines that span the entire width of the grid. These rows remain unchanged.
    *    Note the color of these rows, as they are different in each example.
2. **Locate Influencing Pixels:** Identify all pixels that *are not* part of the barrier rows.
3. **Apply Influence:** For *each* influencing pixel:
    *   Find all directly adjacent pixels (up, down, left, right - not diagonal).
    *   If an adjacent pixel is *not* on a barrier row, change its color to the color of the *original* influencing pixel.
4. **Barrier Rows Unchanged:** The pixels in the barrier rows do not change.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets directly adjacent pixels (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent.append((row + 1, col))  # Down
    if col > 0:
        adjacent.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent.append((row, col + 1))  # Right
    return adjacent

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    
    # Identify barrier rows (rows 6 and 12, but 0-indexed as 5 and 11)
    barrier_rows = [5, 11]

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is an influencing pixel (not on a barrier row)
            if r not in barrier_rows:
                influencing_pixel_color = input_grid[r, c]
                # Get adjacent pixels
                adjacent_pixels = get_adjacent_pixels(input_grid, r, c)
                # Apply influence to adjacent pixels
                for ar, ac in adjacent_pixels:
                    if ar not in barrier_rows:
                        output_grid[ar, ac] = influencing_pixel_color

    return output_grid
```

