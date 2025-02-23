"""
Change the uppermost central azure pixel to blue.
"""

import numpy as np

def get_azure_pixels(grid):
    # Find coordinates of all azure (8) pixels
    return np.argwhere(grid == 8)

def transform(input_grid):
    """
    Transforms the input grid by changing the uppermost central azure pixel to blue.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure pixels
    azure_pixels = get_azure_pixels(input_grid)

    if azure_pixels.size > 0:
        
        #sort by row, then by column.
        sorted_pixels = azure_pixels[np.lexsort((azure_pixels[:, 1], azure_pixels[:, 0]))]
        
        #find vertical mid point.
        min_row = np.min(sorted_pixels[:, 0])
        max_row = np.max(sorted_pixels[:, 0])
        mid_row = (min_row + max_row) / 2

        #select only those near the mid row (within 0.5).
        central_pixels = sorted_pixels[(sorted_pixels[:, 0] >= mid_row - 0.5) & (sorted_pixels[:, 0] <= mid_row + 0.5 )]

        if len(central_pixels) > 0:
             #select top most pixel
            target_pixel = central_pixels[0]

            # Change the color of the target pixel to blue (1)
            output_grid[target_pixel[0], target_pixel[1]] = 1

    return output_grid