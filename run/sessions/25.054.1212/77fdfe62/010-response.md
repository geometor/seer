# 77fdfe62 • 010 • refine_coder

---
```python
"""
Extract the four corner pixels of the input grid and create a 4x4 output grid where each quadrant is filled with the color of the corresponding corner pixel.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts corner pixels and creates a 4x4 output grid with quadrant filling.
    """
    # Get dimensions of the input grid.
    rows, cols = input_grid.shape

    # Determine output grid size.
    out_rows = min(rows // 2, 4)
    out_cols = min(cols // 2, 4)

    # Create output grid initialized with zeros.
    output_grid = np.zeros((out_rows, out_cols), dtype=int)

    # Extract corner pixels.
    top_left = input_grid[0, 0]
    top_right = input_grid[0, cols - 1]
    bottom_left = input_grid[rows - 1, 0]
    bottom_right = input_grid[rows - 1, cols - 1]

    # Fill quadrants.
    output_grid[:out_rows // 2, :out_cols // 2] = top_left
    output_grid[:out_rows // 2, out_cols // 2:] = top_right
    output_grid[out_rows // 2:, :out_cols // 2] = bottom_left
    output_grid[out_rows // 2:, out_cols // 2:] = bottom_right

    return output_grid
```

