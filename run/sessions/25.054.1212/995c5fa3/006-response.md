# 995c5fa3 • 006 • refine_coder

---
```python
"""
The input is a grid of pixels, primarily gray (5) with some white (0) pixels.
The output is a 3x3 grid. Each column in the output grid corresponds to a
column in the input grid (columns 0, 1, and 2 only). The color of each output
column is determined by the length of the *first* vertical "stripe" of white
pixels in the corresponding input column.

1.  **Iterate through Columns:** Examine each column of the input grid, from
    left to right (columns 0, 1, and 2 only).
2.  **Identify White Stripes:** Within each examined column, find vertical
    "stripes" of white (0) pixels. A stripe is one or more contiguous white
    pixels.
3.  **Measure Stripe Length:** If a white stripe is found in the current
    column, determine its length (the number of contiguous white pixels).
4.  **Map Length to Color:** Use the following mapping to determine the output
    color based on the stripe length:
    *   Length 1: Red (2)
    *   Length 2: Azure (8)
    *   Length 3: Green (3)
    *   Length 4: Yellow (4)
5.  **Fill Output Grid:** Create a 3x3 output grid.  For each column (0, 1,
    and 2) in the input grid, find the *first* white stripe and set the
    corresponding column of the *entire* output grid to the mapped color from
    step 4. If no stripe is in the examined input grid column, the
    corresponding output column defaults to black (0).
6. Skip any additional columns in the input grid.
"""

import numpy as np

def get_first_white_stripe_length(grid, col):
    # Find the length of the first vertical stripe of white pixels in a column
    height = grid.shape[0]
    stripe_length = 0
    for y in range(height):
        if grid[y, col] == 0:
            stripe_length += 1
        elif stripe_length > 0:
            return stripe_length
    return stripe_length

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid)

    # Map stripe lengths to colors
    color_map = {
        1: 2,
        2: 8,
        3: 3,
        4: 4
    }

    # Process the first three columns of the input grid
    for col in range(min(3, input_grid.shape[1])):
        # Find the length of the first white stripe in the column
        length = get_first_white_stripe_length(input_grid, col)

        # Map the length to a color, defaulting to 0 if no stripe or length not in map
        color = color_map.get(length, 0)

        # Fill the corresponding column in the output grid
        for row in range(3):
            output_grid[row, col] = color

    return output_grid
```
