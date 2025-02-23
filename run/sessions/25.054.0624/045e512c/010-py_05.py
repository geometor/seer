"""
The transformation involves expanding colored pixels around a central, unchanged horizontal line of blue pixels. Each non-black pixel expands into a 3x3 square centered on the original pixel's location, except for blue pixels which remain unchanged if forming the central horizontal line. If a non-black pixel isn't part of the central blue line, it is treated according to the expansion rule.

1. **Identify Core:** Locate the horizontal line of blue (1) pixels. This serves as a central structure.
2. **Expansion:** Expand each non-black pixel (except the blue pixels forming the central horizontal line) into a 3x3 square, centered on the original pixel's location.
3. **Blue Axis:** The blue pixels forming the central horizontal line remain in their original position.
"""

import numpy as np

def find_blue_line(grid):
    # Find coordinates of blue pixels (1)
    blue_coords = np.argwhere(grid == 1)
    if len(blue_coords) < 2: # assuming minimum two for it to be a line
      return None

    # check if contiguous horizontally
    is_horizontal = all(blue_coords[i][0] == blue_coords[0][0] for i in range(len(blue_coords)))
    if not is_horizontal:
        return None

    return blue_coords

def expand_pixel(grid, r, c, color):
    # expand a given pixel into a 3x3 square centered at (r, c)
    rows, cols = grid.shape
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            grid[i, j] = color
    return grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find the blue line
    blue_line = find_blue_line(input_grid)

    # Copy the blue line first
    if blue_line is not None:
        for r, c in blue_line:
          output_grid[r,c] = 1


    # expand other colors, checking that a given pixel is not part of the central blue axis
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            color = input_grid[r, c]
            if color != 0:  # Skip black pixels
              if blue_line is not None and color == 1 and r == blue_line[0][0] and any(c == col for _, col in blue_line):
                continue # skip if part of central blue line
              else:
                output_grid = expand_pixel(output_grid, r, c, color)

    return output_grid