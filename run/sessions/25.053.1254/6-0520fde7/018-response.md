# 6-0520fde7 • 018 • example_3 - CODE

---
```python
"""
The program transforms an input grid to an output grid based on the following rule:
1. Initialize an output grid of size 3x3, filled with white (0).
2. Iterate through each cell of the input grid.
3. If a cell in the input grid is blue (1), change the cell at the corresponding row and column divided by two in the output grid to red (2).
4. If a cell is not blue (1), ignore it.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the input grid.
    rows, cols = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            # If a cell is blue (1), change the corresponding cell in output_grid to red (2).
            if input_grid[i, j] == 1:
                output_grid[i // 2, j // 2] = 2

    return output_grid
```
