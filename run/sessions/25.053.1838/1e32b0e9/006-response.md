# 1e32b0e9 • 006 • refine_coder

---
```python
"""
1.  **Identify Initial Colored Objects:** Find all contiguous regions (objects) of non-white (non-0) colors in the input grid.

2.  **Simultaneous Expansion:**
    *   Iterate through each pixel of the grid.
    *   For each non-white pixel, check its immediate neighbors (up, down, left, right).
    *   If a neighbor is white, mark it for potential expansion with the current pixel's color.
    *   *Crucially*, if multiple colors are trying to expand into the same white pixel, *none* of them expand into that pixel (this is the boundary condition). This prevents overwriting.

3. **Apply Expansion:** After checking all pixels in a single iteration, update the grid with the marked expansions.

4.  **Repeat:** Repeat steps 2 and 3 until no further changes occur to the grid.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Returns a dictionary of non-white pixel coordinates and their colors."""
    rows, cols = grid.shape
    non_white_pixels = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                non_white_pixels[(r, c)] = grid[r, c]
    return non_white_pixels

def expand_colors_simultaneously(grid, non_white_pixels):
    """Expands all non-white colors simultaneously, handling boundary conditions."""
    new_grid = grid.copy()
    rows, cols = grid.shape
    expansion_map = {}  # Track potential expansions: {(r, c): [color1, color2, ...]}
    changed = False

    for (r, c), color in non_white_pixels.items():
        # Check adjacent cells
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
                if (nr, nc) not in expansion_map:
                    expansion_map[(nr, nc)] = []
                expansion_map[(nr, nc)].append(color)

    # Apply expansions, handling conflicts
    for (nr, nc), colors in expansion_map.items():
        if len(colors) == 1:  # Only expand if there's no conflict
            new_grid[nr, nc] = colors[0]
            changed = True

    return new_grid, changed

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Iteratively expand colors until no change
    changed = True
    while changed:
        # Identify non-white pixels
        non_white_pixels = get_non_white_pixels(output_grid)

        # expand
        output_grid, changed = expand_colors_simultaneously(output_grid, non_white_pixels)

    return output_grid
```
