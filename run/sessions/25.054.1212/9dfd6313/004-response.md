# 9dfd6313 • 004 • refine_coder

---
```python
"""
Transforms the input grid by placing the first column of the input grid onto the main diagonal of the output grid. 
Subsequent columns are shifted to the left, wrapping around as needed.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    # Place the first column of input_grid onto the main diagonal of output_grid
    for i in range(min(rows, cols)):
        output_grid[i][i] = input_grid[i][0]

    # Shift and wrap subsequent columns
    for j in range(1, cols):
        for i in range(rows):
            output_grid[i][(i + j) % cols] = input_grid[i][j]
    
    return output_grid
```
