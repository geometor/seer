"""
Transformation Rule:

1. Identify initial objects: In the input grid, we have a single red pixel (color 2) at coordinates (3, 2) and a single blue pixel (color 1) at (6, 6). The rest is background (color 0).

2. Red object action: The red pixel triggers the creation of four yellow pixels (color 4). These yellow pixels appear in a square pattern *around* where the red pixel *would have been*, if it had been moved one row up:
    - Two yellow pixels above where the red pixel is located.
    - Two yellow pixels below.
    - The yellow pixels are positioned one column to the left and one column to the right.

3. Blue object Action: Similarly, the blue pixel remains in place, but four orange pixels (color 7) appear around the blue pixel and with the same logic.

    -   One orange pixel to the top.
    -   One orange pixel to the bottom.
    -   One orange pixel on the left.
    -    One orange pixel on the right.

4.  Preservation of Initial Objects: The original red and blue pixels maintain its color and position.

In short, we have two agents (red and blue). The red agent creates a cross (top, bottom, left, right) of color 4 centered one row above its position. The blue agent creates a cross (top, bottom, left, right) of color 7 centered in its position.
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