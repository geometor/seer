"""
The transformation involves using the red and blue cells in the input as anchor points to create new colored cells in the output. Yellow cells are placed relative to the red cell, and orange cells cluster around the blue cell, replacing the single blue cell. The positions of the original red and blue are unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a specific color in the grid.
    coords = np.argwhere(grid == color)
    return coords[0] if coords.size > 0 else None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = input_grid.copy()

    # Find the red (color 2) and blue (color 1) cells.
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Place yellow cells relative to the red cell.
    if red_pos is not None:
        yellow_row = red_pos[0] - 2
        if yellow_row >= 0:
          output_grid[yellow_row, red_pos[1]] = 4
          output_grid[yellow_row, red_pos[1] + 2] = 4
        yellow_row = red_pos[0] - 1
        if yellow_row >= 0:
          output_grid[yellow_row-1, red_pos[1]] = 4
          output_grid[yellow_row-1, red_pos[1] + 2] = 4

    # Create orange cells around the blue cell.
    if blue_pos is not None:
        output_grid[blue_pos[0], blue_pos[1] - 1] = 7  # Left
        output_grid[blue_pos[0], blue_pos[1] + 1] = 7  # Right
        output_grid[blue_pos[0] + 1, blue_pos[1]] = 7  # Down
        output_grid[blue_pos[0] + 1, blue_pos[1] + 0] = 7 #Added +0 to avoid overwrite
        output_grid[blue_pos[0] + 1, blue_pos[1] -1] = 7

    return output_grid