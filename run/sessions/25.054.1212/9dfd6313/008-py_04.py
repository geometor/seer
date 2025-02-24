"""
The transformation rearranges colored pixels (non-zero) within a 4x4 grid. Gray (5) pixels remain stationary. Magenta (6) pixels move to the top-right, preserving their original column-then-row order. The yellow (4) pixel moves to the position immediately above the bottom-right gray pixel. All other cells are filled with white (0).
"""

import numpy as np

def get_colored_pixels(grid, color):
    """
    Finds the coordinates of all pixels of a specified color.
    Returns a list of (row, col) tuples.
    """
    pixels = []
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color:
                pixels.append((row, col))
    return pixels

def transform(input_grid):
    # Initialize output grid with all zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Keep gray (5) pixels in place
    gray_pixels = get_colored_pixels(input_grid, 5)
    for row, col in gray_pixels:
        output_grid[row, col] = 5

    # Move magenta (6) pixels to top-right, preserving order
    magenta_pixels = get_colored_pixels(input_grid, 6)
    magenta_pixels.sort(key=lambda x: (x[1], x[0]))  # Sort by column, then row
    magenta_target_row = 0
    magenta_target_col = 2
    
    for _ in magenta_pixels:
      output_grid[magenta_target_row, magenta_target_col] = 6
      magenta_target_col +=1
      if magenta_target_col > 3:
        magenta_target_row += 1
        magenta_target_col = 2
    
    # Move yellow (4) pixel above the bottom-right gray (5)
    yellow_pixels = get_colored_pixels(input_grid, 4)
    if yellow_pixels:  # Check if there's a yellow pixel
        bottom_right_five = None
        for r in range(input_grid.shape[0]-1, -1, -1):
          for c in range(input_grid.shape[1]-1, -1, -1):
            if input_grid[r,c] == 5:
              bottom_right_five = (r,c)
              break
          if bottom_right_five:
            break

        if bottom_right_five:
          target_row = bottom_right_five[0] -1
          target_col = bottom_right_five[1]
          if target_row >= 0:
            output_grid[target_row, target_col] = 4


    return output_grid