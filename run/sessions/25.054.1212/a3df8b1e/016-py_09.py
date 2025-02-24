"""
1. **Find the Blue Pixel:** Scan the input grid to find the location (row and column) of the single blue (1) pixel.
2. **Center the Cross:** Use the row and column of the blue pixel found in step 1 as the center coordinates for a cross pattern in the output grid.
3. **Create the Cross:** In the output grid, set the color of the single pixel where the row and colum intersect (the location of the blue pixel) to blue(1). Then, change the color of the other pixels in the same row *and* the other pixels in the same column as the located blue pixel to blue(1), forming a cross centered on the original blue pixel. All other pixels should remain white(0).
"""

import numpy as np

def find_blue_pixel(grid):
    # Find the coordinates of the blue pixel (value 1).
    for r_idx, row in enumerate(grid):
        for c_idx, pixel in enumerate(row):
            if pixel == 1:
                return r_idx, c_idx
    return None

def transform(input_grid):
    # Initialize output_grid as all white.
    output_grid = np.zeros_like(input_grid)

    # Find the blue pixel's location.
    blue_pixel_location = find_blue_pixel(input_grid)

    if blue_pixel_location:
      center_row, center_col = blue_pixel_location

      # Create the cross pattern, centered at the original blue pixel.
      for r_idx in range(output_grid.shape[0]):
          output_grid[r_idx, center_col] = 1  # Vertical line.
      for c_idx in range(output_grid.shape[1]):
          output_grid[center_row, c_idx] = 1  # Horizontal line.

    return output_grid