# 5-150deff5 • 002 • example_1 - CODE

---
```python
"""
Identifies a gray (5) object in the input grid and segments it into two regions. The region with pixels to the left of the input region's average x coordinate is colored azure (8), while the region with pixels right are colored red (2). The rest of the grid (background) remains unchanged.
"""

import numpy as np

def get_object_pixels(grid, color):
    # returns a list of (x,y) coordinates that correspond to the specified color
    return [(x,y) for x,row in enumerate(grid) for y, pixel in enumerate(row) if pixel == color]

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # 1. Identify the Input Shape:
    gray_pixels = get_object_pixels(input_grid, 5)
        
    if not gray_pixels:
       return output_grid

    # 2. Segment the Shape:
    # Calculate the average x coordinate.
    x_coords = [x for x, _ in gray_pixels]
    avg_x = sum(x_coords) / len(x_coords)

    # Divide based on x coordinate.
    first_area = [(x, y) for x, y in gray_pixels if x <= avg_x]
    second_area = [(x, y) for x, y in gray_pixels if x > avg_x ]

    # 3. Color the Regions:
    for x, y in first_area:
      output_grid[x][y] = 8  # Azure
    for x, y in second_area:
      output_grid[x][y] = 2  # Red

    # 4. Preserve Background (already handled by copying the input grid).
    return output_grid
```
