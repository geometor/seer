"""
The transformation rule is a generalization of the previous example. We apply the "decoration" rule around *every* red and blue cell.

1.  Copy all cells from the input to the output grid.

2.  For each red cell in the input grid:
    *   Place a yellow cell one position above, below, to the left, and to the right of the red cell's location.

3.  For each blue cell in the input grid:
    *   Place an orange cell one position above, below, to the left and to the right of the blue cell's location.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize the output grid
    output_grid = np.copy(input_grid)

    # Find all red (2) and blue (1) cells
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)
    # print(red_positions)
    # print(blue_positions)

    # Create yellow crosses around each red cell
    for y, x in red_positions:
      if y > 0:
        output_grid[y-1, x] = 4
      if y < output_grid.shape[0]-1:
        output_grid[y+1, x] = 4
      if x > 0:
        output_grid[y, x-1] = 4
      if x < output_grid.shape[1]-1:
        output_grid[y, x+1] = 4

    # Create orange surround for each blue cell
    for y, x in blue_positions:
      if y > 0:
        output_grid[y-1,x] = 7
      if y < output_grid.shape[0]-1:
          output_grid[y+1,x] = 7
      if x > 0:
          output_grid[y,x-1] = 7
      if x < output_grid.shape[1]-1:
          output_grid[y,x+1] = 7
    return output_grid