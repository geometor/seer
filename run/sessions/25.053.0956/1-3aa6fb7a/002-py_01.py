"""
Iterate through all pixels in the input grid. If a pixel is azure (value 8),
determine if it should be changed to blue (value 1). An azure pixel is
changed to blue if it is in the first row of a group of azures in a
vertical line or is in the last row of azure pixel in a vertical line of
group of azures. Create a new grid with the modified pixel values.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions and values as the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is azure
            if output_grid[r, c] == 8:
                # Check for vertical adjacency of azure pixels
                is_first_in_vertical_line = (r == 0 or output_grid[r - 1, c] != 8)
                is_last_in_vertical_line = (r == rows - 1 or output_grid[r + 1, c] != 8)

                # Apply the color change rule
                if is_first_in_vertical_line or is_last_in_vertical_line:
                    output_grid[r, c] = 1

    return output_grid