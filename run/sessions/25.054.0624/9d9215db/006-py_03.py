"""
1. Identify the Seed Pattern: Find the bounding box enclosing all non-white pixels in the input grid. This rectangular region defines the "seed pattern."
2. Replicate the Seed: Tile the output grid with the seed pattern. Replicate the seed pattern horizontally and vertically to completely fill output grid, starting from the top-left corner.
"""

import numpy as np

def get_seed_pattern(grid):
    """
    Finds the bounding box of non-white pixels and extracts the seed pattern.
    """
    non_white_pixels = []
    rows = []
    cols = []
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val != 0:
                non_white_pixels.append(((r_idx, c_idx), val))
                rows.append(r_idx)
                cols.append(c_idx)

    if not non_white_pixels:
        return np.array([]), 0, 0

    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    seed_pattern = [row[min_col:max_col+1] for row in grid[min_row:max_row+1]]
    return np.array(seed_pattern), min_row, min_col

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Identify seed pattern.
    seed_pattern, seed_row_start, seed_col_start = get_seed_pattern(input_grid)

    if seed_pattern.size == 0:  # Handle the edge case of an all-white input.
      return output_grid.tolist()
    
    seed_height, seed_width = seed_pattern.shape

    # Replicate the seed pattern across the output grid.
    for r_out in range(output_grid.shape[0]):
        for c_out in range(output_grid.shape[1]):
            seed_r = (r_out ) % seed_height
            seed_c = (c_out ) % seed_width
            output_grid[r_out, c_out] = seed_pattern[seed_r, seed_c]

    return output_grid.tolist()