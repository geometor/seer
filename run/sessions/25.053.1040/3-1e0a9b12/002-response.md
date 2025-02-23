# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Non-Zero Pixels:** Find all pixels in the input grid that have a value other than 0.

2.  **Preserve Order:** Maintain these non-zero pixels in the order they appear in the input reading from top-left, to bottom-right, left to right in each row, and top to bottom by rows.

3.  **Place to last row** Place the ordered non-zero pixels in the last row of the output grid, starting from the leftmost cell and filling towards the right.

4. **Fill Remaining**: Fill the remaining cells in the output grid (those not occupied by the rearranged non-zero pixels) with 0.
"""

import numpy as np

def get_nonzero_pixels(grid):
    """
    Extracts non-zero pixels from the grid, preserving their original order.
    """
    rows, cols = grid.shape
    nonzero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                nonzero_pixels.append(grid[r, c])
    return nonzero_pixels


def transform(input_grid):
    # Initialize output grid with zeros, same size as input
    output_grid = np.zeros_like(input_grid)

    # Get non-zero pixels
    nonzero_pixels = get_nonzero_pixels(input_grid)
    
    # get number of rows in grid
    num_rows = output_grid.shape[0]

    # Place non-zero pixels in the last row of the output grid
    for i, pixel_value in enumerate(nonzero_pixels):
        output_grid[num_rows - 1, i] = pixel_value

    return output_grid
```
