# 3-1e0a9b12 • 004 • example_2 - CODE

---
```python
"""
Moves all non-zero colored objects towards the bottom of the grid, preserving their column and relative row order. Objects in the same column maintain their relative vertical order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the bottom-most
    available position in their respective columns, maintaining their original
    vertical order.

    Args:
    input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
    list of lists: The transformed grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    for j in range(cols):
        # Collect non-zero elements from the current column
        non_zero_elements = []
        for i in range(rows):
            if input_grid[i][j] != 0:
                non_zero_elements.append(input_grid[i][j])

        # Place non-zero elements at the bottom of the column in output_grid
        for i in range(len(non_zero_elements)):
            output_grid[rows - len(non_zero_elements) + i][j] = non_zero_elements[i]

    return output_grid
```

