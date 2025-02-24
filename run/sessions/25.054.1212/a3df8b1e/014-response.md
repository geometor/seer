# a3df8b1e • 014 • example_3 • investigate_coder

---
```python
"""
1. **Find the Blue Pixel:** Scan the input grid to find the location (row and column) of the single blue (1) pixel.
2. **Center the Cross:** Use the row and column of the blue pixel found in step 1 as the center coordinates for a cross pattern in the output grid.
3. **Create the Cross:** In the output grid, change the color of the pixels in the same row and column as the located blue pixel to blue(1), forming a cross. All other pixels should remain white(0).
"""

import numpy as np

def find_blue_pixel(grid):
    # Find the coordinates of the blue pixel (value 1).
    for r_idx, row in enumerate(grid):
        for c_idx, pixel in enumerate(row):
            if pixel == 1:
                return r_idx, c_idx
    return None  # Should not happen in valid cases, as a blue pixel is expected

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid, then convert to all white.
    output_grid = np.zeros_like(input_grid)

    # Find the blue pixel's location.
    blue_pixel_location = find_blue_pixel(input_grid)

    if blue_pixel_location:
      center_row, center_col = blue_pixel_location

      # Create the cross pattern.
      for r_idx in range(output_grid.shape[0]):
          output_grid[r_idx, center_col] = 1  # Vertical line of the cross.
      for c_idx in range(output_grid.shape[1]):
          output_grid[center_row, c_idx] = 1  # Horizontal line of the cross.
    return output_grid
```
