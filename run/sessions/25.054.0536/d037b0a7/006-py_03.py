"""
1.  **Identify Seed Colors:** Examine the first row (the seed row) of the input grid. Identify *all* distinct non-zero colors present in this row. These are the "seed colors."

2.  **Iterate through Seed Colors:** For *each* seed color found in the seed row:

    a. **Identify Seed Columns:** Determine the column indices in the seed row where the current seed color appears.

    b. **Vertical Downward Expansion:** For *each* column index identified in the previous step:

        i. Start from the cell immediately below the seed row (row index 1).

        ii. Proceed downwards, cell by cell, in the current column.

        iii. If the current cell has a value of 0, replace it with the current seed color.

        iv. If the current cell has a non-zero value, stop the expansion for the current column and current seed color.
"""

import numpy as np

def get_seed_colors_and_columns(grid):
    """
    Identifies all seed colors and their corresponding column indices in the first row.
    """
    first_row = grid[0, :]
    seed_colors = np.unique(first_row[first_row != 0])  # Get unique non-zero colors
    seed_data = {}

    for color in seed_colors:
        seed_data[color] = np.where(first_row == color)[0]  # Store column indices for each color

    return seed_data

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Identify all seed colors and their columns
    seed_data = get_seed_colors_and_columns(output_grid)
    #print(f"Seed data: {seed_data}")

    # Iterate through seed colors and perform downward expansion
    for seed_color, seed_columns in seed_data.items():
        for col in seed_columns:
            for row in range(1, rows):  # Start from the second row
                if output_grid[row, col] == 0:
                    output_grid[row, col] = seed_color
                else:
                    break  # Stop at non-zero cell

    return output_grid