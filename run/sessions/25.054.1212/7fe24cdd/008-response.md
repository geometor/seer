# 7fe24cdd • 008 • example_2 • investigate_coder

---
```python
"""
The input grid is replicated four times to create a 6x6 output grid. Each 3x3 quadrant of the output grid is either a direct copy or a mirrored version of the input grid:

1. Top-Left Quadrant: Exact copy of the input grid.
2. Top-Right Quadrant: Mirrored copy (reflection across the vertical axis) of the input grid.
3. Bottom-Left Quadrant: Mirrored copy (reflection across the horizontal axis) of the input grid.
4. Bottom-Right Quadrant: Double-mirrored copy (reflection across both axes, or 180-degree rotation) of the input grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 6x6 array filled with zeros.
    output_grid = np.zeros((6, 6), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Fill the top-left quadrant (direct copy).
    output_grid[:rows, :cols] = input_grid

    # Fill the top-right quadrant (horizontal mirror).
    output_grid[:rows, cols:] = np.fliplr(input_grid)

    # Fill the bottom-left quadrant (vertical mirror).
    output_grid[rows:, :cols] = np.flipud(input_grid)

    # Fill the bottom-right quadrant (double mirror/rotation).
    output_grid[rows:, cols:] = np.rot90(input_grid, 2)

    return output_grid
```
