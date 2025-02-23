# 0a938d79 • 022 • refine_coder

---
```python
"""
1.  **Identify Seed Rows:** Find all rows in the input grid that contain at least one non-white (non-zero) pixel. These are the "seed rows." Record the color and column index of the first non-white pixel in each seed row, maintaining the order.
2.  **Horizontal Striped Fill:** Create an output grid of the same dimensions as the input grid. Fill each row of the output grid with a single color, creating horizontal stripes.
3.  **Interleave Colors:** Starting from the top row of the output grid, assign colors to the rows based on the order of colors and column indices found in the seed rows. Cycle through the seed row colors repeatedly.  If the seed row colors are red and then blue, the output rows will be filled with red, blue, red, blue, etc.
4.  **Column-Based Placement:**  When filling a row with a given color, place the colored pixel in specific columns. The columns are determined by the column indices of the seed pixels *of that color* in the input grid.  Shift the columns cyclically for each subsequent row of the same color.
"""

import numpy as np

def get_seed_rows(grid):
    """Finds the row indices, colors, and column indices of the first non-white pixel in each row."""
    seed_rows = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel != 0:
                seed_rows.append((row_idx, pixel, col_idx))  # Store row index, color, and column index
                break  # Move to the next row once a colored pixel is found
    return seed_rows

def transform(input_grid):
    # Initialize output_grid with zeros
    output_grid = np.zeros_like(input_grid)

    # Find seed rows and their first non-zero colors and column indices
    seed_rows = get_seed_rows(input_grid)
    num_seed_rows = len(seed_rows)

    # Create a dictionary to store column shifts for each color
    color_shifts = {}
    for _, color, _ in seed_rows:
        color_shifts[color] = 0

    # Horizontal Striped Fill with Interleaved Colors and Column-Based Placement
    for row_idx in range(output_grid.shape[0]):
        # use mod operator to pick the appropriate seed row
        if (num_seed_rows > 0):
          seed_row_idx, color, col_idx = seed_rows[row_idx % num_seed_rows]

          # Get the shift value for the current color
          shift = color_shifts[color]

          # Calculate the shifted column index
          shifted_col_idx = (col_idx + shift) % output_grid.shape[1]

          # Place the colored pixel at the shifted column index
          output_grid[row_idx, shifted_col_idx] = color

          # Increment the shift for the current color, wrapping around
          color_shifts[color] = (shift + 1) % output_grid.shape[1]
    return output_grid
```
