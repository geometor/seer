"""
The transformation rule is to locate the single blue square in the input grid and change its color to red in the output grid. All other cells maintain their original colors.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of the object with the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
       return coords
    else:
       return None

def transform(input_grid):
    """
    Transforms the input grid by changing the blue square to red.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the coordinates of the blue square (color 1)
    blue_square_coords = find_object(input_grid, 1)
    
    # Check that object was found
    if blue_square_coords is not None:
       # Change the color of the blue square to red (color 2) in the output_grid
       output_grid[blue_square_coords] = 2

    return output_grid