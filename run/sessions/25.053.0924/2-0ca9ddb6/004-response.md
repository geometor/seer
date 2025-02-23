# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
1.  **Preserve Existing Pixels:**  The azure pixel at (0, 3) and the red pixels at (2, 6) and (7, 1) remain unchanged in their original positions.

2.  **Mirror Blue Pixels with Orange:** For each blue pixel:
    *   Create orange pixels by mirroring the blue pixel's position *horizontally* and *vertically*. Specifically, place an orange pixel one position to the left and one position to the right of the blue pixel in the same row, and one position above and one position below, if and only if these new locations are within the grid boundaries and are not currently occupied by a non-black (non-zero) pixel.

3. **Create Yellow Cross based on positions of Orange related to Red Pixels** For each blue pixel that generated orange pixels in step 2:
    * Create yellow pixels by mirroring, using the position *horizontally* and *vertically*. of the red pixels.
      * Place a yellow pixel two positions above the lowest red pixel
      * Place a yellow pixel two postions below the highest red pixel
      * Place a yellow pixel two position to the left of the rightmost red pixel.
      * Place a yellow pixel two position to the right of the leftmost red pixel.
"""

import numpy as np

def get_nonzero_pixels(grid):
    pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                pixels.append((r, c, value))
    return pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    input_pixels = get_nonzero_pixels(input_grid)

    # Find blue and red pixels
    blue_pixels = [(r, c) for r, c, val in input_pixels if val == 1]
    red_pixels = [(r, c) for r, c, val in input_pixels if val == 2]

    # Mirror blue pixels with orange (7)
    for r, c in blue_pixels:
        # Horizontal mirroring
        if c - 1 >= 0 and output_grid[r, c - 1] == 0:
            output_grid[r, c - 1] = 7
        if c + 1 < output_grid.shape[1] and output_grid[r, c + 1] == 0:
            output_grid[r, c + 1] = 7

        # Vertical mirroring
        if r - 1 >= 0 and output_grid[r - 1, c] == 0:
            output_grid[r - 1, c] = 7
        if r + 1 < output_grid.shape[0] and output_grid[r + 1, c] == 0:
            output_grid[r + 1, c] = 7

    # Create Yellow Cross based on positions of Orange(7) pixels
    if red_pixels: # only run if there are red pixels
      # find the lowest red pixel row
      lowest_red_row = max(red_pixels, key=lambda item:item[0])[0]
      # find the highest red pixel row
      highest_red_row = min(red_pixels, key=lambda item:item[0])[0]
      # find the leftmost red pixel column
      leftmost_red_col = min(red_pixels, key=lambda item:item[1])[1]
      # find the rightmost red pixel column
      rightmost_red_col = max(red_pixels, key=lambda item:item[1])[1]

      # place yellow two above the lowest red row, if allowed
      if highest_red_row - 2 >= 0:
        output_grid[highest_red_row - 2, leftmost_red_col] = 4
        output_grid[highest_red_row - 2, rightmost_red_col] = 4

      # place a yellow two below the highest red row, if allowed
      if lowest_red_row + 2 < output_grid.shape[0]:
        output_grid[lowest_red_row + 2, leftmost_red_col] = 4
        output_grid[lowest_red_row + 2, rightmost_red_col] = 4

    return output_grid
```
