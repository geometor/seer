# f2829549 • 030 • refine_coder

---
```python
"""
1.  **Column Copying:** Copy the first and second column values directly from the input grid to the first and second columns of the output grid, respectively.
2.  **Conditional Third Column:**
    - Iterate through each row of the *input grid*.
    - The width of the *output_grid* is 3.
    - Create an output grid of *input grid* height x 3, filled with black(0).
    - The output grid's first and second columns are a copy of the input grid's first and second columns.
    - If in any row of *input grid*, column at index 3 is blue(1), then in the same row of *output grid* column at index 2 is 3(green).
    - Return *output grid*
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    height = input_grid.shape[0]
    output_grid = np.zeros((height, 3), dtype=int)

    # Copy the first and second columns from input to output
    output_grid[:, 0] = input_grid[:, 0]
    output_grid[:, 1] = input_grid[:, 1]

    # change output pixels: Create the third column based on the condition.
    for i in range(height):
        if input_grid[i, 3] == 1:
            output_grid[i, 2] = 3

    return output_grid.tolist()
```
