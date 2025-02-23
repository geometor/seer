"""
Red pixels become azure. Gray pixels become azure if they are adjacent to a red/azure pixel AND are part of a continuous gray area that is also adjacent to the azure area.  Isolated gray pixels or those only diagonally adjacent without a connecting gray path do not change.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """Returns a list of valid neighbor coordinates."""
    neighbors = []
    for i in range(max(0, r - 1), min(grid.shape[0], r + 2)):
        for j in range(max(0, c - 1), min(grid.shape[1], c + 2)):
            if (i, j) != (r, c):
                neighbors.append((i, j))
    return neighbors

def is_continuous_with_azure(grid, r, c, azure_pixels):
    """
    Checks if the gray pixel at (r, c) is part of a continuous gray area
    that is also adjacent to the azure area.
    """

    if grid[r,c] != 5:
        return False #must start with grey
    
    gray_neighbors = []
    for nr, nc in get_neighbors(grid, r, c):
        if grid[nr, nc] == 5:
             gray_neighbors.append((nr,nc))

    for ar, ac in azure_pixels:
        if (ar,ac) in get_neighbors(grid,r,c):
          # found adjacent azure, now see if there is gray between
          # check if this is part of connected extension
          for gr, gc in gray_neighbors:
              if (gr,gc) in get_neighbors(grid, ar, ac):
                return True  # grey neighbor of the grey is also a neighbor of the azure, so connected
    return False

def transform(input_grid):
    """
    Transforms the input grid by replacing red pixels with azure and conditionally replacing adjacent gray pixels.
    """
    output_grid = np.copy(input_grid)
    red_pixels = np.argwhere(input_grid == 2)
    azure_pixels = []

    # First, change all red pixels to azure
    for r, c in red_pixels:
        output_grid[r, c] = 8
        azure_pixels.append((r,c))

    # Then, conditionally change gray pixels
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if output_grid[r, c] == 5:  # Check gray pixels
                if is_continuous_with_azure(output_grid, r, c, azure_pixels):
                     output_grid[r,c] = 8

    return output_grid