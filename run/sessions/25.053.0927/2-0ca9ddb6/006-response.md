# 2-0ca9ddb6 • 006 • example_3 - CODE

---
```python
"""
1.  Identify pixels with the colors red (2), blue(1) and magenta (6) in the input grid.
2.  Maintain all of the identified pixels in their original locations.
3.  For each pixel location that is directly adjacent (up, down, left, or right, but *not* diagonally) to a red (2) or blue (1) pixel, set the color to yellow (4) in the output grid, unless the location already contains, red(2), blue(1), or magenta(6).
4.  For each pixel location that is directly adjacent (up, down, left, or right, but *not* diagonally) to a blue (1) or magenta (6) pixel, set the color to orange (7) in the output grid, unless the location already contains, red(2), blue(1), or magenta(6).
5. All other pixels remain unchanged (color 0/white).
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    # returns the valid adjacent pixel indices
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent.append((row + 1, col))  # Down
    if col > 0:
        adjacent.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent.append((row, col + 1))  # Right
    return adjacent

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel
    for row in range(rows):
        for col in range(cols):
            # Identify red, blue and magenta pixels and perform actions based on adjacency.
            if input_grid[row, col] == 2 or input_grid[row,col] == 1:
                adjacent_coords = get_adjacent_pixels(input_grid, row, col)
                for r, c in adjacent_coords:
                    if input_grid[r,c] not in [1,2,6]:
                        output_grid[r, c] = 4  # Set adjacent to yellow

            if input_grid[row, col] == 1 or input_grid[row,col] == 6:
                adjacent_coords = get_adjacent_pixels(input_grid, row, col)
                for r, c in adjacent_coords:
                    if input_grid[r,c] not in [1,2,6]:
                        output_grid[r, c] = 7  # Set adjacent to orange
    return output_grid
```
