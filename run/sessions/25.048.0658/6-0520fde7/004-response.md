# 6-0520fde7 • 004 • Response

---

*text:*

```python
"""
This transformation identifies patterns of non-white pixels in the input grid.
It locates all 3x3 subgrids and identifies those that contain exactly three non-zero cells.
If 3x3 subgrid contains exactly 3 non-zero cells, those are mapped to output grid with color red(2).
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to numpy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through each cell of the input grid as a potential top-left corner of a 3x3 subgrid
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Extract the 3x3 subgrid
            subgrid = input_grid[r:r+3, c:c+3]

            # Count non-zero pixels in the subgrid
            non_zero_count = np.count_nonzero(subgrid)

            # Check the condition: exactly three non-zero pixels
            if non_zero_count == 3:
              for i in range(3):
                for j in range(3):
                  if subgrid[i,j] != 0:
                    output_grid[i, j] = 2

    return output_grid
```

