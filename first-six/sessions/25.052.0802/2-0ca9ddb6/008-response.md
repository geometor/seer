# 2-0ca9ddb6 • 008 • refine_code - CODE

---
```python
"""
The transformation rule identifies single-cell objects of colors red (2), blue (1), and magenta (6).  Red cells (2) are preserved, and yellow (4) cells are placed diagonally adjacent to them (NW, NE, SW, SE), forming an 'x' pattern. Blue cells (1) are transformed to orange(7), and orange (7) cells are placed orthogonally adjacent to them (up, down, left, right), forming a '+' pattern. Magenta cells (6) are preserved without modification. Grid boundaries are respected, preventing out-of-bounds placements.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate through the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check for the red cell (color 2)
            if input_grid[i, j] == 2:
                # Place yellow cells (color 4) diagonally
                if i > 0 and j > 0:
                    output_grid[i - 1, j - 1] = 4
                if i > 0 and j < input_grid.shape[1] - 1:
                    output_grid[i - 1, j + 1] = 4
                if i < input_grid.shape[0] - 1 and j > 0:
                    output_grid[i + 1, j - 1] = 4
                if i < input_grid.shape[0] - 1 and j < input_grid.shape[1] - 1:
                    output_grid[i + 1, j + 1] = 4

            # Check for the blue cell (color 1)
            elif input_grid[i, j] == 1:
                # change the blue cell to orange
                output_grid[i, j] = 7
                # Place orange cells (color 7) orthogonally adjacent
                if i > 0:
                    output_grid[i - 1, j] = 7
                if j > 0:
                    output_grid[i, j - 1] = 7
                if j < input_grid.shape[1] - 1:
                    output_grid[i, j + 1] = 7
                if i < input_grid.shape[0] - 1:
                    output_grid[i + 1, j] = 7

    return output_grid
```

