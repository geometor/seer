# f35d900a • 011 • refine_coder

---
```python
"""
1.  **Identify Key Pixels:** Find all pixels in the input grid that are not black (0) and are isolated, i.e., not part of a larger object of the same color.
2.  **Generate Rectangles:** For each key pixel:
    *   Create a 3x3 rectangle of the same color in the output grid. The center of this rectangle will be one row *below* the position of the key pixel in the input grid.
    *   Change the central pixel of each rectangle to color gray (5).
3. All other pixels should be black.
"""

import numpy as np

def find_isolated_pixels(grid):
    """Finds isolated pixels of a given color."""
    isolated_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                neighbors = []
                # Check adjacent cells (up, down, left, right)
                if r > 0: neighbors.append(grid[r-1, c])
                if r < rows - 1: neighbors.append(grid[r+1, c])
                if c > 0: neighbors.append(grid[r, c-1])
                if c < cols - 1: neighbors.append(grid[r, c+1])

                if all(neighbor == 0 or neighbor != grid[r,c] for neighbor in neighbors):
                    isolated_pixels.append(((r, c), grid[r, c]))
    return isolated_pixels

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.zeros_like(input_grid)
    isolated_pixels = find_isolated_pixels(input_grid)

    for (row, col), color in isolated_pixels:
        # Generate 3x3 rectangle, centered one row below
        center_row = row + 1
        center_col = col

        for r in range(center_row - 1, center_row + 2):
            for c in range(center_col - 1, center_col + 2):
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = color

        # change center to gray
        if 0 <= center_row < output_grid.shape[0] and 0 <= center_col < output_grid.shape[1]:
           output_grid[center_row, center_col] = 5

    return output_grid
```
