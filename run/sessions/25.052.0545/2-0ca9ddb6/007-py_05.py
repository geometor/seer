"""
Each single red object in the input gets a yellow "L" shape as its shadow.
Each single blue object in the input gets an orange cross shape surrounding it.
Other single objects remain unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the position of a single-cell object with the given color.
    positions = np.argwhere(grid == color)
    # Return all positions, not just the first one
    return positions if positions.size > 0 else []

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the positions of the red objects (color 2).
    red_positions = find_object(input_grid, 2)
    for red_pos in red_positions:
        # Create yellow "L" shape relative to each red object.
        output_grid[red_pos[0] - 1, red_pos[1] - 1] = 4
        output_grid[red_pos[0] - 1, red_pos[1] + 1] = 4
        output_grid[red_pos[0] + 1, red_pos[1] - 1] = 4
        output_grid[red_pos[0] + 1, red_pos[1] + 1] = 4

    # Find the positions of the blue objects (color 1).
    blue_positions = find_object(input_grid, 1)
    for blue_pos in blue_positions:
        # Create an orange cross around each blue object.
        output_grid[blue_pos[0] - 1, blue_pos[1]] = 7
        output_grid[blue_pos[0] + 1, blue_pos[1]] = 7
        output_grid[blue_pos[0], blue_pos[1] - 1] = 7
        output_grid[blue_pos[0], blue_pos[1] + 1] = 7

    return output_grid