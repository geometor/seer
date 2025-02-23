# 1b2d62fb • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Key Element:** Locate all blue (1) pixels within the input grid.
2.  **Reduce Dimensions:** Create an output grid of size 5x3. Initialize all the pixels in the output grid to be colored white (0).
3.  **Map and Transform:** For each blue pixel in the input grid, calculate it's x position as `x // 2`, and then calculate it's y position using `y // 2`. Transform the corresponding pixel in the output grid at calculated (x, y) coordinates to azure (8). Note, `//` is integer division.
4. **Output Result** Output the new grid.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    return np.argwhere(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((5, 3), dtype=int)  # Initialize 5x3 output grid with white (0)

    blue_pixels = find_pixels_by_color(input_grid, 1)  # Find blue pixels

    for row, col in blue_pixels:
        new_row = row
        new_col = col // 2
        if 0 <= new_row < 5 and 0<= new_col < 3:
            output_grid[new_row, new_col] = 8 #set to azure

    return output_grid
```
