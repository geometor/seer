# 2dee498d • 004 • refine_coder

---
```python
"""
The transformation extracts the top-left subgrid from the input grid. The output grid's dimensions are determined by taking the minimum of the input grid's dimensions and 3. Specifically, the output grid's number of rows is the minimum of 3 and the number of rows in the input grid. Similarly, the output grid's number of columns is the minimum of 3 and the number of columns in the input grid. The values in the output grid are copied from the corresponding positions in the input grid, starting at position [0, 0]. If the input grid has less than 3 rows or columns, the smaller of the dimensions is applied.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the top-left subgrid, with dimensions capped at 3x3.
    """
    # Get input grid dimensions.
    input_rows, input_cols = input_grid.shape

    # Determine output grid dimensions.
    output_rows = min(3, input_rows)
    output_cols = min(3, input_cols)

    # Initialize the output grid.
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Copy values from the input grid to the output grid.
    for row in range(output_rows):
        for col in range(output_cols):
            output_grid[row, col] = input_grid[row, col]

    return output_grid
```

