# 06df4c85 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Horizontal Bands:** Locate the horizontal bands of solid yellow (4) pixels. These bands are three pixels high.

2.  **Identify Islands:** Within each yellow band, identify "islands" of green (3) and red (2) pixels. These islands are 2x2 blocks.

3.  **Propagate Colors (Conditional):**
    *   If an island is green (3): Expand the green color horizontally to the left and right *within* the yellow band. The expansion fills the entire width of the yellow band, replacing any white (0) pixels, only if there is an existing green island withing the yellow row.
    *   If an island is red (2): Expand the red color horizontally to the left and right *within* the yellow band, in place of white pixels (0), only if there is an existing red island. Furthermore, if the row immediately above has green, do not replace yellow with red.

4.  **No Change Outside Bands:** Pixels outside the identified yellow bands remain unchanged.
The rows that don't contain any Green or Red colored pixels are not affected.
"""

import numpy as np

def find_horizontal_bands(grid, band_color, band_height):
    bands = []
    rows, cols = grid.shape
    for r in range(rows - band_height + 1):
        is_band = True
        for i in range(band_height):
            if not np.all(grid[r + i, :] == band_color):
                is_band = False
                break
        if is_band:
            bands.append(r)
    return bands

def propagate_color(grid, row_start, color):
    rows, cols = grid.shape
    for r in range(row_start, row_start+3):
      for c in range(cols):
        if grid[r,c] != 4: # propagate only within band
          grid[r,c] = color

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find horizontal bands of yellow (4) with height 3
    yellow_bands = find_horizontal_bands(output_grid, 4, 3)

    # Iterate through each yellow band
    for band_start_row in yellow_bands:
        has_green = False
        has_red = False
        # check for green and red
        for r in range(band_start_row, band_start_row + 3):
            if 3 in output_grid[r, :]:
                has_green = True
            if 2 in output_grid[r, :]:
                has_red = True

        # propagate colors

        if has_green:
            propagate_color(output_grid, band_start_row, 3)
        if has_red:

          for r in range(band_start_row, band_start_row + 3):
              #skip row if row above contains green
              if r > 0 and 3 in output_grid[r-1,:]:
                continue

              propagate_color(output_grid, band_start_row, 2)


    return output_grid
```
