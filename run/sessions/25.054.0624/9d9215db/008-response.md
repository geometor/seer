# 9d9215db • 008 • example_2 • investigate_coder

---
```python
"""
1. **Identify Key Pixels:** Locate all non-white pixels (specifically blue (1), green (3), and yellow (4)) in the input grid.

2. **Mirror Green and Yellow:** For each green (3) pixel, mirror its position vertically across the center row of the grid. For each yellow pixel (4), mirror vertically across the center row.

3. **Expand Blue Pixels:**
    - Find horizontal distance from the line of blue pixels to edge of grid, on each side.
    - Create horizontal and vertical lines of blue pixels expanding out, using the distance.
    - Yellow and Green pixels in output from step 2 acts as barriers for blue pixel replication, blue will stop.
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
            output_grid[mirrored_coord] = input_grid[r, c]

    # Expand Blue Pixels
    blue_pixels = [(r, c) for r, c in non_white_pixels if input_grid[r, c] == 1]
    if blue_pixels:
        #assumes blue pixels form a contiguous horizontal line, as per task
        min_blue_col = min(c for _, c in blue_pixels)
        max_blue_col = max(c for _, c in blue_pixels)

        #find center blue row
        blue_row = blue_pixels[0][0]

        #calculate distances
        dist_left = min_blue_col
        dist_right = cols - 1 - max_blue_col
        dist_up = blue_row
        dist_down = rows - 1 - blue_row


        #horizontal expansion (left)
        for c in range(dist_left):
           if output_grid[blue_row, c] == 0:
              output_grid[blue_row, c] = 1

        #horizontal expansion (right)
        for c in range(cols - dist_right, cols):
          if output_grid[blue_row,c] == 0:
            output_grid[blue_row, c] = 1

        #vertical expansion (up)
        for r in range(dist_up):
            for c in range(min_blue_col, max_blue_col + 1):
               if output_grid[r,c] == 0:
                output_grid[r, c] = 1

        #vertical expansion (down)
        for r in range(rows-dist_down, rows):
            for c in range(min_blue_col, max_blue_col + 1):
              if output_grid[r,c] == 0:
                output_grid[r, c] = 1
    return output_grid
```
