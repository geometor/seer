"""
Examine each azure pixel in the input grid. An azure pixel should be retained in the output grid if and only if it is part of a contiguous group of two or more azure pixels, either horizontally or vertically. A contiguous group is defined as a sequence of adjacent azure pixels, where adjacency means sharing a side (not just a corner). If an azure pixel is not part of such a group, replace it with a white pixel (value 0) in the output grid.
"""

import numpy as np

def has_adjacent_neighbor(grid, i, j, direction):
    """
    Checks if a given azure pixel at (i, j) has an adjacent azure neighbor in the specified direction,
    and if that neighbor also has a neighbor in the same direction.

    Args:
        grid: The input grid (numpy array).
        i: Row index of the pixel.
        j: Column index of the pixel.
        direction: 'horizontal' or 'vertical'.

    Returns:
        True if the pixel has a neighbor in the specified direction and that neighbor also has a neighbor. False otherwise.
    """
    color = grid[i, j]

    if direction == 'horizontal':
        # Check right neighbor
        if j + 1 < grid.shape[1] and grid[i, j + 1] == color:
             if j + 2 < grid.shape[1] and grid[i, j+2] == color:
                return True
        # Check left neighbor
        if j - 1 >= 0 and grid[i, j - 1] == color:
            if j - 2 >= 0 and grid[i, j - 2] == color:
                return True

    elif direction == 'vertical':
        # Check bottom neighbor
        if i + 1 < grid.shape[0] and grid[i + 1, j] == color:
            if i + 2 < grid.shape[0] and grid[i+2, j] == color:
                return True
        # Check top neighbor
        if i - 1 >= 0 and grid[i - 1, j] == color:
           if i - 2 >= 0 and grid[i-2, j] == color:
                return True

    return False


def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Iterate through the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # If the pixel is azure (8), check its horizontal and vertical neighbors.
            if input_grid[i, j] == 8:
                # Check for horizontal and vertical neighbors.
                if has_adjacent_neighbor(input_grid, i, j, 'horizontal') or \
                   has_adjacent_neighbor(input_grid, i, j, 'vertical'):
                    output_grid[i, j] = 8
                else:
                    output_grid[i,j] = 0
            else:
                output_grid[i,j] = input_grid[i,j] # copy other colors

    return output_grid