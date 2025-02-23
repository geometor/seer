# 1-3aa6fb7a • 004 • refine_coder

---
```python
"""
For each azure pixel in the input grid, check its immediate horizontal neighbors (left and right).
If a neighbor is white (0), change it to blue (1). Do not change vertically or diagonally adjacent cells.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels (0) horizontally adjacent to azure pixels (8) to blue (1).
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape

    # Iterate through each cell of the input_grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:  # Check if the current cell is azure (8)
                # Check to the immediate right
                if c + 1 < cols and input_grid[r, c + 1] == 0:
                    output_grid[r, c + 1] = 1  # Change adjacent white pixel to blue
                # Check to the immedate left
                if c - 1 >= 0 and input_grid[r, c - 1] == 0:
                    output_grid[r, c - 1] = 1  # Change adjacent white pixel to blue

    return output_grid
```

