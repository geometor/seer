# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
Shifts all non-zero colored cells to the last row, maintaining their original order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the last row,
    maintaining their relative order, and filling the rest with zeros.

    Args:
    input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
    list of lists: The transformed grid.
    """
    # Initialize output_grid with zeros
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    # Find non-zero elements and their original positions
    non_zero_elements = []
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != 0:
                non_zero_elements.append((input_grid[i][j], i, j))  # Store value, original row, and original column

    # Sort based on the described logic. The primary key for sorting will be the original row in reverse (bottom up).
    #secondary sort key is the original col (left-to-right).

    non_zero_elements.sort(key=lambda x: ( -x[1], x[2]))

    # Place non-zero elements in the last row of output_grid
    last_row_index = 0
    for element in non_zero_elements:
        output_grid[rows - 1][last_row_index] = element[0]
        last_row_index += 1

    return output_grid
```

