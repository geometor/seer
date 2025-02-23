# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
Iterates through each pixel in the input grid.
Identifies green (3) pixels.
For each green pixel, checks for adjacency with other green pixels:
    Checks if there is a green pixel directly above AND directly below.
    Checks if there is a green pixel directly to the left AND directly to the right.
If either of the adjacency conditions is true, changes the pixel's color to yellow (4).
Returns the modified grid.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets the values of adjacent pixels (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = {}
    if row > 0:
        adjacent['up'] = grid[row - 1, col]
    if row < rows - 1:
        adjacent['down'] = grid[row + 1, col]
    if col > 0:
        adjacent['left'] = grid[row, col - 1]
    if col < cols - 1:
        adjacent['right'] = grid[row, col + 1]
    return adjacent

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each pixel in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current pixel is green (3)
            if output_grid[row, col] == 3:
                # Get adjacent pixel values
                adjacent = get_adjacent_pixels(output_grid, row, col)

                # Check adjacency conditions and change color to yellow (4) if met
                if adjacent.get('up') == 3 and adjacent.get('down') == 3:
                    output_grid[row, col] = 4
                elif adjacent.get('left') == 3 and adjacent.get('right') == 3:
                    output_grid[row, col] = 4

    return output_grid
```
