# 0a938d79 • 020 • refine_coder

---
```python
"""
Identifies rows with colored pixels in the input grid. Extends those colored pixels horizontally across their respective rows. In the output, alternates these extended color rows with blank (all-zero) rows.
"""

import numpy as np

def get_colored_rows(grid):
    # Find rows that have at least one non-zero pixel.
    colored_rows = []
    for i, row in enumerate(grid):
        if np.any(row != 0):
            colored_rows.append(i)
    return colored_rows

def extend_colors_horizontally(grid, row_index):
    # Extend colors horizontally in an alternating manner if different ones appear on the same row.
    rows, cols = grid.shape
    extended_row = np.zeros(cols, dtype=int)
    non_zero_pixels = grid[row_index][grid[row_index] != 0]

    for j in range(cols):
      extended_row[j] = non_zero_pixels[j%len(non_zero_pixels)]

    return extended_row

def transform(input_grid):
    # Initialize output_grid as all zeros with the same dimensions as the input.
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Identify rows with colored pixels.
    colored_rows_indices = get_colored_rows(input_grid)

    # Create alternating pattern.
    output_row_index = 0
    for i in range(len(colored_rows_indices)):
        # Extend colored row.
        if output_row_index < rows:
            output_grid[output_row_index, :] = extend_colors_horizontally(input_grid, colored_rows_indices[i])
            output_row_index += 1

        # Add a blank row.
        if output_row_index < rows:
            output_row_index += 1 # Already initialized to zeros.

    return output_grid
```
