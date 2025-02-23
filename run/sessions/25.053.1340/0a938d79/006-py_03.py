"""
Transforms an input grid based on the presence and arrangement of non-white "seed" pixels.

If seed pixels appear in different columns, the output grid is filled with alternating columns of the first two seed colors, starting from the leftmost seed pixel's column.

If seed pixels are only in the same column or stacked vertically within the same column, the output grid is created by copying rows containing seed pixels and all subsequent white rows downward until a non-white pixel is encountered or the end of the grid.
"""

import numpy as np

def find_seed_pixels(grid):
    """Finds non-white pixels in the grid and returns their coordinates and color."""
    seeds = []
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel != 0:
                seeds.append((r, c, pixel))
    return seeds

def transform(input_grid):
    """Transforms the input grid according to the rules described above."""
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find seed pixels.
    seed_pixels = find_seed_pixels(input_grid)

    if not seed_pixels:  # Handle empty input.
        return output_grid.tolist()

    # Determine transformation type based on column arrangement.
    first_seed_col = min(pixel[1] for pixel in seed_pixels)
    different_columns = any(pixel[1] != first_seed_col for pixel in seed_pixels)

    if different_columns:
        # Alternating Column Fill.
        colors = [pixel[2] for pixel in sorted(seed_pixels, key=lambda p: p[1])][:2]  # Get colors of the leftmost two.

        color_index = 0
        for c in range(first_seed_col, cols):
            for r in range(rows):
                output_grid[r, c] = colors[color_index % 2]
            color_index += 1

    else:
        # Row Copy and following white rows.
        seed_rows = sorted(list(set([pixel[0] for pixel in seed_pixels])))

        row_idx = 0
        while row_idx < rows:
          if row_idx in seed_rows:
            # copy the row
            seed_row = row_idx
            for c in range(cols):
              output_grid[row_idx,c] = input_grid[seed_row,c]

            # copy downward
            row_idx += 1
            while row_idx < rows:
              if any(input_grid[row_idx,c] != 0 for c in range(cols)):
                break # encountered new seed pixel row, stop copying
              
              for c in range(cols):
                output_grid[row_idx,c] = input_grid[seed_row,c]
              row_idx+=1
          else:
             # copy other rows
            for c in range(cols):
                output_grid[row_idx,c] = input_grid[row_idx,c]
            row_idx+=1

    return output_grid.tolist()