"""
The transformation involves expanding yellow and red pixels around a central, unchanged line of blue pixels.

1. **Identify Core:** Locate the horizontal line of blue (1) pixels. This serves as a central structure.
2. **Yellow Expansion:** Expand the yellow (4) pixels. Each single yellow pixel becomes a horizontal line of three yellow pixels, centered on the original yellow pixel's location.
3. **Blue Axis:** The position of the blue pixels doesn't change.
4. **Red Expansion:** Expand the red (2) pixels. The single red pixel expands to become a vertical and a horizontal line, using the original red pixel position as their meeting point, and adjacent to the sides of the original blue pixels.

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

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the blue line
    blue_line = find_blue_line(input_grid)

    # Yellow Expansion
    yellow_coords = np.argwhere(input_grid == 4)
    for y, x in yellow_coords:
        output_grid[y, max(0, x - 1):min(input_grid.shape[1], x + 2)] = 4

    # Red Expansion
    red_coords = np.argwhere(input_grid == 2)
    if blue_line is not None:
      blue_y = blue_line[0][0]
      for r, c in red_coords:
        # find nearest blue
        if blue_line is not None:
          output_grid[blue_y-1:blue_y+2,c] = 2 # extend vertically, including adjacent, making 3 cells
          output_grid[blue_y,blue_line[0][1]-1:blue_line[-1][1]+2] = 2 # add horizontal

    return output_grid