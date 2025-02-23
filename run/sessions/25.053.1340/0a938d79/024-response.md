# 0a938d79 • 024 • refine_coder

---
```python
"""
Identifies rows with colored pixels in the input grid. Extends those colored pixels horizontally across their respective rows, handling single and multiple colors. The output grid alternates these extended color rows with blank (all-zero) rows, repeating this pattern until the output grid is filled.
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
    # Extend colors horizontally, handling single and multiple colors.
    rows, cols = grid.shape
    extended_row = np.zeros(cols, dtype=int)
    non_zero_pixels = grid[row_index][grid[row_index] != 0]
    unique_colors = np.unique(non_zero_pixels)

    if len(unique_colors) == 1:
        # If only one color, fill the entire row.
        extended_row[:] = unique_colors[0]
    else:
        # If multiple colors, create a repeating sequence.
        for j in range(cols):
            extended_row[j] = unique_colors[j % len(unique_colors)]
    return extended_row

def transform(input_grid):
    # Initialize output_grid as all zeros with the same dimensions as input.
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Identify rows with colored pixels.
    colored_rows_indices = get_colored_rows(input_grid)

    # Create the repeating output pattern.
    output_row_index = 0
    colored_row_index = 0
    
    while output_row_index < rows:
        if colored_row_index < len(colored_rows_indices):
           # Extend the colored row.
            extended_row = extend_colors_horizontally(input_grid, colored_rows_indices[colored_row_index])
            output_grid[output_row_index, :] = extended_row
            output_row_index += 1

            # Add a blank row if there is space.
            if output_row_index < rows:
                output_row_index += 1 # Already initialized to zeros
        else:
            # Reset to repeat the pattern.
            colored_row_index = 0
            continue # Check if output_row_index is still valid.

        colored_row_index += 1

    return output_grid
```
