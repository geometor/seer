# 4c4377d9 • 002 • example_1 • investigate_coder

---
```python
"""
1. **Initialization:** Start with the input grid (3x4).
2. **Duplication:** Duplicate the input grid vertically once to double the height, result is a 6x4 grid.
3. **Alteration:**
    Starting from the original top row, which remains untouched:
    * The original second line is moved at the bottom of the grid
    * The original thord line, swap color 5 with 9 and color 9 with 5
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid by duplicating the input grid
    output_grid = np.concatenate((input_grid, input_grid), axis=0)

    # Move the original second row to the bottom.
    second_row = output_grid[1].copy()
    output_grid = np.delete(output_grid, 1, axis=0)
    output_grid = np.vstack([output_grid, second_row])

    # Swap 5s and 9s in the original third row (now the fourth row).
    third_row_index = 3 # Index 2 of the 2nd duplicated block, is now at index 3
    for i in range(output_grid.shape[1]):
        if output_grid[third_row_index, i] == 5:
            output_grid[third_row_index, i] = 9
        elif output_grid[third_row_index, i] == 9:
            output_grid[third_row_index, i] = 5

    return output_grid
```
