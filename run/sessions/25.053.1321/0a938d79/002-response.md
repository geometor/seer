# 0a938d79 • 002 • example_1 - CODE

---
```python
"""
The transformation identifies the columns containing non-white pixels in the input grid.
It then generates full-height columns of those colors in the output grid,
creating an alternating pattern that fills each row.
"""

import numpy as np

def get_colored_columns(input_grid):
    """
    Finds the column indices and colors of non-white pixels in the input grid.
    """
    colored_columns = []
    rows, cols = input_grid.shape
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                colored_columns.append((c, input_grid[r, c]))
                break # only consider first occurance in column
    return colored_columns

def transform(input_grid):
    """
    Transforms the input grid by extending identified colored pixels into full columns.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find columns with colored pixels
    colored_columns = get_colored_columns(input_grid)
    
    first_row = np.zeros(cols, dtype=int)
    # Create alternating pattern based on identified columns.
    for col_index, color in colored_columns:
        for i in range(cols):
          if (i - col_index) % 2 == 0:
              first_row[i] = color


    for r in range(rows):
        output_grid[r,:] = first_row
            

    return output_grid
```
