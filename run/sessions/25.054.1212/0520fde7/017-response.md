# 0520fde7 • 017 • refine_coder

---
```python
"""
1.  **Identify the Gray Stripe:** Find the vertical gray stripe (all pixels in a column have a value of 5).
2.  **Check for Adjacent Blues:** For each *row* in the *output* grid (going from 0 to 2), determine if there's *at least one* row in the input grid where a blue pixel (value 1) is directly to the left *or* right of the gray stripe.
3.  **Place Red Pixel:** If, for a given output row, the condition in step 2 is true, place a red pixel (value 2) in the corresponding row of the output grid. The red pixel will be placed in the middle column (column index 1).
4. All other output pixels are 0.
"""

import numpy as np

def find_gray_stripe(grid):
    """Finds the column index of the vertical gray stripe."""
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == 5 for i in range(rows)):
            return j
    return -1  # Should not happen in valid cases, based on problem definition


def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)
    gray_stripe_col = find_gray_stripe(input_grid)

    # Check for adjacent blues for each output row
    for output_row in range(3):
        has_adjacent_blue = False
        for input_row in range(input_grid.shape[0]):
            if (0 <= gray_stripe_col - 1 < input_grid.shape[1] and
                input_grid[input_row, gray_stripe_col - 1] == 1) or \
               (0 <= gray_stripe_col + 1 < input_grid.shape[1] and
                input_grid[input_row, gray_stripe_col + 1] == 1):
                has_adjacent_blue = True
                break  # Found a blue pixel, no need to check other input rows

        # Place red pixel if adjacent blue was found
        if has_adjacent_blue:
            output_grid[output_row, 1] = 2

    return output_grid
```
