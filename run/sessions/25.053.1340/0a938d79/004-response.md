# 0a938d79 • 004 • refine_coder

---
```python
"""
Transforms an input grid based on the presence and arrangement of non-white "seed" pixels. If seed pixels appear in different columns, the output grid is filled with alternating columns of the first two seed colors. If seed pixels are only in the same column or stacked in multiple rows, the output grid is created by copying rows containing seed pixels.
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

    # Determine transformation type.
    first_seed_col = seed_pixels[0][1]
    different_columns = any(pixel[1] != first_seed_col for pixel in seed_pixels)

    if different_columns:
        # Alternating Column Fill.
        colors = [seed_pixels[0][2], seed_pixels[1][2]]
        if len(colors) < 2:
            if colors[0] == 2:
              colors.append(8)
            else:
              colors.append(2)
          
        start_col = first_seed_col
        color_index = 0
        for c in range(start_col, cols):
            for r in range(rows):
                output_grid[r, c] = colors[color_index % 2]
            color_index += 1

    else:
        # Row Copy.
        last_seed_row = None
        for r in range(rows):
            row_has_seed = any(pixel[0] == r for pixel in seed_pixels)
            if row_has_seed:
                for c in range(cols):
                    output_grid[r, c] = input_grid[r, c]
                last_seed_row = r
            elif last_seed_row is not None:
                for c in range(cols):
                    output_grid[r,c] = output_grid[last_seed_row,c]
                

    return output_grid.tolist()
```
