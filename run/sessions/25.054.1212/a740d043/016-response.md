# a740d043 • 016 • refine_coder

---
```python
"""
The transformation rule is to "crop" the input grid by removing the outer "frame" of the dominant color. The frame consists of contiguous blocks of the dominant color starting from the edges and extending inwards until a different color is encountered.
"""

import numpy as np

def get_dominant_border_color(grid):
    """Finds the most frequent color on the border of the grid."""
    border_pixels = np.concatenate([
        grid[0, :], grid[-1, :], grid[:, 0], grid[:, -1]
    ])
    unique, counts = np.unique(border_pixels, return_counts=True)
    dominant_color = unique[np.argmax(counts)]
    return dominant_color

def find_inner_region_bounds(grid, dominant_color):
    """Finds the row and column indices that define the inner region after removing the border frame."""
    rows, cols = grid.shape

    min_row, max_row = 0, rows - 1
    min_col, max_col = 0, cols - 1

    # Find top boundary
    for r in range(rows):
        if any(grid[r, :] != dominant_color):
            min_row = r
            break

    # Find bottom boundary
    for r in range(rows - 1, -1, -1):
        if any(grid[r, :] != dominant_color):
            max_row = r
            break

    # Find left boundary
    for c in range(cols):
        if any(grid[:, c] != dominant_color):
            min_col = c
            break

    # Find right boundary
    for c in range(cols - 1, -1, -1):
        if any(grid[:, c] != dominant_color):
            max_col = c
            break

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    """
    Extracts the internal region of the input grid by removing the border of the dominant color.
    The border is defined as contiguous blocks of the dominant color starting from edges.
    """
    # Convert input_grid to numpy array
    grid = np.array(input_grid)

    # Find the dominant color on the border
    dominant_color = get_dominant_border_color(grid)

    # Find the bounding box of the internal region
    min_row, max_row, min_col, max_col = find_inner_region_bounds(grid, dominant_color)

    # Extract the internal region
    output_grid = grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
