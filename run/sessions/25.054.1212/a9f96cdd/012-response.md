# a9f96cdd • 012 • refine_coder

---
```python
"""
1.  Locate: Find the single red (2) pixel in the input grid.

2.  Move and Recolor: Move the red pixel one position diagonally up and to the left. Change its color to green (3). If this new position is outside the grid, do *not* place the green pixel.

3.  Conditional Gray Pixel:
    *   If the green pixel was placed (new position was within bounds): Place a gray (6) pixel one position *above* the green pixel. If the gray pixel location would be out of bounds, do not place it.

4.  Azure and Orange Placement:
    *   If the green pixel was placed:
        *   Place an azure (8) pixel one position *below* the green pixel.
        *   Place an orange (7) pixel one position *below* and one position to the *right* of the green pixel.
    *   If the green pixel was *not* placed (because the new location calculated in step 2 was out of bounds):
        *   Place an azure (8) pixel one position to the *left* of the *original* red pixel's location.
        *   Place an orange (7) pixel one position to the *right* of the *original* red pixel's location.

5.  Bounds: Do not place any pixels outside the bounds of the grid.

6.  Output: The output grid should contain only the placed pixels (green, gray, azure, orange) with all other cells being black (0).
"""

import numpy as np

def find_red_pixel(grid):
    # Find the coordinates of the red (2) pixel
    red_indices = np.where(grid == 2)
    if len(red_indices[0]) > 0:
        return (red_indices[0][0], red_indices[1][0])
    else:
        return None

def transform(input_grid):
    # Initialize output_grid as all zeros
    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    # Find the red pixel in the input grid
    red_pixel_coords = find_red_pixel(input_grid)

    if red_pixel_coords is None:
        return output_grid # Return empty grid if no red pixel

    # Calculate the new coordinates for the green pixel
    green_pixel_coords = (red_pixel_coords[0] - 1, red_pixel_coords[1] - 1)

    # Check if the new green pixel position is within the grid bounds
    if 0 <= green_pixel_coords[0] < rows and 0 <= green_pixel_coords[1] < cols:
        # Place the green pixel
        output_grid[green_pixel_coords[0], green_pixel_coords[1]] = 3

        # Add gray pixel (one above green)
        gray_coords = (green_pixel_coords[0] - 1, green_pixel_coords[1])
        if 0 <= gray_coords[0] < rows and 0 <= gray_coords[1] < cols:
            output_grid[gray_coords] = 6

        # Add azure pixel (one below green)
        azure_coords = (green_pixel_coords[0] + 1, green_pixel_coords[1])
        if 0 <= azure_coords[0] < rows and 0 <= azure_coords[1] < cols:
            output_grid[azure_coords] = 8

        # Add orange pixel (one below and one right of green)
        orange_coords = (green_pixel_coords[0] + 1, green_pixel_coords[1] + 1)
        if 0 <= orange_coords[0] < rows and 0 <= orange_coords[1] < cols:
            output_grid[orange_coords] = 7

    else:
        # Add azure and orange based on original red position
        azure_coords = (red_pixel_coords[0], red_pixel_coords[1] - 1)  # Left of red
        orange_coords = (red_pixel_coords[0], red_pixel_coords[1] + 1) # Right of red

        if 0 <= azure_coords[0] < rows and 0 <= azure_coords[1] < cols:
            output_grid[azure_coords] = 8
        if 0 <= orange_coords[0] < rows and 0 <= orange_coords[1] < cols:
            output_grid[orange_coords] = 7

    return output_grid
```
