"""
1.  **Identify** the 2x2 block of pixels near the center of the input grid with 2 magenta (6), and 2 red (2) pixels.
2. **Inversion** select the original square and invert the colors, the red (2) becomes magenta (6).
3.  **Expansion:** Expand the magenta color to fill the grid, starting from the
    bottom left corner.
"""

import numpy as np

def find_2x2_block(grid):
    # Find a 2x2 block with magenta (6) and red (2)
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i, j] == 6 and grid[i, j+1] == 2 and
                grid[i+1, j] == 2 and grid[i+1, j+1] == 6):
                return (i, j)  # Top-left coordinates of the block
    return None

def transform(input_grid):
    # Initialize output_grid with zeros and same dimensions as input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the 2x2 block
    block_coords = find_2x2_block(input_grid)

    if block_coords:
        # "Inversion" and color change: Replace red (2) with magenta (6)
      
        # Expansion and fill: Fill the output grid with magenta, starting from bottom-left.
        for i in range(rows):
            for j in range(cols):
                if i + j <= rows-1: #this fills the lower triangle
                  output_grid[rows - 1 - i, j] = 6

    return output_grid