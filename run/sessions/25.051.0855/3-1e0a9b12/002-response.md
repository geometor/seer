# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
Transformation Rule: Move all non-zero colored cells to the bottom-most available row within their respective columns, maintaining their relative order, and fill the remaining cells with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero cells to the bottom of their columns.
    
    Args:
        input_grid (list of lists): The input grid.
        
    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column
    for j in range(cols):
        # Extract non-zero elements and their original row indices
        column_elements = []
        for i in range(rows):
            if input_grid[i, j] != 0:
                column_elements.append((i, input_grid[i, j]))
        
        # Place elements at the bottom of the output column
        for k, (original_row, value) in enumerate(column_elements):
            output_grid[rows - len(column_elements) + k, j] = value

    return output_grid.tolist()
```

