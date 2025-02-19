# 3-1e0a9b12 • 004 • example_2 - CODE

---
```python
"""
Moves all non-zero colored cells to the bottom rows of the grid,
preserving their original column and color, filling the rows from bottom to top.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero cells to the bottom rows.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid.
    rows, cols = output_grid.shape

    # Clear the last row to prepare to move the non-zero cells.
    # The last rows will be filled with the input cells with non-zero values, from bottom to top.
    output_grid[:, :] = 0
    
    # Iterate through each column.
    for j in range(cols):
        # Find the non-zero elements in the current column.
        non_zero_elements = []
        for i in range(rows):
           if input_grid[i,j] != 0:
              non_zero_elements.append(input_grid[i,j])
        
        # Move last non-zero values to the last rows.
        for i, value in enumerate(reversed(non_zero_elements)):
           output_grid[rows-1-i, j] = value
           

    return output_grid
```

