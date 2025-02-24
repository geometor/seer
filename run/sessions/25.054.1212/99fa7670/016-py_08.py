"""
1.  **Identify Non-zero Pixels:** Find all pixels in the input grid that are not white (value 0). Record their color and original (row, column) position.
2.  **Horizontal Expansion:** For each non-zero pixel, set all pixels in its row to that pixel's color.
3.  **Restricted Fill-Down:** For each non-zero pixel identified in step 1, starting from its *original* row and *original* column, fill downwards in that column with the pixel's color until the bottom of the grid is reached.  This fill-down only occurs in the columns where non-zero pixels originally existed.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify non-zero pixels and their original positions
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] != 0:
                non_zero_pixels.append((r, c, output_grid[r, c]))

    # Horizontal Expansion
    for r, c, color in non_zero_pixels:
        output_grid[r, :] = color

    # Restricted Fill-Down
    for r, c, color in non_zero_pixels:
        for i in range(r, rows):
            output_grid[i, c] = color

    return output_grid