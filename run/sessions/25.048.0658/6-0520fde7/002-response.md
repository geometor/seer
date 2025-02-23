# 6-0520fde7 • 002 • Response

---

*text:*

```python
"""
The transformation identifies the centroid of the non-white pixels in the input grid.
It extracts the color of the pixel at the centroid's coordinates.
A 3x3 output grid is created, filled with white (0).
If the central pixel from the input is not white (0), the center cell (1, 1) of the output grid is colored red (2).
Otherwise, the center cell remains white (0).
"""

import numpy as np

def calculate_centroid(grid):
    # Collect coordinates of non-white cells
    non_white_coords = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                non_white_coords.append((r, c))

    # Return None if the is no non-white cells.
    if not non_white_coords:
      return None

    # Calculate the centroid
    centroid_row = sum([c[0] for c in non_white_coords]) / len(non_white_coords)
    centroid_col = sum([c[1] for c in non_white_coords]) / len(non_white_coords)

    return int(centroid_row), int(centroid_col)

def transform(input_grid):
    # Convert input_grid to numpy array
    input_grid = np.array(input_grid)

    # Calculate the centroid of non-white pixels
    centroid = calculate_centroid(input_grid)

    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # If the centroid is not None
    if centroid is not None:
      # Map the central pixel's color to the output grid
      central_pixel_value = input_grid[centroid]
      if central_pixel_value != 0:
          output_grid[1, 1] = 2  # Paint red

    return output_grid
```
