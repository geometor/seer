# 88a62173 • 008 • example_2 • investigate_coder

---
```python
"""
The input grid is condensed into a 2x2 output grid. Each cell in the output grid represents a quadrant of the input grid. If a quadrant in the input grid contains at least one blue (1) pixel, the corresponding output cell is blue (1). Otherwise, the output cell is white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid into a 2x2 output grid based on the presence of blue pixels in each quadrant.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2, 2), dtype=int)

    # Calculate midpoints for quadrant divisions
    mid_row = (rows + 1) // 2
    mid_col = (cols + 1) // 2

    # Define quadrant boundaries with overlap
    quadrants = [
        (0, mid_row, 0, mid_col),       # Top-left
        (0, mid_row, mid_col, cols),   # Top-right
        (mid_row, rows, 0, mid_col),       # Bottom-left
        (mid_row, rows, mid_col, cols)    # Bottom-right
    ]

    # Iterate through quadrants and check for blue pixels
    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = input_grid[row_start:row_end, col_start:col_end]
        if 1 in quadrant:  # Check if any blue pixel exists
            output_grid[i // 2, i % 2] = 1

    return output_grid.tolist()
```
