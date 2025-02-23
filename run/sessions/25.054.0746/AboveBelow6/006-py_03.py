"""
1.  Identify Red Bands: Locate all horizontal bands of red (2) pixels, even if not fully contiguous on a single row. A red band might be "interrupted" by other color pixels.
2.  Determine Expansion: Each identified red band expands downwards by two rows.
3. Expansion and Overwrite For each red band, starting from the top-most:
    *   Copy the pixels from the row where the red band starts.
    *   Insert two copies of this row immediately below the start row of the red band. The original rows below the expanded rows, are overwritten by the expansion.
    *   If there is no room, skip the expansion for that band.
4.  No Padding. Do not add extra padding rows.
5. Preserve. No pixels should shift - pixels above should remain and pixels below should be overwritten by the expanded object.
"""

import numpy as np

def find_red_bands(grid):
    # Find rows containing red pixels, even if non-contiguous
    red_rows = np.where(np.any(grid == 2, axis=1))[0]
    bands = []
    for row in red_rows:
        bands.append(row)
    return bands

def transform(input_grid):
    # Create a copy to avoid modifying the original
    output_grid = np.copy(input_grid)
    original_height = input_grid.shape[0]

    # Find all red bands
    red_bands = find_red_bands(output_grid)

    # Expand each red band downwards by two rows
    for start_row in red_bands:
        # Check if there is enough space to expand
        if start_row + 3 <= original_height:
           #copy pixels from start row
           red_band_row = output_grid[start_row,:]
           # Insert two copies below the start row
           for i in range(1, 3):
              output_grid[start_row + i, :] = red_band_row

    return output_grid