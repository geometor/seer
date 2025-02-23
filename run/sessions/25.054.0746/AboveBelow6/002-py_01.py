"""
1. Identify Objects: Locate the rectangular band of red (2) pixels. Also, note the surrounding yellow (4) and white (0) areas.
2. Red Band Expansion: The transformation rule is to expand the red band downwards. Specifically, copy the existing row of the red band twice, placing the copies immediately below the original red band.
3. Preservation: All pixels not modified by the expansion remain the same between the input and output. Thus all the white pixels, and the yellow pixels above the red band remain unchanged. The yellow pixels at the bottom are replaced.
"""

import numpy as np

def find_red_band(grid):
    # Find the row indices where red pixels are present
    red_rows = np.where(np.any(grid == 2, axis=1))[0]
    if len(red_rows) > 0:
        # Assuming the red band is contiguous, return the start and end row
        return red_rows[0], red_rows[-1]
    else:
        return None, None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find the red band
    start_row, end_row = find_red_band(input_grid)

    # If red band is not found just return the input.
    if start_row is None:
        return output_grid
    
    # Get red band row
    red_band_row = input_grid[start_row, :]
    
    # Expand the red band downwards by 2 rows
    for i in range(1, 3):
      output_grid[end_row + i, :] = red_band_row
    
    return output_grid