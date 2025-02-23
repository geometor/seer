"""
Swap all instances of gray (5) with azure (8), and all instances of azure (8) with gray (5) in the grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping all instances of gray (5) and azure (8).
    """
    output_grid = np.copy(input_grid)

    # Iterate through all cells
    for r in range(input_grid.shape[0]):
      for c in range(input_grid.shape[1]):
          # If the pixel is gray (5), change it to azure (8)
          if input_grid[r, c] == 5:
              output_grid[r, c] = 8
          # If the pixel is azure (8), change it to gray (5)
          elif input_grid[r, c] == 8:
              output_grid[r, c] = 5

    return output_grid