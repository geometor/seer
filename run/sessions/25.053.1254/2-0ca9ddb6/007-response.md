# 2-0ca9ddb6 • 007 • refine_coder

---
```python
"""
1.  Identify Key Colors: Locate all red (2), blue (1), and other non-black colored pixels in the input grid.
2.  Yellow Placement (around red): For each red pixel:
    *   Place a yellow (4) pixel one position to the left and one position to the right of the red pixel, *on the row above and the row below* the red pixel's row. If these positions are outside the grid boundaries or occupied by non-black pixels, do not place a yellow pixel in that specific location.
3.  Orange Placement (around blue): For each blue pixel:
    *   Place an orange (7) pixel one position to the left and one position to the right of the blue pixel, *on the same row* as the blue pixel.
    * If blue is below red, place orange pixels on the rows above and below, similar to rule 2
    *   If these positions are outside the grid boundaries, or occupied by non-black pixels, do not place an orange pixel.
4. Other non-black: other non-black pixels remain unchanged
5.  Preserve Other Colors: All other non-black pixels from the input grid that were *not* red or blue should remain in their original positions and retain their original colors in the output grid.
6. Black pixels unchanged: Black (0) pixels are considered the background and are not explicitly acted upon, except where replaced by yellow or orange pixels according to the rules above.
"""

import numpy as np

def find_pixels(grid, color):
    """Finds all pixels of a given color in the grid."""
    return np.argwhere(grid == color)

def is_valid(grid, row, col):
    """Checks if a position is within the grid boundaries."""
    return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)

    # Find red and blue pixels
    red_pixels = find_pixels(input_grid, 2)
    blue_pixels = find_pixels(input_grid, 1)
    
    # Place yellow pixels around red pixels
    for r, c in red_pixels:
        for dr in [-1, 1]:  # Above and below
            new_r = r + dr
            for dc in [-1, 1]: # Left and Right
              new_c = c + dc
              if is_valid(input_grid, new_r, new_c) and input_grid[new_r,new_c] == 0:
                  output_grid[new_r, new_c] = 4

    # Place orange pixels around blue pixels
    for r, c in blue_pixels:
      #check if any red pixel is above
      red_above = False
      for red_r, red_c in red_pixels:
        if red_r < r:
          red_above = True
          break

      for dc in [-1, 1]:
          new_c = c + dc
          if is_valid(input_grid, r, new_c) and input_grid[r,new_c] == 0 :
              output_grid[r, new_c] = 7
      if red_above:
        for dr in [-1, 1]:
          new_r = r + dr
          for dc in [-1,1]:
            new_c = c + dc
            if is_valid(input_grid, new_r, new_c) and input_grid[new_r, new_c] == 0:
                output_grid[new_r,new_c] = 7
    return output_grid
```
