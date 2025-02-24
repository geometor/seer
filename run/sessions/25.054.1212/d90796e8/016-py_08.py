"""
1.  **Identify** all red (2), green (3), and gray (5) pixels in the input grid.
2.  **Preserve** all gray (5) pixels; their color and position remain unchanged in the output grid.
3.  **Locate** instances where a red (2) pixel is diagonally adjacent to a green (3) pixel, either to the Northeast (NE) or Southwest (SW).
4.  **Replace** these *specific* instances of green and red pixel pairs with azure (8).
5. **Preserve** the rest of the red and green pixels that do not respect the condition of replacement.
6.  All other cells that are not explicitly mentioned above should be white/empty (0).
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color).tolist()

def transform(input_grid):
    # initialize output_grid with white cells
    output_grid = np.zeros_like(input_grid)
    input_grid_rows, input_grid_cols = input_grid.shape

    # Find the locations of all relevant colors.
    red_pixels = find_pixels_by_color(input_grid, 2)
    green_pixels = find_pixels_by_color(input_grid, 3)
    gray_pixels = find_pixels_by_color(input_grid, 5)

    # Preserve gray pixels.
    for row, col in gray_pixels:
       output_grid[row, col] = 5
    
    # Preserve green and red pixels that are not replaced
    for row, col in green_pixels:
        output_grid[row, col] = 3

    for row, col in red_pixels:
        output_grid[row, col] = 2

    # Check for the red-green relationship and replace with azure.
    for r_row, r_col in red_pixels:
        for g_row, g_col in green_pixels:
            if (r_row == g_row + 1 and r_col == g_col - 1) or \
               (r_row == g_row - 1 and r_col == g_col + 1) :
                output_grid[r_row, r_col] = 8
                output_grid[g_row, g_col] = 8

    return output_grid