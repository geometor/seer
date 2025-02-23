# 0a938d79 • 022 • refine_coder

---
```python
"""
Identifies rows with colored pixels in the input grid. Extends those colored pixels in an alternating pattern horizontally across their respective rows.  The output grid alternates these extended color rows with blank (all-zero) rows, and then repeats this pattern.
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
    # Extend colors horizontally in an alternating manner.
    rows, cols = grid.shape
    extended_row = np.zeros(cols, dtype=int)
    non_zero_pixels = grid[row_index][grid[row_index] != 0]

    if len(non_zero_pixels) > 0:  # Handle cases where a row might be all zeros
       for j in range(cols):
          extended_row[j] = non_zero_pixels[j % len(non_zero_pixels)]

    return extended_row

def transform(input_grid):
    # Initialize output_grid as all zeros with the same dimensions as the input.
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Identify rows with colored pixels.
    colored_rows_indices = get_colored_rows(input_grid)

    # Create output, handling potential out-of-bounds.
    output_row_index = 0
    colored_row_index = 0
    
    while output_row_index < rows:
        if colored_row_index < len(colored_rows_indices):
            # Extend colored row.
            extended_row = extend_colors_horizontally(input_grid, colored_rows_indices[colored_row_index])
            output_grid[output_row_index, :] = extended_row
            output_row_index += 1

            # Add a blank row if there's space
            if output_row_index < rows:
                output_row_index += 1  # Already initialized to zeros.
                
        else:
            # reset the index, to repeat the pattern.
            colored_row_index = 0
            continue #restart the while, to check if output_row_index is still valid

        colored_row_index += 1


    return output_grid
```
