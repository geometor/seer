# f2829549 • 026 • example_5 • investigate_coder

---
```python
"""
1.  **Initialize:** Create an output grid with the same height as the input grid. The width of the output will be calculated in the next step.

2. **Calculate Columns to Isolate, and the output width:**
    * Take the first column from the Input
    * Take the fourth column from the input
    * Take the element-wise sum of the two selected columns, replace any non-zero result with the color green (value 3)
    * The width of the output is equal to the number of columns selected (3).

3.  **Populate Output:**
    *   Iterate through each row of the derived columns.
    *   Transfer the results of the calculations directly into the output.

4.  **Result:** The output grid is a summarized representation, where orange (7) and blue(1) combine as green(3)
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    input_grid = np.array(input_grid)
    height = input_grid.shape[0]
    output_grid = np.zeros((height, 3), dtype=int)

    # Extract the first column.
    first_column = input_grid[:, 0]

    # Extract the fourth column.
    fourth_column = input_grid[:, 3]

    # elementwise sum of first and fourth
    summed_column = first_column + fourth_column

    # if sum > 0, make the output element green (3)
    summed_column[summed_column > 0] = 3

    # populate the output grid
    output_grid[:, 0] = first_column
    output_grid[:, 0][output_grid[:, 0] > 0] = 3
    output_grid[:, 1] = fourth_column
    output_grid[:, 1][output_grid[:, 1] > 0] = 3
    output_grid[:, 2] = summed_column

    return output_grid.tolist()
```
