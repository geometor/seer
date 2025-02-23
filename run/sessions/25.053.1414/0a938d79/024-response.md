# 0a938d79 • 024 • refine_coder

---
```python
"""
1.  **Iterate** through each row of the input grid.
2.  **Check** if the current row contains any non-zero pixels.
3.  **If the row is all zeros:** Copy the all-zero row directly to the corresponding row in the output grid.
4.  **If the row has non-zero pixels:**
    *   Find the first non-zero pixel value (color) in that row.
    *   Fill the *entire* corresponding output row with this color.
5.  **Repeat**: After processing each input row and creating a corresponding output row, inspect the input grid for rows below the just processed row, and if the color of this lower row is the same as the just processed row in the input, replicate the output row. Continue until a row of a different color (including 0) is found, then proceed.
"""

import numpy as np

def get_first_non_zero(row):
    """Finds the first non-zero element in a row."""
    for pixel in row:
        if pixel != 0:
            return pixel
    return 0

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    height, width = input_grid.shape
    row_index = 0

    while row_index < height:
        row = input_grid[row_index]
        first_non_zero = get_first_non_zero(row)

        if first_non_zero == 0:
            # Copy the all-zero row
            output_grid[row_index] = row
            row_index += 1
        else:
            # Fill the output row with the first non-zero color
            output_grid[row_index] = np.full(width, first_non_zero)

            # Check for row repetition
            next_row_index = row_index + 1
            while next_row_index < height and get_first_non_zero(input_grid[next_row_index]) == first_non_zero:
                output_grid[next_row_index] = np.full(width, first_non_zero)
                next_row_index += 1

            row_index = next_row_index

    return output_grid
```
