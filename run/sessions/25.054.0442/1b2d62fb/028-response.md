# 1b2d62fb • 028 • refine_coder

---
```python
"""
1.  **Extract:** Extract the first three columns from the input grid.
2.  **Conditional color changes:**
    *   Examine columns 1, 2, and 3 of the original input, along with column 4 (all '1's).
    *   Identify positions where the background color (0) is present in the first three columns.
    *   Apply color changes in the output grid (the 5x3 extracted portion) based on this rule:

        * If in the input, a '0' value in any of the first three columns, directly corresponds with a value of '1' in same row of the fourth column, the output grid value remains unchanged
        * If in the input, a '0' value in columns 1, 2, or 3 does *not* have a value of '1' in the same row, fourth column, replace the pixel in the output with an '8'.
        * if the value is not '0', the output will always be '0' in output.

3.  **Output:** The resulting 5x3 grid with the modified colors is the final output.
"""

import numpy as np

def transform(input_grid):
    # Extract the first three columns
    output_grid = input_grid[:, :3].copy()
    
    # Get the fourth column for the condition
    fourth_column = input_grid[:, 3]

    # Iterate through rows and the first three columns
    for i in range(input_grid.shape[0]):
        for j in range(3):
            # Check if the current value is 0
            if input_grid[i, j] == 0:
                # Check the condition with the fourth column
                if fourth_column[i] != 1:
                    output_grid[i, j] = 8
            else:
                output_grid[i,j] = 0

    return output_grid
```
