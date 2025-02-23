# a85d4709 • 006 • refine_coder

---
```python
"""
Transforms the input grid according to the following rules:

1. Identify Rows: The input grid consists of rows of pixels.
2. Transform Rows by color and sequence. The output grid replaces the
   entire input row with an entire row of a single color.
    * If a row in the input has some pixels with color `5`, and a
      corresponding all-`3` row does NOT exist in the output, then replace
      all pixels in this input row with `2`.
    * If a row in the input has some pixels with color `0`, and a
      corresponding all-`3` row does NOT exist in the output, then replace
      all pixels in this input row with `4`.
    * If an entire row of color `5` exists in the input, replace that
      entire row with color `3`
    * If all remaining rows have pixels of color `0`, then those rows
      all become `3`.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows = len(input_grid)
    cols = len(input_grid[0])
    
    # Check for entire row of 5
    all_5_row = -1
    for i in range(rows):
        if np.all(input_grid[i] == 5):
            all_5_row = i
            break

    # Apply transformations
    for i in range(rows):
        if all_5_row != -1 and np.all(input_grid == 5):
          output_grid[i,:] = 3
        elif np.any(input_grid[i] == 5) and all_5_row == -1:
            output_grid[i,:] = 2
        elif np.any(input_grid[i] == 0) and all_5_row == -1:
           output_grid[i,:] = 4
        elif np.any(input_grid[i] == 0) and all_5_row != -1:
           output_grid[i,:] = 3

    return output_grid
```
