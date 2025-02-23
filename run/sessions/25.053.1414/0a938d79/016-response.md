# 0a938d79 • 016 • refine_coder

---
```python
"""
1.  **Identify Non-White Pixels:** Find all pixels in the input grid that are not white (color 0). Note their color and original row and column.
2.  **Horizontal Expansion:** For each non-white pixel, create a full row of pixels with its color, starting with the original coordinates.
3.  **Vertical Interleaving:** Create a new output grid with the same dimensions as the input. For each row in the output, find the original rows of all non-white pixels in the input. Populate the new row by horizontally expanding the color of any matching pixels in the input. If multiple pixels can be expanded into a grid location, prioritize them in their numeric order, so lower color numbers are overwritten by higher color numbers.
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
    # Initialize output_grid as all zeros, same size as input
    output_grid = np.zeros(input_grid.shape, dtype=int)
    
    # Find non-white pixels and their original positions
    non_white_pixels = find_non_white_pixels(input_grid)

    # Create the rows, by expanding the color across the row
    expanded_rows = {}
    for r, c, v in non_white_pixels:
      expanded_rows[r] = [v] * input_grid.shape[1]
    
    # Create output by expanding rows and stacking, overwriting 
    #   if there are conflicts based on color value
    for output_row in range(output_grid.shape[0]):
      for r, c, v in non_white_pixels:
        # expand rows, including the original row
        if (output_row - r) % (len(non_white_pixels)) == 0:
           output_grid[output_row,:] = expanded_rows[r]
           
    return output_grid
```
