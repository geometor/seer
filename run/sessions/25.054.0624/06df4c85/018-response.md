# 06df4c85 • 018 • refine_coder

---
```python
"""
1.  **Identify Yellow Bands:** Find all horizontal bands of yellow (4) pixels that are exactly three pixels high.

2.  **Locate Islands:** Within each yellow band, identify 2x2 "islands" of green (3) or red (2) pixels.

3.  **Propagate Green:** For each green (3) island:
    *   Expand the green color horizontally to the left and right, *within the yellow band*.
    *   Stop the expansion when a non-yellow pixel or the grid edge is encountered.

4.  **Propagate Red:** For each red (2) island:
    *   Expand the red color horizontally to the left and right, *within the yellow band*.
    *   Stop when a non-yellow pixel or the grid boundary is encountered.
    *   Check the cells directly above the current red island's cells. If any of those cells are green, then do not replace yellow color of corresponding column with red.

5. **Fill in Yellow:** Within each band, after expansion, replace any remaining yellow with the color that has most recently expanded into it. If there are multiple colors, fill with last color that would be encountered traveling left-to-right.

6.  **Preserve Other Pixels:** All pixels outside the identified yellow bands remain unchanged.
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

def is_island(grid, r, c, color):
    rows, cols = grid.shape
    if r + 1 >= rows or c + 1 >= cols:
        return False
    return (grid[r, c] == color and
            grid[r + 1, c] == color and
            grid[r, c + 1] == color and
            grid[r + 1, c + 1] == color)

def propagate_color(grid, r, c, color, band_start_row, band_height):
    rows, cols = grid.shape

    # Propagate left
    for i in range(c - 1, -1, -1):
        if band_start_row <= r < band_start_row + band_height and grid[r,i] == 4:
           grid[r, i] = color
        else:
            break
    # Propagate right
    for i in range(c+2,cols):
        if band_start_row <= r < band_start_row + band_height and grid[r,i] == 4:
            grid[r,i] = color
        else:
            break

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find horizontal bands of yellow (4) with height 3
    yellow_bands = find_horizontal_bands(output_grid, 4, 3)

    # Iterate through each yellow band
    for band_start_row in yellow_bands:
        # Iterate within the band to find islands
        for r in range(band_start_row, band_start_row + 3):
            for c in range(cols):
                # Green island propagation
                if is_island(output_grid, r, c, 3):
                    propagate_color(output_grid, r, c, 3, band_start_row, 3)
                    #Also propagate to the other rows of the band
                    if r == band_start_row:
                       propagate_color(output_grid, r+1, c, 3, band_start_row, 3)
                       propagate_color(output_grid, r+2, c, 3, band_start_row, 3)
                    elif r == band_start_row + 1:
                       propagate_color(output_grid, r-1, c, 3, band_start_row, 3)
                       propagate_color(output_grid, r+1, c, 3, band_start_row, 3)
                    else: # r == band_start_row + 2
                       propagate_color(output_grid, r-2, c, 3, band_start_row, 3)
                       propagate_color(output_grid, r-1, c, 3, band_start_row, 3)

                # Red island propagation
                elif is_island(output_grid, r, c, 2):
                    # Check for green directly above.
                    suppress = False
                    if r > 0 and grid[r-1,c] == 3:
                        suppress = True
                    if r > 0 and grid[r-1, c+1] == 3:
                        suppress = True
                    if not suppress:
                        propagate_color(output_grid, r, c, 2, band_start_row, 3)
                        #Also propagate to the other rows of the band
                        if r == band_start_row:
                           propagate_color(output_grid, r+1, c, 2, band_start_row, 3)
                           propagate_color(output_grid, r+2, c, 2, band_start_row, 3)
                        elif r == band_start_row + 1:
                           propagate_color(output_grid, r-1, c, 2, band_start_row, 3)
                           propagate_color(output_grid, r+1, c, 2, band_start_row, 3)
                        else: # r == band_start_row + 2
                           propagate_color(output_grid, r-2, c, 2, band_start_row, 3)
                           propagate_color(output_grid, r-1, c, 2, band_start_row, 3)


    return output_grid
```
