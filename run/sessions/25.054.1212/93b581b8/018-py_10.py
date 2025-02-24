"""
1.  **Identify Central Block:** Locate the *inner* 2x2 block of non-zero pixels within the input grid.
2.  **Preserve the central block:** The central 2x2 goes to the same place in output and input.
3.  **Color-Based Mirroring:** For each *color* present in the central 2x2 block:
    *   Create a new 2x2 block in the output grid with that same color.
    *   The position of this 2x2 block in the input determines which *corner* of the output grid receives a copy, the color in the central 2x2 block corresponds to the output corner by this rule, using top left corner of 2x2 block as the position.
        *    top left color - goes to top left of output
        *    top right color - goes to top right of output
        *    bottom left color - goes to the bottom left
        *    bottom right color goes to the bottom right
4.  **Fill Remaining:** Any remaining pixels in the output grid not part of the central 2x2 block or the mirrored blocks are set to 0 (black).
"""

import numpy as np

def find_central_block(grid):
    # Find the inner-most 2x2 block of non-zero pixels
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            block = grid[r:r+2, c:c+2]
            if np.all(block != 0):
                return r, c
    return None

def transform(input_grid):
    # Initialize output_grid as all zeros
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the central 2x2 block
    central_block_coords = find_central_block(input_grid)
    if central_block_coords is None:
        return output_grid  # Return all zeros if no central block is found

    r, c = central_block_coords

    # Preserve central block
    output_grid[r:r+2, c:c+2] = input_grid[r:r+2, c:c+2]
    
    # Mirror each cell to the corresponding corner based on position inside the central block
    for i in range(2):
        for j in range(2):
            color = input_grid[r + i, c + j]
            if i == 0 and j == 0: # Top Left
                output_grid[0:2, 0:2] = color
            elif i == 0 and j == 1: # Top Right
                output_grid[0:2, cols - 2:cols] = color
            elif i == 1 and j == 0: # Bottom Left
                output_grid[rows - 2:rows, 0:2] = color
            elif i == 1 and j == 1: # Bottom Right
                output_grid[rows - 2:rows, cols - 2:cols] = color

    return output_grid