# 2-0ca9ddb6 • 016 • refine_coder

---
```python
"""
1.  **Grid and Pixels:** The input and output are grids of pixels, where each
    pixel has a color represented by a number (0-9).
2.  **Key Pixels:** Identify all non-white (i.e., colored) pixels in the
    *input* grid. These are the "key" pixels.
3.  **Azure (8) Rule:**
    *   For each key pixel that is azure (color 8), examine its *adjacent*
        neighbors. Adjacent means directly above, below, left, or right (not
        diagonal).
    *   If an adjacent neighbor is white (color 0), change its color to orange
        (color 7).
4.  **Red (2) and Blue (1) Rule:**
    *   For each key pixel that is red (color 2) or blue (color 1), examine
        pixels that are exactly at an L1 distance of 2.  This means two steps
        away, counting only horizontal and vertical steps, not diagonal.
    *   If a pixel at L1 distance of 2 is white (color 0), change its color to
        yellow (color 4).
5.  **Magenta (6) Exception:** Key pixels that are magenta (color 6) do *not*
    cause any color changes in other pixels.
6.  **Application of Changes:** The key idea is to apply color based on the
    *input* grid's state, updating the *output* grid.
"""

import numpy as np

def get_neighbors(grid, row, col, distance=1):
    """Gets the neighbors of a cell within a specified L1 distance."""
    neighbors = []
    rows, cols = grid.shape
    for i in range(max(0, row - distance), min(rows, row + distance + 1)):
        for j in range(max(0, col - distance), min(cols, col + distance + 1)):
            if (abs(row - i) + abs(col - j)) == distance and (row, col) != (i,j):
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify Key Pixels and Target Pixels, and store changes
    changes = []  # List to store (row, col, new_color) tuples
    key_pixels = []
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != 0:
                key_pixels.append((i, j, input_grid[i, j]))

    # Determine Changes
    for r, c, color in key_pixels:
        # Azure (8) Rule
        if color == 8:
             neighbors = get_neighbors(input_grid, r, c, distance=1) # adjacent
             for nr, nc in neighbors:
                if input_grid[nr, nc] == 0:  # Check if white
                    changes.append((nr, nc, 7))   # Change to orange

        # Red (2) and Blue (1) Rule
        elif color == 1 or color == 2:
            neighbors = get_neighbors(input_grid, r, c, distance=2) # L1=2
            for nr, nc in neighbors:
                if input_grid[nr, nc] == 0:   # Check if white
                    changes.append((nr, nc, 4))    # Change to Yellow

        # Magenta (6) behavior - no change
        elif color == 6:
            pass  # Do nothing.

    # Apply changes
    for r, c, new_color in changes:
        output_grid[r, c] = new_color

    return output_grid
```
