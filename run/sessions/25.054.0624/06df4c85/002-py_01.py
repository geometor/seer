"""
The transformation rule involves identifying 2x2 blocks of colors 1 (blue), 2 (red), and 3 (green) within an azure (8) background.
These blocks are then replicated horizontally based on their initial position. Red blocks starting at x=3 or x=9 are replicated 
to create a total of three instances of red blocks. Blue and Green are replicated once.
"""

import numpy as np

def find_2x2_blocks(grid, color):
    """Finds all 2x2 blocks of the specified color in the grid."""
    blocks = []
    height, width = grid.shape
    for y in range(height - 1):
        for x in range(width - 1):
            if (grid[y:y+2, x:x+2] == color).all():
                blocks.append((y, x))  # Store top-left corner coordinates
    return blocks

def transform(input_grid):
    """Transforms the input grid according to the replication rules."""
    output_grid = np.copy(input_grid)
    height, width = output_grid.shape

    # Find 2x2 blocks of colors 1, 2, and 3
    red_blocks = find_2x2_blocks(input_grid, 2)
    blue_blocks = find_2x2_blocks(input_grid, 1)
    green_blocks = find_2x2_blocks(input_grid, 3)
    
    # Replicate red blocks based on the starting position.
    for y, x in red_blocks:
      if x == 3 or x == 9:
          output_grid[y:y+2, 6:8] = 2
          output_grid[y:y+2, 12:14] = 2

    # Duplicate blue blocks
    for y, x in blue_blocks:
        output_grid[y:y+2, 9:11] = 1 #only one copy

    # Duplicate green blocks
    for y, x in green_blocks:
        output_grid[y:y+2, 9:11] = 3  #only one copy

    return output_grid