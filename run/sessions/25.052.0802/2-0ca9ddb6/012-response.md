# 2-0ca9ddb6 • 012 • refine_code - CODE

---
```python
"""
The transformation rule identifies single-cell objects of color red (2) and blue (1). It then modifies the grid around these cells: red cells are surrounded by a diamond of yellow (4) cells, and blue cells are replaced by an orange (7) cell and surrounded by a plus sign (+) of orange cells. Other single-cell objects, such as magenta (6), are left unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules for single-cell red and blue objects.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid

    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Process red (2) cells
            if input_grid[i, j] == 2:
                # Add yellow (4) cells diagonally
                if i > 0 and j > 0:
                    output_grid[i - 1, j - 1] = 4
                if i > 0 and j < input_grid.shape[1] - 1:
                    output_grid[i - 1, j + 1] = 4
                if i < input_grid.shape[0] - 1 and j > 0:
                    output_grid[i + 1, j - 1] = 4
                if i < input_grid.shape[0] - 1 and j < input_grid.shape[1] - 1:
                    output_grid[i + 1, j + 1] = 4

            # Process blue (1) cells
            elif input_grid[i, j] == 1:
                # Replace the blue cell with an orange (7) cell
                output_grid[i, j] = 7
                # Add orange (7) cells in a plus shape
                if i > 0:
                    output_grid[i - 1, j] = 7
                if j > 0:
                    output_grid[i, j - 1] = 7
                if j < input_grid.shape[1] - 1:
                    output_grid[i, j + 1] = 7
                if i < input_grid.shape[0] - 1:
                    output_grid[i + 1, j] = 7

    return output_grid
```

