"""
1.  **Identify Non-Zero Pixels:** Locate all pixels in the input grid that are not white (value 0). Note their color and their original row and column position.

2.  **Horizontal Expansion:** For each non-zero pixel, change all pixels in its row to that pixel's color.

3.  **Restricted Vertical Expansion (Fill-Down):** For each non-zero pixel identified in step 1, fill downwards *from its original row and column position*. The fill color is the color of the original non-zero pixel. The fill extends to the bottom of the grid, but *only* within that original column. Do not use any horizontally changed values for fill down.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # 1. Identify Non-Zero Pixels
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] != 0:
                non_zero_pixels.append((r, c, output_grid[r, c]))

    # 2. Horizontal Expansion
    for r, _, color in non_zero_pixels:
        output_grid[r, :] = color

    # 3. Restricted Vertical Expansion (Fill-Down)
    # Re-iterate using *original* positions
    for orig_r, orig_c, color in non_zero_pixels:
        for r in range(orig_r, rows):
            output_grid[r, orig_c] = color

    return output_grid