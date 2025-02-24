# d90796e8 • 018 • refine_coder

---
```python
"""
1.  **Initialization:** Start with an output grid filled entirely with white (0).
2.  **Preserve Gray:** Identify all gray (5) pixels in the input grid. Copy these pixels to the same positions in the output grid, maintaining their color.
3.  **Conditional Replacement:**
    *   Locate all red (2) and green (3) pixels in the input grid.
    *   For each red pixel, check if a green pixel exists diagonally adjacent to it in either the Northeast (NE) or Southwest (SW) direction.
    *   If such a diagonally adjacent green pixel is found, replace *both* the red and green pixels with azure (8) in the output grid.
4.  **Clear Remaining:** After processing all red and green pixels, any cell in the output grid that is not gray (5) or azure (8) should be set to white (0). This ensures that only the replaced pairs and the preserved gray pixels remain.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color).tolist()

def transform(input_grid):
    # initialize output_grid with white cells
    output_grid = np.zeros_like(input_grid)

    # Find the locations of all relevant colors.
    red_pixels = find_pixels_by_color(input_grid, 2)
    green_pixels = find_pixels_by_color(input_grid, 3)
    gray_pixels = find_pixels_by_color(input_grid, 5)

    # Preserve gray pixels.
    for row, col in gray_pixels:
       output_grid[row, col] = 5

    # Check for the red-green relationship and replace with azure.
    for r_row, r_col in red_pixels:
        for g_row, g_col in green_pixels:
            if (r_row == g_row + 1 and r_col == g_col - 1) or \
               (r_row == g_row - 1 and r_col == g_col + 1) :
                output_grid[r_row, r_col] = 8
                output_grid[g_row, g_col] = 8

    return output_grid
```
