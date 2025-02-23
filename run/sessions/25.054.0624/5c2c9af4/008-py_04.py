"""
The transformation rule takes sparse red pixels in the input grid and generates a pattern of nested red squares in the output grid. The red pixels in the input do not directly map to the output, but their presence triggers the generation of the nested square pattern.
"""

import numpy as np

def get_red_pixels(grid):
    """
    Finds the coordinates of all red pixels in the input grid.
    """
    return np.argwhere(grid == 2)

def transform(input_grid):
    """
    Transforms the input grid into an output grid with nested red squares.
    """
    # Initialize the output grid with all white pixels.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find red pixels in the input (though their exact locations aren't directly used).
    red_pixels = get_red_pixels(input_grid)

    #if no red pixels, return blank grid
    if len(red_pixels) == 0:
      return output_grid

    # Determine the number of nested squares and their sizes/spacing.
    # Drawing nested squares
    for i in range(min(rows, cols) // 2):
       
        #top
        output_grid[i, i:cols-i] = 2

        #bottom
        output_grid[rows-1-i, i:cols-i] = 2

        #left
        output_grid[i:rows-i, i] = 2

        #right
        output_grid[i:rows-i, cols-1-i] = 2

    return output_grid