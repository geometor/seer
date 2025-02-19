"""
The transformation identifies single red (2) and blue (1) cells in the input grid.
It preserves these cells in the output. A yellow (4) cross is created around the red cell,
and an orange (7) cross is created around the blue cell. The crosses are formed by placing
the respective colors one cell away in each cardinal direction (up, down, left, right).
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
      return (coords[0][0], coords[1][0])
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    grid_size = input_grid.shape

    # Find the red and blue cells.
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)
    
    # create yellow cross around red cell.
    if red_pos:
      row, col = red_pos
      if row > 0:
        output_grid[row-1, col] = 4
      if row < grid_size[0] -1:
        output_grid[row+1, col] = 4
      if col > 0:
        output_grid[row, col-1] = 4
      if col < grid_size[1] - 1:
        output_grid[row, col+1] = 4

    # create orange cross around blue cell
    if blue_pos:
      row, col = blue_pos
      if row > 0:
        output_grid[row - 1, col] = 7
      if row < grid_size[0] - 1:
        output_grid[row + 1, col] = 7
      if col > 0:
        output_grid[row, col-1] = 7
      if col < grid_size[1] - 1:
          output_grid[row, col + 1] = 7      

    return output_grid