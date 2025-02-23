# 3-1e0a9b12 • 006 • example_3 - CODE

---
```python
"""
The transformation rule is to move all non-zero colored objects in each column of the input grid to the bottom of the corresponding column in the output grid, while maintaining their vertical order within each column. Any empty spaces created at the top of the columns in the output grid are filled with white color (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero elements in each column to the bottom,
    maintaining their order, and filling the remaining spaces with zeros.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)  # Initialize output_grid with zeros

    num_rows, num_cols = input_grid.shape

    # Iterate through each column
    for j in range(num_cols):
        # Extract non-zero elements from the current column
        non_zero_elements = input_grid[:, j][input_grid[:, j] != 0]
        
        # Calculate the starting row index for placing non-zero elements at the bottom
        start_row = num_rows - len(non_zero_elements)
        
        # Place the non-zero elements at the bottom of the corresponding column in output_grid
        output_grid[start_row:, j] = non_zero_elements

    return output_grid
```

