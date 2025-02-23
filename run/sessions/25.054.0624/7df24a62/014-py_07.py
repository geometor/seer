"""
Identifies yellow (4) pixels in the input grid and places blue (1) pixels adjacent to them, replacing yellow pixels with blue if they are in adjacent positions.
"""

import numpy as np

def get_adjacent_positions(grid, row, col):
    """Gets the adjacent positions (including diagonals) for a given cell."""
    rows, cols = grid.shape
    adjacent_positions = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):  # Exclude the cell itself
                adjacent_positions.append((i, j))
    return adjacent_positions

def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is yellow
            if input_grid[row, col] == 4:
                # Get adjacent positions
                adjacent_coords = get_adjacent_positions(input_grid, row, col)
                # Iterate through adjacent positions
                for r, c in adjacent_coords:

                    # if the cell is yellow (4), change it to blue (1)
                    if output_grid[r,c] == 4:
                        output_grid[r,c] = 1
                    # if the position is empty, and adjacent to yellow pixel, fill it with blue
                    elif output_grid[r,c] == 0:
                        output_grid[r, c] = 1

    return output_grid