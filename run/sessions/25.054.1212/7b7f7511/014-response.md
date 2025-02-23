# 7b7f7511 • 014 • example_3 • investigate_coder

---
```python
"""
The program takes the input grid and crops it to produce the output grid. The output grid consists of the top half of the input grid. Specifically, we take all columns, and the rows from the start index (0) up to, but not including, the row at the middle of the height of the input (input rows / 2).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_rows = len(input_grid)
    input_cols = len(input_grid[0])
    output_rows = input_rows // 2
    output_cols = input_cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # change output pixels 
    for i in range(output_rows):
        for j in range(output_cols):
            output_grid[i][j] = input_grid[i][j]

    return output_grid
```
