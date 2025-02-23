"""
The transformation rule involves a color swap between two specific colors. The colors that are swapped depend on the presence of those colors in each example. If blue and red are present, those colors are swapped. If blue and green are present, those colors are swapped. The position and shapes of other colored objects remain unchanged. The output grid maintains the same dimensions as the input grid.

Iterating through the color swap combinations:

1.  **Check for Blue (1) and Red (2):** If both colors are present in the input grid, swap all instances of blue with red and red with blue.
2. **Check for Blue (1) and Green(3):** If both colors are present, and the condition in step 1 is not met, then swap blue with green, and green with blue.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Check for presence of blue (1) and red (2).
    has_blue = 1 in input_grid
    has_red = 2 in input_grid

    if has_blue and has_red:
        # Swap blue (1) with red (2) and vice versa.
        output_grid[input_grid == 1] = 2
        output_grid[input_grid == 2] = 1
    else:
        # Check for presence of blue (1) and green (3).
        has_green = 3 in input_grid
        if has_blue and has_green:
           #Swap blue(1) and green(3)
           output_grid[input_grid == 1] = 3
           output_grid[input_grid == 3] = 1

    return output_grid