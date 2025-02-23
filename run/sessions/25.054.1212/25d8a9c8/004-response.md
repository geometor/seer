# 25d8a9c8 • 004 • refine_coder

---
```python
"""
The transformation rule performs a color replacement based on the following mapping:

1. Yellow (4) in the input becomes gray (5) in the output.
2. Red (2) or Green (3) in the input becomes white (0) in the output.
3. Maroon (9) becomes gray (5).
4. Blue (1) remains blue (1).
5. Gray (6) becomes Gray (5)
6. Orange (7) remains orange (7).

"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color transformation rules.
            if input_grid[i, j] == 4:
                output_grid[i, j] = 5
            elif input_grid[i, j] == 2 or input_grid[i, j] == 3:
                output_grid[i, j] = 0
            elif input_grid[i,j] == 9:
                output_grid[i,j] = 5
            elif input_grid[i,j] == 6:
                output_grid[i,j] = 5


    return output_grid
```

