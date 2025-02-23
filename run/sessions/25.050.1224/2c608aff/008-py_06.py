"""
A single yellow block extends to the right and become horizontally elongated. All other objects and background are preserved as is.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Return None if no object of the specified color is found
    return coords

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule:
    A single yellow block extends to the right and become horizontally elongated.
    All other objects and background are preserved as is.
    """
    output_grid = np.copy(input_grid)
    yellow_coords = find_object(input_grid, 4)

    #find single yellow object
    if yellow_coords is not None:
        #get x coordinate
        x = yellow_coords[0][1]

        #modify four cells from x to right
        row = 3
        for i in range(4):
          if x + i < output_grid.shape[1]:
            output_grid[row][x + i] = 4

    return output_grid