# 7837ac64 • 012 • refine_coder

---
```python
"""
1.  **Identify Vertical Stripes:** Find the repeating vertical stripes of color alternating with white (0) columns.
2.  **Divide Rows:** Divide the input grid rows into three equal-sized regions (top, middle, bottom). For non-divisible row counts, the extra row(s) are not considered.
3.  **Extract Deviating Colors:** Within each region, examine the rows that belong to the vertical stripe pattern. Identify any "deviating" pixels - those that *do not* match the dominant color of the vertical stripe in that region.
4.  **Populate Output Grid:**
    *   For the *top* region, if deviating colors were found, fill the *first* row of the output grid as follows: the first deviating color goes in the first column, if a second color exists in the region, place 0 in the second column, and the the second color in the third column. If only one color exists, insert 0 in the second and third columns. If no deviating colors, fill with 0.
    *   For the *middle* region, if deviating colors were found, fill the *second* row of the output grid: place the first color found in the first column. If a second color exists, use 0 for the remaining columns.
    *  For the *bottom* region, if deviating colors are found fill the *third* row with the first deviating color.
5. **Handle edge cases**: If there are fewer than three rows per section, use a blank (all 0) row.
"""

import numpy as np
from collections import Counter

def find_vertical_stripe_color(grid):
    """Finds the dominant color in the repeating vertical stripes."""
    # Check the first few columns to identify the pattern
    color_counts = Counter()
    for r in range(grid.shape[0]):
        for c in range(0, min(3, grid.shape[1]), 2):  # Check every other column, up to the first 3.
            if grid[r, c] != 0:
                color_counts[grid[r, c]] += 1
    if color_counts:
        return color_counts.most_common(1)[0][0]  # most frequent non-zero color
    return 0  # If no non-zero colors found, return 0


def get_deviating_colors(grid, stripe_color):
    """
    Extracts deviating colors from rows within the stripe pattern, grouped by region.
    Assumes stripes alternate with white (color 0)
    """
    rows, cols = grid.shape
    region_size = rows // 3
    deviating_colors = {0: [], 1: [], 2: []}

    for region in range(3):
        start_row = region * region_size
        end_row = start_row + region_size
        # limit end row for cases where rows are not multiple of 3
        end_row = min(end_row, grid.shape[0])

        for r in range(start_row, end_row):
            # check for consistent stripe structure
            if all(grid[r,c] == stripe_color for c in range(0, grid.shape[1], 2)):
               for c in range(0, grid.shape[1]):
                   if grid[r,c] != stripe_color and grid[r,c] != 0:
                       # found deviating
                       if grid[r,c] not in deviating_colors[region]:
                          deviating_colors[region].append(grid[r,c])


    return deviating_colors


def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Identify the dominant vertical stripe color
    stripe_color = find_vertical_stripe_color(input_grid)

    # Get deviating colors, grouped by region (top, middle, bottom)
    deviating_colors = get_deviating_colors(input_grid, stripe_color)

    # Populate the output grid based on the deviating colors
    for region in range(3):
        colors = deviating_colors[region]
        if colors:
            if region == 0:
                output_grid[region, 0] = colors[0]
                if len(colors) > 1:
                   output_grid[region,1] = 0
                   output_grid[region,2] = colors[1]
            if region == 1:
                output_grid[region, 0] = colors[0]
            if region == 2:
               output_grid[region,:] = colors[0]

    return output_grid
```
