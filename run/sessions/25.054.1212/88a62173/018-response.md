# 88a62173 • 018 • refine_coder

---
```python
"""
The input grid is divided into four quadrants. Each quadrant corresponds to a pixel in the 2x2 output grid. The color of each output pixel is determined by the most frequent color within its corresponding input quadrant.
"""

import numpy as np
from collections import Counter

def get_quadrant(grid, row_start, row_end, col_start, col_end):
    """Helper function to extract a quadrant from the grid."""
    return grid[row_start:row_end, col_start:col_end]

def get_most_frequent_color(grid):
    """
    Helper function to get the most frequent color in a grid.
    Returns the color.  Does *not* handle tie-breaking.
    """
    counts = Counter(grid.flatten())
    most_common = counts.most_common(1)  # Get the single most common
    if most_common:
        return most_common[0][0]
    else:
        return 0  # Default to 0 if the quadrant is empty


def transform(input_grid):
    # initialize output_grid as 2x2 numpy array with zeros
    output_grid = np.zeros((2, 2), dtype=int)

    # get input grid dimensions
    rows, cols = input_grid.shape

    # calculate midpoints for quadrant division
    row_mid = (rows + 1) // 2  # Integer division, rounding up for center
    col_mid = (cols + 1) // 2

    # Process each quadrant
    quadrants = [
        (0, row_mid, 0, col_mid),          # Top-left
        (0, row_mid, col_mid, cols),       # Top-right
        (row_mid, rows, 0, col_mid),       # Bottom-left
        (row_mid, rows, col_mid, cols)  # Bottom-right
    ]

    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = get_quadrant(input_grid, row_start, row_end, col_start, col_end)
        # Determine the most frequent color in the quadrant
        most_frequent = get_most_frequent_color(quadrant)
        # Assign to the corresponding output pixel
        output_grid[i // 2, i % 2] = most_frequent

    return output_grid
```

