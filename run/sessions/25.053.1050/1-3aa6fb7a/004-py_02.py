"""
Change the uppermost central azure pixel to blue.
Central is defined by sorting first by column, and selecting the
left-most, then among those, selecting the top-most pixel.
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
        
        #sort by column, then by row.
        sorted_pixels = azure_pixels[np.lexsort((azure_pixels[:, 0], azure_pixels[:, 1]))]
        
        #select top most pixel
        target_pixel = sorted_pixels[0]

        # Change the color of the target pixel to blue (1)
        output_grid[target_pixel[0], target_pixel[1]] = 1

    return output_grid