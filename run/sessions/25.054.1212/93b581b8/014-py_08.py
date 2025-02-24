"""
The transformation identifies a central 2x2 block of colored pixels and preserves it. 
Then, for the green and magenta colors in the central block, it mirrors those colors
by creating 2x2 regions filled with color 3 (green) in the lower right corner
and color 6 (magenta) at the bottom left corner of the grid.
Colors 2 (red) and 5 (grey) are not processed to be mirrored in that way.
"""

import numpy as np

def find_central_block(grid):
    # Find the largest 2x2 block of non-zero pixels
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            block = grid[r:r+2, c:c+2]
            if np.all(block != 0):
                return r, c
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find the central 2x2 block
    central_block_coords = find_central_block(input_grid)
    if central_block_coords is None:
      return output_grid

    r, c = central_block_coords

    # Preserve the central block (unnecessary since we copied, but for clarity)
    # output_grid[r:r+2, c:c+2] = input_grid[r:r+2, c:c+2]

    # Mirror based on colors 3 and 6 in center block (simplified based on observation)
    # Check for color 3 (green)
    if 3 in input_grid[r:r+2, c:c+2]:
       output_grid[rows-2:rows, cols-2:cols] = 3

    #Check for color 6 (magenta)
    if 6 in input_grid[r:r+2, c:c+2]:
       output_grid[rows-2:rows, 0:2] = 6
    
    #Check for color 2 (red)
    if 2 in input_grid[r:r+2, c:c+2]:
       output_grid[0:2, 0:2] = 2
       
    #Check for color 5 (grey)
    if 5 in input_grid[r:r+2, c:c+2]:
       output_grid[0:2, cols-2:cols] = 5

    return output_grid