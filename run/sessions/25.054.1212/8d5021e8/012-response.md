# 8d5021e8 • 012 • refine_coder

---
```python
"""
1. Expand Grid: The output grid's height is three times the input grid's height, and the output grid's width is two times the input grid's width.

2. Column Mirroring with Repetition:
    *   The first column of the *input* grid is copied to the *second* and *fourth* columns of the output grid.
    *   The second column of the *input* grid is copied to the *first* and *third* columns of the output grid.

3. Vertical Repetition:** Steps 1 and 2 are applied to each set of three rows within output. The entire mirrored pattern is copied downwards, repeating it three times to achieve the tripled height.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with tripled height and doubled width
    output_height = input_grid.shape[0] * 3
    output_width = input_grid.shape[1] * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Mirror and repeat
    for i in range(3):  # Repeat the pattern three times vertically
        # Copy the input columns to the output, mirrored as per the refined rule
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 1] = input_grid[:, 0]  # Input col 0 to output col 1
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 3] = input_grid[:, 0]  # Input col 0 to output col 3
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 0] = input_grid[:, 1]  # Input col 1 to output col 0
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 2] = input_grid[:, 1]  # Input col 1 to output col 2

    return output_grid
```
