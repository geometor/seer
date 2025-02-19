"""
The transformation involves several actions. The cell with color code `2` is replaced with color code `8`. Then this new cell will have a copy below. After that, the background, originally white (color 0), is changed to green (color 3), while the azure object remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)

    # Find the coordinates of the cell with color 2.
    red_coords = np.argwhere(input_grid == 2)

    # Replace all instances of color 2 with color 8.
    output_grid[input_grid == 2] = 8

    #Extend the existing object.
    if len(red_coords) > 0:
      row, col = red_coords[0]
      output_grid[row+1, col] = 8


    # Create a new grid filled with color 3 (green).
    new_output_grid = np.full(input_grid.shape, 3)

    # Copy the azure (color 8) object from output_grid to new_output_grid.
    new_output_grid[output_grid == 8] = 8

    return new_output_grid