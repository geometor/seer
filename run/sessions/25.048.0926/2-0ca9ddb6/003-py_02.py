"""
The transformation rule involves drawing a yellow cross above the red cell and an orange cross around the blue cell. The original cells remain, other positions remain unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object with the given color.
    coords = np.where(grid == color)
    positions = []
    for i in range(len(coords[0])):
           positions.append( (coords[0][i], coords[1][i]))
    return positions # return all occurences

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the red object (color 2)
    red_positions = find_object(input_grid, 2)
    for red_pos in red_positions:
        # Create the yellow cross one cell above red
        row, col = red_pos
        output_grid[row - 1 , col - 1] = 4
        output_grid[row - 1, col + 1] = 4
        output_grid[row - 2, col]     = 4 # cell above
        output_grid[row, col ]       = 2 # preserve location
        # output_grid[row - 1, col] = 4 # cell above, removed
        # output_grid[row + 1, col] = 4 # cell below, removed

    # Find the blue object (color 1)
    blue_positions = find_object(input_grid, 1)
    for blue_pos in blue_positions:
        # Create the orange cross around blue
        row, col = blue_pos
        output_grid[row - 1, col] = 7
        output_grid[row + 1, col] = 7
        output_grid[row, col - 1] = 7
        output_grid[row, col + 1] = 7

    return output_grid