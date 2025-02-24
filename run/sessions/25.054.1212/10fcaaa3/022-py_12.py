"""
Duplicates non-zero pixels in the input grid and conditionally fills zero 
pixels with azure (8) in the expanded output grid. The duplication rule shifts 
pixels horizontally, with a larger shift for pixels not in the first column.
"""

import numpy as np

def get_non_zero_pixels(grid):
    """Finds the coordinates of all non-zero pixels in the grid."""
    return np.argwhere(grid != 0)

def transform(input_grid):
    # Determine output grid size.
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 2, input_width * 2

    # Initialize output grid with zeros.
    output_grid = np.zeros((output_height, output_width), dtype=int)

     # Duplicate and position non-zero pixels.
    non_zero_pixels = get_non_zero_pixels(input_grid)
    for r, c in non_zero_pixels:
        color = input_grid[r, c]
        output_grid[r*2 + 1, c*2 + 1] = color  # original location in the upscaled output
        output_grid[r*2 + 1, (c+2)*2 + 1 if c > 0 else (c+1)*2+1 ] = color # copy at the upscaled x-coordinate to its right


    # Conditionally fill zero pixels with azure (8).
    for i in range(output_height):
        for j in range(output_width):
            if output_grid[i,j] == 0: # consider only zero locations
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                      output_grid[i,j] = 8

    return output_grid