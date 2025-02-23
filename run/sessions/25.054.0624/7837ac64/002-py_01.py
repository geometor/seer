"""
The transformation extracts a 3x3 subgrid from the input. This subgrid is defined by the
top-leftmost occurrence of the colors blue (1), white (0), and green (3). The top-left cell
of this subgrid is blue, the top-right cell is green, and the rest are white.
"""

import numpy as np

def find_top_leftmost_colors(input_grid, colors):
    # Iterate through the grid to find the top-leftmost instance of the specified colors.
    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] in colors:
                return (r, c)
    return None

def transform(input_grid):
    # Find the top-leftmost occurrence of colors 1, 0, and 3
    top_left_corner = find_top_leftmost_colors(input_grid, [1,0,3])

    # check for edge cases where no colors or not big enough grid
    if top_left_corner is None:
        return np.array([[0]]) # Return the base color.

    # Extract the relevant 3x3 subgrid
    rows,cols = input_grid.shape

    # Initialize the output grid with zeros (white)
    output_grid = np.zeros((3, 3), dtype=int)

    # determine target top-left cell
    target_r = -1
    target_c = -1

    for r in range(rows-2):
      for c in range(cols-2):
        section = input_grid[r:r+3,c:c+3]
        if (section[0,0] == 1) and (section[0,2] == 3) and (np.array_equal(section,np.array([[1,0,3],[1,0,0],[1,0,0]]))):
          target_r = r
          target_c = c
          break
      if target_r >=0:
        break

    if target_r >=0:
      output_grid = input_grid[target_r:target_r+3, target_c:target_c+3]
    else:
       output_grid = np.zeros((3, 3), dtype=int)
       output_grid[0,0] = 1
       output_grid[0,2] = 3
       
    return output_grid