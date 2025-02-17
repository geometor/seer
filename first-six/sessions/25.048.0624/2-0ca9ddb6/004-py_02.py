"""
Transformation Rule:

1.  **Identify initial objects:** The input grid contains two red pixels (color 2), two blue pixels (color 1), and one azure pixel (color 8).

2.  **Red object action:** Each red pixel triggers the creation of four yellow pixels (color 4). These yellow pixels form a cross shape *around* the position where the red pixel *would have been*, if it had been moved one row up:

    *   Two yellow pixels above the original position.
    *   Two yellow pixels below the original position.
    *   The yellow pixels are positioned one column to the left and one column to the right.

3.  **Blue object action:** Each blue pixel triggers the creation of four orange pixels (color 7). These orange pixels create a cross centered at the blue pixel position.

    *   One orange pixel on the top.
    *   One orange pixel at the bottom.
    *   One orange pixel to the left.
    *   One orange pixel to the right.

4.  **Azure object action:** The azure pixel (color 8) does not trigger any action.

5.  **Preservation of Initial Objects:** All colored pixels (red, blue and azure) are kept, including their color and original position.

In summary, red and blue agents trigger the creation of crosses in different positions, and different colors (yellow and orange, respectively), while the azure agent does not have associated any actions.
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