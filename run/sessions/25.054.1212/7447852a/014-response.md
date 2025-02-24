# 7447852a • 014 • example_3 • investigate_coder

---
```python
"""
Copies the input grid and changes the color of red pixels to yellow if they are not part of any 3x3 square, using only red pixels as corners.
"""

import numpy as np

def get_potential_squares_corners(grid):
    red_pixels = []
    potential_squares_corners = []
    height, width = grid.shape
    for r in range(height):
        for c in range(width):
            if grid[r,c] == 2:
                red_pixels.append((r,c))

    for r in range(height - 2):
        for c in range(width - 2):
            if grid[r, c] == 2 and grid[r + 2, c] == 2 and grid[r, c + 2] == 2 and grid[r + 2, c + 2] == 2:
              potential_squares_corners.append([(r,c), (r+2, c), (r, c+2), (r+2, c+2)])
    return potential_squares_corners

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # Get potential 3x3 squares
    potential_squares_corners = get_potential_squares_corners(input_grid)
    
    red_pixels_to_change = []
    for r in range(height):
        for c in range(width):
            if input_grid[r, c] == 2:
                is_corner = False
                for square in potential_squares_corners:
                    if (r,c) in square:
                        is_corner = True
                        break
                if not is_corner:
                    red_pixels_to_change.append((r,c))


    # Change color to the identified red pixels.
    for r, c in red_pixels_to_change:
        output_grid[r, c] = 4
    
    return output_grid
```
