# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
The transformation rule is: A green (3) pixel changes to yellow (4) if and only if there exists at least one other green pixel directly above or below it AND at least one other green pixel directly to its left or right.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid according to the specified rule.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Helper function to check for adjacent green pixels
    def has_adjacent_greens(r, c):
        has_vertical = False
        has_horizontal = False

        # Check vertical neighbors
        if r > 0 and input_grid[r-1][c] == 3:
            has_vertical = True
        if r < rows - 1 and input_grid[r+1][c] == 3:
            has_vertical = True

        # Check horizontal neighbors
        if c > 0 and input_grid[r][c-1] == 3:
            has_horizontal = True
        if c < cols - 1 and input_grid[r][c+1] == 3:
            has_horizontal = True
            
        return has_vertical and has_horizontal

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is green
            if input_grid[r][c] == 3:
                # Check for adjacent green pixels and change color if necessary
                if has_adjacent_greens(r, c):
                    output_grid[r][c] = 4

    return output_grid
```
