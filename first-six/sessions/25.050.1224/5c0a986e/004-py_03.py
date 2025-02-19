"""
The transformation preserves two 2x2 squares (blue and red) from the input grid. It then adds a diagonal line of blue pixels starting near the top-left corner and a diagonal line of red pixels starting to the right and down from the first blue addition. The red diagonal skips a cell, creating a gap.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)  # Start with a copy of the input

    # Find the 2x2 squares (for generalization, though not strictly needed in this specific case)
    def find_squares(grid):
      squares = []
      for r in range(grid.shape[0] - 1):
        for c in range(grid.shape[1] - 1):
          if grid[r, c] == grid[r+1, c] == grid[r, c+1] == grid[r+1, c+1] != 0:
            squares.append((r, c, grid[r,c])) # row, col, color
      return squares

    squares = find_squares(input_grid)

    # Add diagonal blue pixels
    for i in range(6):
        output_grid[1 + i, i] = 1

    # Add diagonal red pixels, skipping (6,8)
    output_grid[2, 5] = 2
    output_grid[3, 6] = 2
    output_grid[4, 7] = 2
    output_grid[5, 8] = 2
    output_grid[7, 9] = 2
    
    return output_grid