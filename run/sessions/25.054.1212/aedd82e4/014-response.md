# aedd82e4 • 014 • example_3 • investigate_coder

---
```python
"""
Detects all instances of four adjacent red cells in a square, then transforms the red pixel at the lower-right of the square to blue.
"""

import numpy as np

def find_2x2_squares(grid, color):
    """Finds all 2x2 squares of the specified color."""
    rows, cols = grid.shape
    squares = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i, j] == color and
                grid[i + 1, j] == color and
                grid[i, j + 1] == color and
                grid[i + 1, j + 1] == color):
                squares.append((i, j))
    return squares

def transform(input_grid):
    """
    Transforms the input grid by changing the color of the lower-right pixel
    of each 2x2 red square from red to blue.
    """
    output_grid = np.copy(input_grid)
    red_squares = find_2x2_squares(output_grid, 2)

    # Change the color of the lower-right pixel of each identified square
    for i, j in red_squares:
        output_grid[i + 1, j + 1] = 1

    return output_grid
```
