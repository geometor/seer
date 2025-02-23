# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
1.  **Identify** all pixels with the value 3 (green).
2.  **Locate** the green pixels that have exactly two green neighbors, where neighbors may be above, below, to the left, or to the right - no diagonals.
3. **Change** the value/color for only the identified pixels in the previous step to 4 (yellow).
4.  All other pixels remain **unchanged**.
"""

import numpy as np

def count_neighbors(grid, r, c, target_color):
    """Counts the number of neighbors with the target color around a pixel."""
    rows, cols = grid.shape
    count = 0
    # Check above
    if r > 0 and grid[r-1, c] == target_color:
        count += 1
    # Check below
    if r < rows - 1 and grid[r+1, c] == target_color:
        count += 1
    # Check left
    if c > 0 and grid[r, c-1] == target_color:
        count += 1
    # Check right
    if c < cols - 1 and grid[r, c+1] == target_color:
        count += 1
    return count

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is green
            if input_grid[r, c] == 3:
                # Count green neighbors
                neighbor_count = count_neighbors(input_grid, r, c, 3)
                # Change color to yellow if exactly two green neighbors
                if neighbor_count == 2:
                    output_grid[r, c] = 4

    return output_grid
```
