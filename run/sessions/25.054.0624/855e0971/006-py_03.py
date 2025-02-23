"""
1.  **Identify Bands:** Divide the input grid into horizontal bands.  A band is a set of one or more contiguous rows that have identical color patterns. The first band is from row 0 to the first row that differs. Subsequent bands continue from the end of the previous band.
2.  **Find Propagation Starting Points:** For each band (except the first band), identify the *columns* that have white pixels (value 0) in the *first row* of that band.
3.  **Propagate White Pixels Downward:** For each band (except the first band) set the pixel in each column identified in step 2 to white (0) for all rows within that band.
4.  **Handle Single Band Case:** If the input grid consists of only a single band (spans entire height), then find any white pixels (value 0). If any white pixels exist, get the location of the *first row* where any non-white pixel exists, then set the values of all pixels in these column indices to 0, starting *from that row* down to the end of the grid.
5.  **Assemble Output:** Combine all (modified or unmodified) bands to create the output grid.
"""

import numpy as np

def _find_bands(grid):
    bands = []
    start_row = 0
    for i in range(1, grid.shape[0]):
        if not np.array_equal(grid[i], grid[start_row]):
            bands.append((start_row, i - 1))
            start_row = i
    bands.append((start_row, grid.shape[0] - 1))  # Add the last band
    return bands

def _find_white_pixel_columns_in_first_row(band, grid):
    white_columns = []
    first_row_of_band = band[0]
    for c in range(grid.shape[1]):
        if grid[first_row_of_band, c] == 0:
            white_columns.append(c)
    return white_columns

def _propagate_white_pixels(band, white_columns, grid):
    output_grid = np.copy(grid)
    for r in range(band[0], band[1] + 1):
        for c in white_columns:
            output_grid[r, c] = 0
    return output_grid


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # 1. Identify Bands
    bands = _find_bands(input_grid)

    # 2. & 3. Find and Propagate (for non-first bands)
    for band in bands[1:]:
        white_columns = _find_white_pixel_columns_in_first_row(band, input_grid)
        output_grid = _propagate_white_pixels(band, white_columns, output_grid)

    # 4. Handle Single Band Case
    if len(bands) == 1:
        white_columns = []
        for c in range(input_grid.shape[1]):
          if input_grid[0,c] == 0:
            white_columns.append(c)

        if len(white_columns) > 0:
            first_non_white_row = 0
            for r in range(input_grid.shape[0]):
              for c in white_columns:
                if input_grid[r,c] != 0:
                  first_non_white_row = r
                  break
              else:
                continue
              break

            for r in range(first_non_white_row, output_grid.shape[0]):
                for c in white_columns:
                  output_grid[r,c] = 0

    # 5. Assemble Output (already done in-place)
    return output_grid