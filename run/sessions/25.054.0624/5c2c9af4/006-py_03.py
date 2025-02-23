"""
The transformation identifies non-black (non-0) pixels in the input grid and expands them outwards in the output grid, while preserving the black background. The exact expansion rule is complex and may involve shape creation or tracing, not just simple dilation.
"""

import numpy as np
from collections import Counter

def find_non_background_pixels(grid, background_color=0):
    """Finds the positions of pixels that are not the background color."""
    non_background_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != background_color:
                non_background_pixels.append(((r, c), grid[r, c]))  # Store position and color
    return non_background_pixels

def expand_pixels(input_grid, non_background_pixels):
    """Expands non-background pixels outwards, preserving the background."""
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    for (r, c), color in non_background_pixels:
      #initial implementation of simple dilation, to build on
      for x in range(-1,2):
          for y in range(-1,2):
              new_r = r + x
              new_c = c + y

              if 0 <= new_r < rows and 0<= new_c < cols:
                    output_grid[new_r,new_c] = color
    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()

    # Identify non-background pixels
    non_background_pixels = find_non_background_pixels(input_grid)

    # Expand or trace the non-background pixels, preserving background
    output_grid = expand_pixels(input_grid, non_background_pixels)

    return output_grid