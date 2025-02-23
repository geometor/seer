# 9af7a82c • 004 • refine_coder

---
```python
"""
1.  **Determine Output Dimensions:** The output grid has the same number of columns as the input grid. The number of rows in the output grid is equal to the number of rows in the input grid plus 2.

2.  **Column-wise Transformation:**  For each column in the input grid, perform the following steps to create the corresponding column in the output grid:

    a. **Extract Input Column:** Get all values from the current column of the input grid.

    b. **Reorder Values:** Treat the non zero values in the input column as the ordering.

    c. **Pad with Zeros:** Fill any remaining cells in the output column (after placing the reordered values) with the value 0 (representing the color white).

3.  **Assemble Output:** Combine the transformed columns to form the complete output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_height =  input_grid.shape[0] + 2
    output_width = input_grid.shape[1]
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for j in range(input_grid.shape[1]):
        # Get the values from the input column
        input_column_values = input_grid[:, j]

        # Get non-zero values and their original indices.
        non_zero_values = input_column_values[input_column_values != 0]

        # build output col
        output_col = np.concatenate([non_zero_values, np.zeros(output_height - len(non_zero_values), dtype=int)])

        # write col to output
        output_grid[:, j] = output_col


    return output_grid.tolist()
```
