# 3-1e0a9b12 • 008 • refine_code - CODE

---
```python
"""
The transformation rule is as follows:
1. Identify Non-White Cells: Examine each column in the input grid to find cells that are not white (color code 0).
2. Record and Preserve: For each column, as soon as a non-white cell is found, record its color. It is only the first non-white cell for each column.
3. Translate to last row: move the set of recorded colors to the last row of the output grid. The order of colors in a column are maintained.
4. Clear other rows: Set all cells in the rows above to be white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize the output grid as all white (0).
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column of the input grid.
    for j in range(input_grid.shape[1]):
        # Find the first non-white cell in the current column.
        for i in range(input_grid.shape[0]):
            if input_grid[i, j] != 0:
                # Place the color of the non-white cell in the last row of the output grid.
                output_grid[-1, j] = input_grid[i, j]
                break  # Stop after finding the first non-white cell

    return output_grid
```

