"""
For each red (2) pixel in the input grid, copy the red pixel and place a yellow (4) pixel directly above and below it, if within bounds.
For each blue (1) pixel in the input grid, copy the blue pixel and place an orange (7) pixel directly above, below, left, and right, if within bounds.
All other pixels are ignored, and the output grid is initialized with zeros.
"""

import numpy as np

def get_colored_pixels(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == color:
                pixels.append((r, c))
    return pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find red pixels and expand vertically.
    red_pixels = get_colored_pixels(input_grid, 2)
    for r, c in red_pixels:
      output_grid[r,c] = 2 # transfer original
      if r > 0:
          output_grid[r - 1, c] = 4
      if r < output_grid.shape[0] - 1:
          output_grid[r + 1, c] = 4

    # Find blue pixels and expand horizontally and vertically.
    blue_pixels = get_colored_pixels(input_grid, 1)
    for r, c in blue_pixels:
        output_grid[r,c] = 1 # transfer original
        if r > 0:
            output_grid[r - 1, c] = 7
        if r < output_grid.shape[0] - 1:
            output_grid[r + 1, c] = 7
        if c > 0:
            output_grid[r, c - 1] = 7
        if c < output_grid.shape[1] - 1:
            output_grid[r, c + 1] = 7

    return output_grid