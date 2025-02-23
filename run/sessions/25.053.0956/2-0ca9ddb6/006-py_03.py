"""
Scans the input grid and identifies all non-white (non-zero) pixels, "original pixels".
Initializes an output grid identical to the input grid.
Iterates through each original pixel:
    Examines the four neighboring positions (up, down, left, right) around the original pixel.
    Adds new pixels in the output grid one above, one below, one left and one right of the original pixel.
        If original pixel is blue(1), add orange(7) pixels.
        if original pixel is red (2), add yellow(4) pixels.
        if original pixel is magenta (6), no new pixels.
    If a neighboring position is outside the grid boundaries, skip adding a pixel in that direction.
    If a neighboring postion is not white(0) then skip adding a pixel in that direction.
Returns the updated output grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    def get_neighbors(r, c):
      """get valid neighbors, skipping out of bounds"""
      neighbors = []

      if r > 0:
        neighbors.append( (r-1,c) )
      if r < rows - 1:
        neighbors.append( (r+1,c) )
      if c > 0:
        neighbors.append( (r, c-1) )
      if c < cols - 1:
        neighbors.append( (r, c+1) )
      return neighbors
        

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            pixel_value = input_grid[r, c]

            # Process based on the pixel color
            if pixel_value == 1:  # Blue
                new_color = 7  # Orange
            elif pixel_value == 2:  # Red
                new_color = 4  # Yellow
            elif pixel_value == 6:  # Magenta
                new_color = None # no new color
            else:
                continue

            if new_color is not None:
              neighbors = get_neighbors(r,c)
              for nr, nc in neighbors:
                if output_grid[nr,nc] == 0:
                  output_grid[nr, nc] = new_color

    return output_grid