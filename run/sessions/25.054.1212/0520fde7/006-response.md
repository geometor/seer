# 0520fde7 • 006 • refine_coder

---
```python
"""
1. Identify Central Column: Find the central vertical column of the input grid.
2. Locate Gray Pixels: Determine the row indices of any gray (value 5) pixels within this central column.
3. Create Output Grid: Initialize a 3x3 output grid filled with white pixels (value 0).
4. Map Gray to Red: For each row index where a gray pixel was found in the input's central column, set the pixel at the *same* row index, but the *center* column (index 1), of the output grid to red (value 2).
"""

import numpy as np

def get_central_column_index(grid):
    """
    Returns the index of the central column of a 2D numpy array.
    """
    _, num_cols = grid.shape
    return num_cols // 2

def get_gray_indices_in_column(column):
    """
    Returns the indices of gray (5) pixels in a column.
    """
    return np.where(column == 5)[0]

def transform(input_grid):
    """
    Transforms the input grid according to the rules.
    """
    # Create Output Grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Identify Central Column
    central_col_index = get_central_column_index(input_grid)
    central_column = input_grid[:, central_col_index]

    # Locate Gray Pixels
    gray_indices = get_gray_indices_in_column(central_column)

    # Map Gray to Red
    for row_index in gray_indices:
        if row_index < 3: # Ensure we don't go out of bounds of 3x3
            output_grid[row_index, 1] = 2

    return output_grid
```

