"""
1.  **Identify Initial Positions:** Locate all red (2) and green (3) pixels in the input grid.

2.  **Expand:** For each red and green pixel, create a 3x3 block of the same color centered on the original pixel's location in the output grid. If the edges go beyond the sides, then stop there.

3.  **Overlap (Interaction):** Where the expanded 3x3 regions of red and green pixels overlap, replace those pixels in the output grid with gray (5) pixels.

4.  **Fill**: keep the rest of the grid as the same, white (0) pixels
"""

import numpy as np

def get_pixels_by_color(grid, color):
    """Finds the positions of all pixels of a given color."""
    return np.argwhere(grid == color)

def expand_pixel(grid, position, color):
    """Expands a pixel into a 3x3 block."""
    rows, cols = grid.shape
    row, col = position
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            grid[i, j] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Get initial positions of red and green pixels
    red_pixels = get_pixels_by_color(input_grid, 2)
    green_pixels = get_pixels_by_color(input_grid, 3)
    
    # Expand the red and green pixels first, store in temp grids for overlap
    expanded_red_grid = np.copy(input_grid)
    for pos in red_pixels:
       expanded_red_grid =  expand_pixel(expanded_red_grid, pos, 2)
       
    expanded_green_grid = np.copy(input_grid)
    for pos in green_pixels:
        expanded_green_grid = expand_pixel(expanded_green_grid, pos, 3)

    # combine expanded red and green and create gray
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if(expanded_red_grid[i,j] == 2 and expanded_green_grid[i,j] == 3):
                output_grid[i,j] = 5
            elif(expanded_red_grid[i,j] == 2):
                output_grid[i,j] = 2
            elif(expanded_green_grid[i,j] == 3):
                output_grid[i,j] = 3
            else:
                output_grid[i,j] = 0 # keep existing background

    return output_grid