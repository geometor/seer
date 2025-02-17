"""
Transformation Rule:

1.  **Identify initial objects:** The input grid contains a red pixel (color 2) at (2,2), a blue pixel (color 1) at (7,3), and a magenta pixel (color 6) at (5,6).

2.  **Red object action:** The red pixel triggers the creation of four yellow pixels (color 4) around the location where the red agent would be if it had moved one position up.

    *   Two yellow pixels above the original red pixel.
    *   Two yellow pixels below the original red pixel.
    *   All yellow pixels are separated by one cell from the vertical axis where the red pixel is located.

3.  **Blue object action:** The blue pixel triggers the creation of an orange cross of color 7 centered at its position.
    *   One orange pixel to the top.
    *   One orange pixel to the bottom.
    *   One orange pixel to the left.
    *    One orange pixel to the right.

4.  **Magenta object action:** The magenta pixel does not trigger any action, remaining unchanged.

5.  **Preservation of Initial Objects:** The original red, blue and magenta pixels are kept, without any changes.

The logic derived from the previous examples works here as well. Red agents generate a cross pattern of color 4 one row above their position. Blue agents create a cross pattern of color 7 centered on their position. Magenta, similar to azure, does not trigger any change.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            # Red object action
            if input_grid[r, c] == 2:  # Red pixel
                # Create four yellow pixels around the position one row above
                if r - 1 > 0:
                  if c - 1 >= 0:
                      output_grid[r - 2, c - 1] = 4
                  if c + 1 < input_grid.shape[1]:
                      output_grid[r - 2, c + 1] = 4
                if r > 0:
                  if c - 1 >= 0:
                      output_grid[r, c - 1] = 4
                  if c + 1 < input_grid.shape[1]:
                      output_grid[r, c + 1] = 4

            # Blue object action
            elif input_grid[r, c] == 1:  # Blue pixel
                # Create four orange pixels around the blue pixel
                if r - 1 >= 0:
                    output_grid[r - 1, c] = 7  # Top
                if r + 1 < input_grid.shape[0]:
                    output_grid[r + 1, c] = 7  # Bottom
                if c - 1 >= 0:
                    output_grid[r, c - 1] = 7  # Left
                if c + 1 < input_grid.shape[1]:
                    output_grid[r, c + 1] = 7  # Right

    return output_grid