# a9f96cdd • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Initialization:** Start with an input grid of dimensions 3x5.
2.  **Locate:** Note the red pixel (value 2) in the top row at position (0,2).
3.  **Transformation**: Create azure colored pixel with value 8 and orange colored pixel with value 7 in the second row of the output grid. Azure is one row down and one column to the left and orange is one row down and one column to the right, relative to the input red pixel.
4. **Output:** maintain original grid size and all the white pixels.
"""

import numpy as np

def find_pixel_by_value(grid, value):
    # Find the coordinates of a pixel with a specific value.
    coords = np.where(grid == value)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return the first occurrence
    return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the red pixel (value 2).
    red_pixel_coords = find_pixel_by_value(input_grid, 2)

    if red_pixel_coords:
        # Calculate coordinates for the azure and orange pixels.
        azure_coords = (red_pixel_coords[0] + 1, red_pixel_coords[1] - 1)
        orange_coords = (red_pixel_coords[0] + 1, red_pixel_coords[1] + 1)

        # Set the azure and orange pixels in the output grid,
        # checking bounds.
        if 0 <= azure_coords[0] < output_grid.shape[0] and 0 <= azure_coords[1] < output_grid.shape[1]:
            output_grid[azure_coords] = 8
        if 0 <= orange_coords[0] < output_grid.shape[0] and 0 <= orange_coords[1] < output_grid.shape[1]:
             output_grid[orange_coords] = 7

    return output_grid
```
