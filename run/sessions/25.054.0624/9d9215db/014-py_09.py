"""
1. **Identify Non-Zero Pixels:** Locate all pixels in the input grid that have a color value other than 0 (white). These are the "seed" pixels.

2. **Horizontal Extension/Repetition:** For each seed pixel:
    a. Extend the pixel's color horizontally to the left and right. The pattern alternates between the colors in a row.
    b. The extension length seems to extend to the edges of the input grid, or where the 0 value is encountered.
    c. A minimum length of one unit to the left and the right

3. **Vertical Extension:** The color '3' green expands to fill the height of the grid in its original column

4. **Result:** The output grid is formed by combining these horizontal and vertical expansions. It is as though the seed pixels' colors have "bled" outwards, primarily horizontally but also vertically for color '3'(green).
"""

import numpy as np

def get_nonzero_pixels(grid):
    """Finds the coordinates and colors of non-zero pixels in a grid."""
    nonzero_pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                nonzero_pixels.append(((r, c), value))
    return nonzero_pixels

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Get non-zero pixels
    nonzero_pixels = get_nonzero_pixels(input_grid)
    
    # Horizontal and Vertical Extensions
    for (row, col), value in nonzero_pixels:
        # Horizontal Extension
        
        output_grid[row, :] = input_grid[row,:]
        
        
        left = col - 1
        right = col + 1

        
        while left >= 0:
           output_grid[row, left] = value
           left -= 1

        while right < cols:
            output_grid[row, right] = value
            right += 1
        
        # Vertical Extension (only for green color '3')

        if value == 3:
            output_grid[:, col] = 3

    # replace intermediate zeros
    for (row, col), value in nonzero_pixels:
      for c in range(cols):
        if output_grid[row,c] == 0:
          if c > 0 and c < cols-1:
            if output_grid[row,c-1] != 0 and output_grid[row, c+1] != 0:
              output_grid[row,c] = output_grid[row,c-1]


    return output_grid