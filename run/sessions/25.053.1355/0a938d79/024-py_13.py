"""
1.  **Identify Seed Rows:** Examine each row of the input grid. A row is a "seed row" if it contains at least one non-white (non-zero) pixel.
2.  **Record Seed Row Information:** For each seed row, store:
    *   The color of the first non-white pixel.
    *   The column index of that first non-white pixel.
    *   The seed rows should be recorded in the order in which they appear in the input.
3. **Initialize output:** create an output grid of matching size, filled with white.
4.  **Create Horizontal Stripes:** Iterate through the rows of the *output* grid. For each row:
    *   Determine the color to use by cycling through the colors of the seed rows, in order.  (e.g., If the seed row colors are red, blue, green, the output rows will be filled red, blue, green, red, blue, green, etc.)
    *   Fill the *entire* output row with the selected color.
5. **Output complete:** the output is a grid, with each row completely filled with the color of the seed row.
"""

import numpy as np

def get_seed_rows(grid):
    """Finds the row indices and colors of the first non-white pixel in each row."""
    seed_rows = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel != 0:
                seed_rows.append((row_idx, pixel, col_idx))  # Store row index, color and col index
                break  # Move to the next row once a colored pixel is found
    return seed_rows

def transform(input_grid):
    # initialize output_grid with all white (0)
    output_grid = np.zeros_like(input_grid)

    # Find seed rows, their first non-zero color and column index
    seed_rows = get_seed_rows(input_grid)
    num_seed_rows = len(seed_rows)

    # Horizontal Striped Fill - Interleave colors
    for row_idx in range(output_grid.shape[0]):
        # use mod operator to pick the appropriate seed row, but only need color
        if (num_seed_rows > 0):
          seed_row_idx, color, _ = seed_rows[row_idx % num_seed_rows]

          # fill the entire row with color
          output_grid[row_idx, :] = color

    return output_grid