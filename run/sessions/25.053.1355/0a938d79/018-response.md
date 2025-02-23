# 0a938d79 • 018 • example_3 - CODE

---
```python
"""
1.  **Identify Colored Pixels:** Locate all non-white (non-zero) pixels in the input grid.
2.  **Horizontal Replication:** For each colored pixel:
    *   Replace all white pixels in the same row with the color of the identified pixel.
3. **Pattern Replication:**
   *  Starting with each original colored pixel row.
   *  alternating below, fill the rows with the same color as the original pixel row.
"""

import numpy as np

def get_colored_pixels(grid):
    """Finds the coordinates and colors of non-white pixels."""
    colored_pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel != 0:
                colored_pixels.append(((row_idx, col_idx), pixel))
    return colored_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Find colored pixels
    colored_pixels = get_colored_pixels(input_grid)

    # Horizontal Replication and pattern creation
    for (row, col), color in colored_pixels:
        # Fill the original row
        output_grid[row, :] = color

        # alternate the filled rows
        offset = 1
        while row + offset < output_grid.shape[0]:
          output_grid[row+offset,:] = color
          offset += 2
    
    return output_grid
```
