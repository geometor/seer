"""
1.  **Identify Seed Rows:** Find all rows in the input grid that contain at least one non-white pixel. These are the "seed rows."
2. **Sort Seed Rows**: Order all seed rows in a new list, ordered by their
    index.
3.  **Iterate Through Seed Rows (Top to Bottom):** For each seed row:
    *   Find all non-white pixels within that row.
    *   For each non-white pixel find the color
    *   Fill the entire current seed row with that color.
    * Starting from two rows below the current seed row (`start_row + 2`), fill every other row with that same color until the bottom of the grid is reached.
"""

import numpy as np

def get_seed_rows(grid):
    """Identifies rows with at least one non-white pixel and extracts seed pixel information."""
    seed_rows = []
    for row_index, row in enumerate(grid):
        non_white_pixels = []
        for col_index, pixel_value in enumerate(row):
            if pixel_value != 0:
                non_white_pixels.append({"col": col_index, "color": pixel_value})
        if non_white_pixels:
            seed_rows.append({"row_index": row_index, "seed_pixels": non_white_pixels})
    return seed_rows

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows = len(output_grid)
    cols = len(output_grid[0])

    # Find and sort seed rows.
    seed_rows = get_seed_rows(input_grid)

    # Iterate through seed rows.
    for seed_row in seed_rows:
        row_index = seed_row["row_index"]
        # Iterate over the seed_pixels in order
        for pixel_info in seed_row["seed_pixels"]:
            color = pixel_info["color"]

            # Fill the entire seed row.
            output_grid[row_index, :] = color

            # Fill alternating rows below.
            for r in range(row_index + 2, rows, 2):
                output_grid[r, :] = color

    return output_grid