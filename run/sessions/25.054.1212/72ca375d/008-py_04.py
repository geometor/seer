"""
Identify the 2x2 square region of yellow (color 4) pixels in the input grid, and output this region.
"""

import numpy as np

def find_object(grid, color, shape_type=None, dimensions=None):
    """
    Finds objects of a specific color, optionally matching shape and dimensions.
    Returns a list of (start_row, start_col) positions.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                if shape_type == "rectangle" and dimensions:
                  width, height = dimensions
                  if r + height <= rows and c + width <= cols:
                      subgrid = grid[r:r+height, c:c+width]
                      if np.all(subgrid == color):
                        objects.append((r,c))

                # add logic here for more shapes if ever required

                else: # any object
                  objects.append((r,c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid by extracting the 2x2 yellow square.
    """
    # Find the 2x2 yellow (color 4) square.
    yellow_squares = find_object(input_grid, color=4, shape_type="rectangle", dimensions=(2, 2))

    # Extract the first found 2x2 yellow square.
    if yellow_squares:
        start_row, start_col = yellow_squares[0]
        output_grid = input_grid[start_row:start_row+2, start_col:start_col+2]
        return output_grid
    else:
      return None # handle case where no 2x2 yellow is present
