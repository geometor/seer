"""
Identifies non-white pixels in the input grid and expands them to the right and down, filling their respective rows and columns in the output grid.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of all non-white pixels in the grid."""
    non_white_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel_value in enumerate(row):
            if pixel_value != 0:
                non_white_pixels.append((row_index, col_index, pixel_value))
    return non_white_pixels

def transform(input_grid):
    """Transforms the input grid by expanding non-white pixels to the right and down."""
    # Initialize output_grid as all white with the same dimensions as input
    output_grid = np.zeros_like(input_grid)
    
    # Get non-white pixels and their locations
    non_white_pixels = get_non_white_pixels(input_grid)
    
    # Iterate through the non-white pixels
    for row, col, value in non_white_pixels:
        # Fill the row to the right with the pixel's value
        output_grid[row, col:] = value
        # Fill the columns down with the pixel's value
        output_grid[row:, col:] = value
    
    return output_grid