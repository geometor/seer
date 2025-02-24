# 7447852a • 018 • refine_coder

---
```python
"""
Copies the input grid and changes the color of red pixels to yellow if they are not part of any 3x3 square's corners, where a square is defined by having red or yellow corners.
"""

import numpy as np

def is_valid_square(grid, r, c):
    """Checks if a 3x3 square centered at (r, c) has red or yellow corners."""
    height, width = grid.shape
    corners = [
        (r - 1, c - 1), (r - 1, c + 1),
        (r + 1, c - 1), (r + 1, c + 1)
    ]
    for cr, cc in corners:
        if not (0 <= cr < height and 0 <= cc < width):
            return False  # Out of bounds
        if grid[cr, cc] not in (2, 4):
            return False  # Not a red or yellow corner
    return True

def is_corner_of_square(grid, r, c):
    """Checks if the pixel at (r,c) is a corner of ANY valid 3x3 squares."""
    height, width = grid.shape

    # Check all possible 3x3 squares that could have (r,c) as a corner
    for center_r in range(r - 1, r + 2):
        for center_c in range(c - 1, c + 2):
            if is_valid_square(grid, center_r, center_c):
                return True # Found square
    return False

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    red_pixels_to_change = []

    for r in range(height):
        for c in range(width):
            if input_grid[r, c] == 2:
                # Check if it's part of any 3x3 square's corner
                if not is_corner_of_square(input_grid, r, c):
                    red_pixels_to_change.append((r, c))

    # Change color to the identified red pixels.
    for r, c in red_pixels_to_change:
        output_grid[r, c] = 4

    return output_grid
```
