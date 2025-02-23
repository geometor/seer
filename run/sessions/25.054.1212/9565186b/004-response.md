# 9565186b • 004 • refine_coder

---
```python
"""
1.  **Identify Azure and Blue Pixels:** Locate all pixels in the input grid that are colored azure (8) or blue (1).
2.  **Determine the Minimal Bounding Box:** Find the smallest rectangle that completely encloses all the azure and blue pixels found in step 1.
3.  **Fill with Gray:** Change the color of all pixels within the bounding box (including the edges) determined in step 2 to gray (5).
4. **Other pixels:** All other pixels retain their original colors.
"""

import numpy as np

def find_bounding_box(grid, colors):
    """Finds the minimal bounding box containing specified colors."""
    rows, cols = grid.shape
    min_row, min_col = rows, cols
    max_row, max_col = -1, -1

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] in colors:
                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r)
                max_col = max(max_col, c)

    if max_row == -1: # No matching colors found
        return None

    return min_row, min_col, max_row, max_col

def transform(input_grid):
    """Transforms the input grid by filling the bounding box of blue/azure pixels with gray."""

    # Initialize output_grid as a copy of the input.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find the bounding box coordinates for blue (1) and azure (8) pixels.
    bounding_box = find_bounding_box(input_grid, [1, 8])

    # If no blue or azure pixels are found, return the original grid.
    if bounding_box is None:
        return output_grid

    min_row, min_col, max_row, max_col = bounding_box

    # Fill the bounding box with gray (5).
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            output_grid[r, c] = 5

    return output_grid
```
