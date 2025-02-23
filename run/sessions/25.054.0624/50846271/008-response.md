# 50846271 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Red Objects:** Locate all red (value 2) pixels within the input grid. Consider contiguous regions of red pixels as single objects.

2.  **Identify Target Gray Pixels:** Find gray (value 5) pixels that are cardinally adjacent (up, down, left, or right, *not* diagonally) to any red pixel.

3.  **Conditional Color Change:** For each *gray* pixel from those found in step two, check the input grid. IF the *gray* pixel found in step 2 is gray, change it to azure (8) in the output grid.

4. **Preserve Other Pixels:** All other pixels in the input grid retain their original color in the output grid. In other words. If it is not a gray pixel next to a red pixel, as defined above, copy its value to the same coordinates in the output grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the cardinal neighbors of a pixel."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel
    for row in range(rows):
        for col in range(cols):
            # Find red pixels
            if input_grid[row, col] == 2:
                # Check cardinal neighbors
                neighbors = get_neighbors(input_grid, row, col)
                for n_row, n_col in neighbors:
                    # If neighbor is gray, change it to azure in output
                    if input_grid[n_row, n_col] == 5:
                        output_grid[n_row, n_col] = 8
    return output_grid
```
