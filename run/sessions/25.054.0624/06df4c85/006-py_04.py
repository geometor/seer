"""
The transformation rule involves identifying 2x2 blocks of colors 1 (blue), 2 (red), and 3 (green) within an azure (8) background.
These blocks are duplicated once next to their original positions. If the initial x coordinate of the block is odd, the block is replicated every six columns towards the right.
The first three rows, first three columns, and last three columns of the original grid are preserved.
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

    # Preserve the first three rows, first three columns and last three columns.
    # output_grid[:3, :] = input_grid[:3, :] #first 3 rows already copied
    # output_grid[:, :3] = input_grid[:, :3] # first 3 colums already copied
    # output_grid[:, width-3:] = input_grid[:, width-3:] # last 3 colums already copied


    # Find 2x2 blocks of colors 1, 2, and 3
    red_blocks = find_2x2_blocks(input_grid, 2)
    blue_blocks = find_2x2_blocks(input_grid, 1)
    green_blocks = find_2x2_blocks(input_grid, 3)
    
    # Replicate colored blocks.
    for y, x in red_blocks:
      output_grid[y:y+2, x+3:x+5] = 2 # duplicate once
      if x % 2 != 0: # odd
        for i in range(x + 6, width -1, 6):
            if i + 2 <= width: # Prevent index out of bounds
              output_grid[y:y+2, i:i+2] = 2
    
    for y, x in blue_blocks:
      output_grid[y:y+2, x+3:x+5] = 1
      if x % 2 != 0:
        for i in range(x + 6, width -1, 6):
            if i + 2 <= width:
              output_grid[y:y+2, i:i+2] = 1

    for y, x in green_blocks:
      output_grid[y:y+2, x+3:x+5] = 3
      if x % 2 != 0:
        for i in range(x + 6, width - 1, 6):
            if i + 2 <= width:
              output_grid[y:y+2, i:i+2] = 3

    return output_grid