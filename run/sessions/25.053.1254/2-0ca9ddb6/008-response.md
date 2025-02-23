# 2-0ca9ddb6 • 008 • refine_coder

---
```python
"""
1.  **Locate Key Pixels:** Find the locations of the red (2) and blue (1) pixels within the input grid.  There will be at most one of each.

2.  **Create Yellow Region (Conditional):** Around the red (2) pixel, create a 3x3 square region. Within this region, change *only* the background (0) pixels to yellow (4). If the original input grid contains a non-zero color at the position of the red pixel, preserve it, and place it in the center of the 3x3 yellow region.

3.  **Create Orange Region (Conditional):** Around the blue (1) pixel, create a 3x3 square region.  Within this region, change *only* the background (0) pixels to orange (7). If the original input grid contains a non-zero color at the position of the blue pixel, preserve it, and place it in the center of the 3x3 orange region.

4.  **Preserve Other Colors:** Pixels in the input grid that have colors other than 0, 1 and 2 should be preserved and included in the output at their original coordinates.

5.  **Output:** The modified grid is the output.
"""

import numpy as np

def find_pixel(grid, color):
    # Find the coordinates of a specific color pixel.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return first occurrence
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find the red (2) pixel
    red_pixel_coords = find_pixel(input_grid, 2)
    if red_pixel_coords:
        # Create a 3x3 yellow (4) region around the red pixel, conditionally
        row, col = red_pixel_coords
        for i in range(max(0, row - 1), min(output_grid.shape[0], row + 2)):
            for j in range(max(0, col - 1), min(output_grid.shape[1], col + 2)):
                if output_grid[i, j] == 0:  # Only replace if background (0)
                    output_grid[i, j] = 4
        output_grid[row,col] = input_grid[row,col] # preserve input color


    # Find the blue (1) pixel
    blue_pixel_coords = find_pixel(input_grid, 1)
    if blue_pixel_coords:
        # Create a 3x3 orange (7) region around the blue pixel, conditionally
        row, col = blue_pixel_coords
        for i in range(max(0, row - 1), min(output_grid.shape[0], row + 2)):
            for j in range(max(0, col - 1), min(output_grid.shape[1], col + 2)):
                if output_grid[i, j] == 0:  # Only replace if background (0)
                    output_grid[i, j] = 7
        output_grid[row,col] = input_grid[row,col] # preserve input color

    return output_grid
```

