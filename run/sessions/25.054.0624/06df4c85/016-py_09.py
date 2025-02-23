"""
1.  **Identify Horizontal Bands:** Locate the horizontal bands of solid yellow (4) pixels. These bands are three pixels high.

2.  **Identify Islands:** Within each yellow band, identify "islands" of green (3) and red (2) pixels. These islands are 2x2 blocks.

3.  **Propagate Colors (Conditional):**
    *   If a 2x2 island is green (3): Expand the green color horizontally to the left and right *within* the yellow band. The expansion fills the yellow band, replacing any yellow (4) pixels.
    *   If a 2x2 island is red (2): Expand the red color horizontally to the left and right *within* the yellow band, replacing any yellow (4) pixels. Furthermore, if the row immediately above has green, do not replace yellow with red.

4.  **No Change Outside Bands:** Pixels outside the identified yellow bands remain unchanged.
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

def propagate_color_in_band(grid, band_start_row, band_height, color):
    for r in range(band_start_row, band_start_row + band_height):
        for c in range(grid.shape[1]):
            if grid[r,c] == 4:  # Only replace yellow pixels
              grid[r, c] = color

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
                    propagate_color_in_band(output_grid, band_start_row, 3, 3)
                # Red island propagation
                elif is_island(output_grid, r, c, 2):
                    # Check for green in the row above
                    if r > band_start_row and 3 in output_grid[r - 1, :]:
                        continue  # Skip red propagation
                    else:
                        propagate_color_in_band(output_grid, band_start_row, 3, 2)

    return output_grid