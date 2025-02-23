# 0520fde7 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify the vertical gray stripe:** Find the complete vertical stripe in the input grid which contains only the color gray (value 5).
2. **Identify horizontal runs of blue adjacent to gray:** Find locations to either the left, or the right of this stripe where there are 1 or more blue pixels. Consider only the rows which have the vertical gray stripe.
3.  **Create the output grid:** Create an output grid with dimensions of 3x3, and fill it all with white (0) pixels.
4.  **Transform Blue Runs to Red:** For each segment, or a group of blue pixels, transform one white pixel in the output to red (value 2), at the equivalent row index. In case of multiple blue pixel segments on different sides of gray, consider each segment separately, putting a red pixel on the left column if blue is to the left of the gray segment, and a red pixel on the right if blue is to the right of the gray column.
"""

import numpy as np

def find_vertical_stripe(grid, color):
    # Find the complete vertical stripe of a specific color.
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)
    rows, cols = input_grid.shape

    # Find the vertical gray stripe (color 5).
    gray_stripe_col = find_vertical_stripe(input_grid, 5)

    if gray_stripe_col == -1:
        return output_grid  # No gray stripe found.

    # Identify horizontal runs of blue (color 1) adjacent to the gray stripe.
    for i in range(rows):
        if gray_stripe_col > 0 and input_grid[i, gray_stripe_col - 1] == 1:
           output_grid[i,0] = 2
        if gray_stripe_col < cols - 1 and input_grid[i, gray_stripe_col + 1] == 1:
           output_grid[i,2] = 2
    
    return output_grid
```
