"""
The transformation involves keeping the original red and blue cells and adding yellow cells relative to the red cell and adding orange cells to form an L-shape around the blue cell. Then a final orange cell is added by mirroring, relative to the blue cell, one of the already available orange cells.
"""

import numpy as np

def find_object(grid, color):
    """Finds the position of a single-cell object of the specified color."""
    coords = np.argwhere(grid == color)
    if coords.size > 0:
        return tuple(coords[0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    
    # Find the red and blue cells
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Red cell actions: add yellow cells
    if red_pos:
        output_grid[red_pos[0] - 1, red_pos[1] - 1] = 4
        output_grid[red_pos[0] - 1, red_pos[1] + 1] = 4

    # Blue cell actions: add orange cells in L-shape and mirrored
    if blue_pos:
        output_grid[blue_pos[0] , blue_pos[1] - 1] = 7
        output_grid[blue_pos[0] + 1, blue_pos[1] - 1] = 7
        output_grid[blue_pos[0] + 1, blue_pos[1]] = 7
        output_grid[blue_pos[0] + 1, blue_pos[1] + 1] = 7
        output_grid[blue_pos[0] , blue_pos[1] + 1] = 7  # Mirrored cell

    return output_grid