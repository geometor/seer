"""
Transforms an input grid based on the presence and arrangement of non-white "seed" pixels.

1. Find Seed Pixels: Identify all non-white pixels (pixels with values other than 0) in the input grid. These are the "seed pixels."

2. Determine Layout and Transformation Type:
   - If all seed pixels are in the same column, the layout is considered "vertical," and the transformation is "row copy and following white rows."
   - If seed pixels appear in different columns, the layout is considered "horizontal," and the transformation is "alternating columns."

3. Horizontal Layout - Alternating Columns:
   - Identify the two leftmost seed pixels.
   - Starting from the column of the *leftmost* seed pixel, fill the entire grid to the *right*, alternating the colors of the two identified seed pixels column by column.

4. Vertical Layout - Row Copy and Following White Rows:
    - Sort the seed pixels by their row index.
    - For each seed pixel row (from top to bottom, from the first seed pixel down):
        - Copy the entire seed pixel row to the output grid.
        - Continue copying the content of the original seed row to subsequent rows in the output grid.
        - Stop copying when you encounter a row in the *input* grid that contains any non-white pixel.
        - Continue with next seed row.
    - Copy all other rows to the output grid, matching input.
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
             # copy the seed row
            seed_row = row_idx
            for c in range(cols):
              output_grid[row_idx,c] = input_grid[seed_row,c]

            # Copy downward until a non-white row is encountered in input_grid.
            row_idx += 1
            while row_idx < rows and all(input_grid[row_idx, c] == 0 for c in range(cols)):
                for c in range(cols):
                    output_grid[row_idx, c] = input_grid[seed_row,c]
                row_idx += 1

          else:
            # copy other rows
            for c in range(cols):
                output_grid[row_idx,c] = input_grid[row_idx,c]
            row_idx+=1          

    return output_grid.tolist()