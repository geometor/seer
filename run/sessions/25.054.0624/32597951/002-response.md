# 32597951 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify the Azure Region:** Locate all azure (8) pixels within the input grid. This forms the "region of interest."

2.  **Vertical Bounds:** Find the minimum and maximum row indices of the azure colored region.

3.  **Conditional Color Change:** Iterate through all the blue pixels (1). If a blue pixel is *adjacent* (horizontally, vertically, or diagonally) to an azure pixel, AND is on a row where an azure pixel exists, change it to green (3).

4. **Preserve Other Pixels:** All other pixels in the grid retain their original colors.
"""

import numpy as np

def get_azure_region(grid):
    """Finds the coordinates of all azure (8) pixels."""
    return np.argwhere(grid == 8)

def get_vertical_bounds(azure_region):
    """Determines the minimum and maximum row indices of the azure region."""
    rows = azure_region[:, 0]
    return np.min(rows), np.max(rows)

def is_adjacent(coord1, coord2):
    """Checks if two coordinates are adjacent (horizontally, vertically, or diagonally)."""
    return abs(coord1[0] - coord2[0]) <= 1 and abs(coord1[1] - coord2[1]) <= 1

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    azure_region = get_azure_region(input_grid)
    min_row, max_row = get_vertical_bounds(azure_region)

    # Iterate through all pixels
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 1:  # Check if it's a blue pixel
                is_adjacent_to_azure = False
                for azure_coord in azure_region:
                    if is_adjacent((r, c), azure_coord) and min_row <= r <= max_row: #check within vertical boundary
                        is_adjacent_to_azure = True
                        break
                if is_adjacent_to_azure:
                    output_grid[r, c] = 3  # Change to green

    return output_grid
```
