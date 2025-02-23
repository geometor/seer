# 1e32b0e9 • 018 • refine_coder

---
```python
"""
The transformation rule identifies cells of color blue. The blue color expands in all eight directions (including diagonals) until it reaches a cell of any color other than black (0) or the edge of the grid. The expansion occurs one cell at a time, propagating outwards from the original blue cells.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding blue color outwards.
    """
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find initial blue cells
    blue_cells = [(r, c) for r in range(rows) for c in range(cols) if input_grid[r, c] == 1]

    # Propagate blue color
    queue = blue_cells.copy()
    while queue:
        r, c = queue.pop(0)

        # Iterate over all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r + dr, c + dc

                # Check bounds and if the neighbor is black (0)
                if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr, nc] == 0:
                    output_grid[nr, nc] = 1
                    queue.append((nr, nc))

    return output_grid
```
