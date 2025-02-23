"""
1. **Identify Key Pixels:** Locate all non-white pixels (specifically blue (1), green (3), and yellow (4)) in the input grid.

2. **Mirror Green and Yellow:** For each green (3) pixel, mirror its position vertically across the center row of the grid. For each yellow pixel (4), mirror vertically across the center row. If a mirrored position already has same color, don't change.

3. **Expand Blue Pixels:**
    - Find the leftmost and rightmost blue pixels in the original blue line.
    - Expand horizontally: fill the entire row with blue, starting from the leftmost edge of the grid up to the first non-white pixel or edge. Continue filling from the right most original blue to the right edge, stopping at any non-white pixel.
    - Expand vertically:  From each blue pixel in the expanded horizontal line, expand upwards and downwards. Stop expansion in a direction when a non-white pixel (or the grid edge) is encountered.

"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of non-white pixels."""
    coords = np.argwhere(grid != 0)
    return [tuple(coord) for coord in coords]

def mirror_vertically(grid, coord):
    """Mirrors a coordinate vertically across the center row."""
    center_row = grid.shape[0] // 2
    new_row = 2 * center_row - coord[0]
     # Handle edge case where grid height is even.
    if grid.shape[0] % 2 == 0 and new_row >= grid.shape[0]:
      new_row = grid.shape[0] - 1-(coord[0]-(grid.shape[0]//2))

    return (new_row, coord[1])

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify Key Pixels
    non_white_pixels = get_non_white_pixels(input_grid)

    # Mirror Green and Yellow
    for r, c in non_white_pixels:
        if input_grid[r, c] == 3 or input_grid[r,c] == 4:  # Green or yellow
            mirrored_coord = mirror_vertically(input_grid, (r, c))
            if output_grid[mirrored_coord] != input_grid[r,c]: #only update if not same color
              output_grid[mirrored_coord] = input_grid[r, c]

    # Expand Blue Pixels
    blue_pixels = [(r, c) for r, c in non_white_pixels if input_grid[r, c] == 1]
    if blue_pixels:
        #assumes blue pixels form a contiguous horizontal line, as per task
        min_blue_col = min(c for _, c in blue_pixels)
        max_blue_col = max(c for _, c in blue_pixels)
        blue_row = blue_pixels[0][0]

        #horizontal expansion (left to right)
        for c in range(cols):
          if output_grid[blue_row,c] == 0:
            output_grid[blue_row,c] = 1
          else:
            if c < min_blue_col: #before the original blue, stop if any color
                break
            elif c>=max_blue_col:#after blue, stop if not white
                if output_grid[blue_row,c] != 1:
                  break

        #Vertical Expansion, up and down, using the horizontal length
        for r in range(rows):
          for c in range(cols):
            if r == blue_row:
              continue #skip original row
            if output_grid[blue_row,c] == 1: #if original row is blue
               if output_grid[r,c] == 0:
                output_grid[r,c]=1

               elif r < blue_row:
                 if output_grid[r,c]!= 0:
                   break
               else:
                  if output_grid[r,c] != 0:
                    break
    return output_grid