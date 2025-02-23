# 6-0520fde7 • 002 • example_1 - CODE

---
```python
"""
If the input grid contains a vertical column of gray color (5), the output is a fixed 3x3 grid with a red pixel (2) in the center and white color (0) elsewhere. The input's content otherwise is ignored.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of a gray column.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Check if any column is entirely composed of the color 5 (gray).
    gray_column_present = False
    for j in range(cols):
        if np.all(input_grid[:, j] == 5):
            gray_column_present = True
            break

    # Initialize a 3x3 output grid filled with 0 (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # If a gray column is present, set the center cell to 2 (red).
    if gray_column_present:
        output_grid[1, 1] = 2

    return output_grid.tolist()
```
