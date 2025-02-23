# 00d62c1b • 016 • refine_coder

---
```python
"""
1.  **Identify the Green Shape:** Locate all green (3) pixels in the input grid.  Combine these into a single green shape, regardless of whether they are initially contiguous.

2.  **Identify the True Perimeter:** Iterate through all pixels *within the green shape*. A pixel is part of the perimeter if it meets *either* of these conditions:
    *   It is on the edge of the entire grid (top row, bottom row, leftmost column, or rightmost column).
    *   It has at least one direct neighbor (up, down, left, or right – *not* diagonal) that is *not* part of the *green shape*.

3.  **Identify Interior Pixels:** Iterate through all pixels of the *green shape*. A pixel is considered "interior" if and *only if* all four of its direct neighbors (up, down, left, and right) are *also* part of the *green shape*.

4.  **Modify Interior Pixels:** Change the color of all identified interior pixels to yellow (4).

5. **Preserve Other Pixels:** Ensure all other pixels (those not part of the original green shape) in the grid retain their original colors. The output grid must be the same size as the input grid.
"""

import numpy as np

def find_green_shape(grid):
    """
    Finds all green pixels and returns their coordinates as a set.
    """
    green_shape = set()
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 3:
                green_shape.add((r, c))
    return green_shape

def find_true_perimeter(green_shape, rows, cols):
    """
    Finds the true perimeter pixels of the green shape.
    """
    perimeter = set()
    for r, c in green_shape:
        # Check if it's on the edge of the grid
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            perimeter.add((r, c))
            continue

        # Check direct neighbors (up, down, left, right)
        is_perimeter = False
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in green_shape:
                is_perimeter = True
                break
        if is_perimeter:
            perimeter.add((r, c))
    return perimeter

def find_interior_pixels(green_shape, rows, cols):
    """
    Finds the interior pixels of the green shape.
    """
    interior = set()
    for r, c in green_shape:
        # Check all four direct neighbors
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        is_interior = True
        for nr, nc in neighbors:
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in green_shape:
                is_interior = False
                break
        if is_interior:
            interior.add((r, c))
    return interior


def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the Green Shape (all green pixels)
    green_shape = find_green_shape(input_grid)

    # Find the true perimeter of combined shape
    # perimeter = find_true_perimeter(green_shape, rows, cols) # Removed, not directly used

    # Identify Interior Pixels
    interior_pixels = find_interior_pixels(green_shape, rows, cols)

    # Modify Interior Pixels
    for r, c in interior_pixels:
        output_grid[r, c] = 4

    return output_grid
```

