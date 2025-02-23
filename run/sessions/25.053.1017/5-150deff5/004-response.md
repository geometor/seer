# 5-150deff5 • 004 • example_2 - CODE

---
```python
"""
1.  **Identify the Input:** The input is a grid of pixels, primarily containing white (0) and gray (5) pixels.
2.  **Locate Gray Pixels:** Identify all pixels with the color gray (5).
3. **Determine the adjacent pixels:** For each gray pixel look at the directly adjacent pixels - do not include diagonals.
4.  **Apply Color Substitution Rules:**
    *   If a gray (5) pixel is adjacent to at least one white (0) pixel, change its color to azure (8) in the output grid.
    *   If the Gray(5) pixel has no adjacent white(0) pixels, change its color to red(2).
5.  **Maintain Other Pixels:** All white (0) pixels in the input grid remain white (0) in the output grid.
6.  **Output:** The output is a grid of the same dimensions as the input, with the gray pixels replaced according to the adjacency rule and all other pixels are the same.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets the values of adjacent pixels, excluding diagonals."""
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append(grid[row-1, col])  # Up
    if row < rows - 1:
        adjacent.append(grid[row+1, col])  # Down
    if col > 0:
        adjacent.append(grid[row, col-1])  # Left
    if col < cols - 1:
        adjacent.append(grid[row, col+1])  # Right
    return adjacent

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the input grid
    for row in range(rows):
        for col in range(cols):
            # Locate Gray Pixels
            if input_grid[row, col] == 5:
                # Determine adjacent pixels
                adjacent_values = get_adjacent_pixels(input_grid, row, col)
                # Apply Color Substitution Rules
                if 0 in adjacent_values:
                    output_grid[row, col] = 8  # Change to azure
                else:
                    output_grid[row, col] = 2  # Change to red

    # Maintain Other Pixels (0 remains 0, already handled by initialization)
    return output_grid
```
