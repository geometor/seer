# 0a938d79 • 014 • example_3 - CODE

---
```python
"""
1.  **Identify Key Pixels:** Locate all pixels in the input grid that are not white (color 0). In this case, find the red pixel (value 2) and the green pixel (value 3).
2.  **Horizontal Expansion:** For each identified pixel, expand its color horizontally to fill the entire row.
3.  **Vertical Repetition:** Duplicate each expanded row vertically. Alternate rows with orignal locations for red and green, so one row of red, then a row of white, the next a row of green and a row of white, etc, throughout the entire grid. If lines of different colors are on top of each other, they will overwrite each other in the order red and green pixels.
"""

import numpy as np

def find_non_white_pixels(grid):
    # Find coordinates of all non-white pixels
    non_white_pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel != 0:
                non_white_pixels.append((row_idx, col_idx, pixel))
    return non_white_pixels

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.zeros_like(input_grid)
    
    # Find non-white pixels
    non_white_pixels = find_non_white_pixels(input_grid)

    # Expand each non-white pixel horizontally and repeat vertically
    for row_idx, col_idx, pixel_value in non_white_pixels:
        # Horizontal expansion
        output_grid[row_idx, :] = pixel_value

    # Alternate rows
    for row in range(output_grid.shape[0]):
        for r,c,v in non_white_pixels:
            if (row - r) % 2 == 0 :
                 output_grid[row,:] = v


    return output_grid
```
