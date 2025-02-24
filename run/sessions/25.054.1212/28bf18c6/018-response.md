# 28bf18c6 • 018 • refine_coder

---
```python
"""
The output grid is formed by taking the top-left 3x6 subgrid of the
input, then setting to 0 any cell which does not appear at least once
in its color's respective 4x4 subgrid in the full 8x8 input.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 6), dtype=int)

    # Extract the 3x6 subgrid
    subgrid_3x6 = input_grid[:3, :6]

    # Iterate through the 3x6 subgrid
    for i in range(3):
        for j in range(6):
            current_color = subgrid_3x6[i, j]
            output_grid[i,j] = current_color

            # Iterate over all 4x4 sub-grids in the 8x8 grid
            color_found = False
            for row_start in range(0, 5):  # 8 - 4 + 1 = 5
                for col_start in range(0, 5):
                    subgrid_4x4 = input_grid[row_start:row_start+4, col_start:col_start+4]
                    if current_color in subgrid_4x4:
                        color_found = True
                        break # Exit search in 4x4 subgrids
                if color_found:
                  break

            if not color_found:
               output_grid[i, j] = 0

    return output_grid
```
