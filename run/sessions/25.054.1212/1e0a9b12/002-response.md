# 1e0a9b12 • 002 • example_1 • investigate_coder

---
```python
"""
1. Identify non-zero pixels: Find all pixels in the input grid with values other than 0.
2. Preserve Order: Maintain the original order of these non-zero pixels as they appear from left-to-right, top-to-bottom in the input.
3. Move to Bottom: Move the identified non-zero pixels to the bottom-most available rows of the output grid. Fill the rows from left to right.
4. Fill Remaining: All other cells in output grid, not occupied are filled with 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero pixels to the bottom,
    preserving their original order, and filling the remaining cells with zeros.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)
    non_zero_pixels = []

    # 1. Identify and store non-zero pixels with their original positions.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_pixels.append((input_grid[r, c], r, c))

    # 2. (Order is implicitly preserved as we iterate row-by-row, then column by column)

    # 3. Move to the bottom.
    num_non_zero = len(non_zero_pixels)
    output_row = rows - 1
    output_col = 0
    for pixel_value, _, _ in non_zero_pixels:
        output_grid[output_row, output_col] = pixel_value
        output_col += 1
        if output_col == cols:
            output_col = 0
            output_row -= 1
            if output_row < 0:  # added to prevent going beyond boundary if there are many non-zero pixels
                break

    # 4. Fill the remaining (already done by initializing output_grid with zeros).
    return output_grid
```
