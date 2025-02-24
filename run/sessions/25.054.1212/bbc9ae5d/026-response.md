# bbc9ae5d • 026 • example_5 • investigate_coder

---
```python
"""
1.  **Identify** the orange (7) pixel in the input grid.
2.  **Expand** the orange area. Create a 3x3 block of orange pixels in output grid, with position of original orange pixel as the top left cell.
3.   **Copy** all white (0) pixel positions
4.  **Construct** the output grid, maintaining the original horizontal length, but with 3 times the original height.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_grid = np.zeros((input_height * 3, input_width), dtype=int)

    # Find the orange pixel
    orange_pixels = np.where(input_grid == 7)
    if orange_pixels[0].size > 0:  # Check if any orange pixels were found
       orange_row, orange_col = orange_pixels[0][0], orange_pixels[1][0]

       # Expand the orange pixel to a 3x3 block
       for i in range(3):
           for j in range(3):
               output_grid[orange_row + i, orange_col + j] = 7

    # Copy white pixel positions (accounting for expansion)
    white_pixels = np.where(input_grid == 0)
    for i in range(len(white_pixels[0])):
        row = white_pixels[0][i]
        col = white_pixels[1][i]

        output_grid[row, col] = 0
        output_grid[row + input_height, col] = 0
        output_grid[row + 2*input_height, col] = 0
        

    return output_grid
```
