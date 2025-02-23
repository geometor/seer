"""
1.  **Identify Solid Rows:** Find all rows that consist of a single, uniform color across their entire width.
2.  **Preserve Solid Rows:** All pixels belonging to these solid rows are kept unchanged in the output.
3.  **Conditional Pixel Preservation:** For all other rows (non-solid rows):
    *   A pixel is *kept* if and only if there exists a solid row *anywhere* in the grid that has the *same color* AND the *same column index* as the pixel in question.
    *   A pixel directly below a solid line of the same color will extend that solid line color down.
4. **Remove other Pixels:** Any pixel not meeting the conditions in steps 2 or 3 is removed (set to 0). This means the output grid will only contain pixels that were either part of a solid row or had a "matching" solid-row pixel in the same column.
"""

import numpy as np

def find_solid_rows(grid):
    # Find rows that are entirely of one color.
    rows, cols = grid.shape
    solid_rows = []
    for r in range(rows):
        unique_colors = np.unique(grid[r, :])
        if len(unique_colors) == 1:
            solid_rows.append((r, unique_colors[0]))  # (row_index, color)
    return solid_rows

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find solid rows.
    solid_rows = find_solid_rows(input_grid)

    # Preserve solid rows.
    for row_index, color in solid_rows:
        output_grid[row_index, :] = color

    # Conditional Pixel Preservation and Removal
    for r in range(rows):
        for c in range(cols):
            if any(r == row_index for row_index, _ in solid_rows):
                continue # Already handled solid rows

            keep_pixel = False
            for row_index, color in solid_rows:
                if input_grid[r, c] == color:
                    keep_pixel = True
                    break

            if not keep_pixel:
                output_grid[r,c] = 0
            elif not any(r == row_index and input_grid[r,c] == color for row_index, color in solid_rows):
                solid_row_colors = [color for _, color in solid_rows]
                if input_grid[r,c] not in solid_row_colors:
                    output_grid[r,c] = 0

    # final pass to extend solid line colors down.
    for r in range(rows):
        for c in range(cols):
             for row_index, color in solid_rows:
                if r > row_index and input_grid[r,c] == color and output_grid[row_index, c] == color:
                  output_grid[r,c] = color


    return output_grid