"""
The transformation rule is as follows:

1. **Identify Azure Regions:** Locate all contiguous horizontal sequences of azure (color 8) pixels in the input grid.

2. **Place Blue Pixels to the left and the right:** for each azure region, place a blue (color 1) pixel immediately to the right of the *rightmost* azure pixel of this region, and another blue pixel at the left, only if these are blank pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        c = 0
        while c < cols:
            if output_grid[r, c] == 8:
                # Found start of an azure region
                start_c = c
                while c < cols and output_grid[r, c] == 8:
                    c += 1
                end_c = c - 1  # Index of the rightmost azure pixel

                # Place blue to the right of the rightmost
                if end_c + 1 < cols and output_grid[r, end_c + 1] == 0:
                    output_grid[r, end_c + 1] = 1
                # Place blue to the left of the leftmost
                if start_c -1 >= 0 and output_grid[r, start_c -1] == 0:
                    output_grid[r,start_c -1] = 1
            else:
                c += 1

    return output_grid