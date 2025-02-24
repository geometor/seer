"""
1.  **Identify** all red (2), green (3), and gray (5) pixels in the input grid.
2.  **Preserve** gray (5) pixels; they remain unchanged in the output.
2.  **Preserve** one of the red(2) pixels; they remain unchanged in the output.
3.  **Locate** instances where a red (2) pixel and a green (3) are in specific positions, the red being to the SW and NE of a green.
4.  **Replace** these green and red by the colour azure (8).
5. **Preserve** the location of green pixels.
6.  All other cells remain white (0).
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color).tolist()

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    input_grid_rows, input_grid_cols = input_grid.shape
    output_grid_rows, output_grid_cols = output_grid.shape
    
    # Find the locations of all relevant colors.
    red_pixels = find_pixels_by_color(input_grid, 2)
    green_pixels = find_pixels_by_color(input_grid, 3)
    gray_pixels = find_pixels_by_color(input_grid, 5)

    # Preserve gray pixels.
    #for row, col in gray_pixels:
    #    output_grid[row, col] = 5

    # Preserve green pixels
    #for row, col in green_pixels:
    #    output_grid[row, col] = 3
        
    # Preserve one red pixel.
    #if len(red_pixels)>1:
    #   output_grid[red_pixels[0][0], red_pixels[0][1]] = 2

    # Check for the red-green relationship and replace with azure.
    for r_row, r_col in red_pixels:
        for g_row, g_col in green_pixels:
            if (r_row == g_row + 1 and r_col == g_col - 1) or \
               (r_row == g_row - 1 and r_col == g_col + 1) :
                output_grid[r_row, r_col] = 8
                output_grid[g_row, g_col] = 8

    return output_grid