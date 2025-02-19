"""
The transformation rule is as follows:
1. Identify a yellow "L" shaped object and a red cell in the input grid.
2. Remove the red cell.
3. Expand the yellow object into a 5x5 tilted square-like shape, pointing upwards and leftwards, 
   with its bottom-left corner 4 cells diagonally down and left from a starting position near the initial yellow object.

"""

import numpy as np

def find_object(grid, color):
    """Finds coordinates of cells with a specific color."""
    coords = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == color:
                coords.append((r, c))
    return coords

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Objects
    yellow_coords = find_object(input_grid, 4)
    #red_coords = find_object(input_grid, 2) # Not needed, we will just overwrite that cell

    # Determine expansion start. Take first yellow object for expansion.
    # There could be a more sophisticated start point

    # 2 & 3. Expand the yellow object and remove red
    # The expansion could be more sophistated, but it is a good start

    if len(yellow_coords)>0:
      start_row = yellow_coords[0][0]
      start_col = yellow_coords[0][1]
      # print(start_row, start_col)

      for i in range(5):
        for j in range(5):
            row = start_row -4 + i +j
            col = start_col +4 - i -3 + j
            # print(row,col)
            if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i>=2 and j>=2) :
                output_grid[row, col] = 4

    return output_grid