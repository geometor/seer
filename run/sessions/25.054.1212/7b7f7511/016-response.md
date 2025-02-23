# 7b7f7511 • 016 • refine_coder

---
```python
"""
The program transforms the input grid into the output grid by cropping it to its top-left quarter. Specifically:

1.  **Determine Dimensions:** Get the number of rows and columns of the input grid.
2.  **Calculate Output Rows**: Calculate the number of output rows. Divide the input rows by 2. If the input rows is even, that value is the result. If the input rows is odd, add the remainder of input rows / 2 to the result.
3.  **Calculate Output Columns**: the number of columns in the output is exactly half the number of columns in the input.
4.  **Crop Grid:** Create the output grid by selecting the input rows from the top (index 0) of the input grid up to, but not including, the calculated output rows, and the columns from the left (index 0) of the input grid, up to, but not including, the calculated output columns.
5.  **Output**: The output grid consists of the top-left quarter of the input grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_rows = len(input_grid)
    input_cols = len(input_grid[0])
    output_rows = input_rows // 2 + input_rows % 2
    output_cols = input_cols // 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # change output pixels
    for i in range(output_rows):
        for j in range(output_cols):
            output_grid[i][j] = input_grid[i][j]

    return output_grid
```
