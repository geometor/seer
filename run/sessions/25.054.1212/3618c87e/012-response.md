# 3618c87e • 012 • refine_coder

---
```python
"""
1.  **Copy Input:** Begin with an output grid that's a copy of the input grid.

2.  **Identify Columns:** Examine the bottom row of the *input* grid. If a pixel is gray (5), mark its column as "active".

3.  **Conditional Swap:** For each "active" column in the *input* grid:
    *   Iterate upwards from the second-to-last row to the top row.
    *   If a pixel is blue (1), change the corresponding pixel in the *output* grid to gray (5).
    *   If a pixel is gray (5), change the corresponding pixel in the *output* grid to blue (1).

4. **Bottom Row Modification:**
    * In the *input* grid, in an active column, if there were *any* blue (1) or gray (5) pixels *above* the bottom row, change the corresponding pixel in the *output* grid's bottom row to blue (1). Otherwise the bottom row pixel in the output grid stays gray (5).

5.  **Preservation:** All other pixels, not involved in the operations above, remain unchanged in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify active columns (where the bottom row is gray)
    active_columns = [j for j in range(cols) if input_grid[-1, j] == 5]

    # Conditional Swap and Bottom Row Modification
    for j in active_columns:
        # Conditional Swap (iterating upwards)
        for i in range(rows - 2, -1, -1):
            if input_grid[i, j] == 1:  # If blue
                output_grid[i, j] = 5  # Change to gray
            elif input_grid[i, j] == 5:  # If gray
                output_grid[i, j] = 1  # Change to blue

        # Bottom Row Modification
        if any(input_grid[i, j] in (1, 5) for i in range(rows - 1)):
            output_grid[-1, j] = 1

    return output_grid
```
