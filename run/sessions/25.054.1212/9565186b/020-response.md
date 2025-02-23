# 9565186b • 020 • example_4 • investigate_coder

---
```python
"""
The middle row of the input grid is preserved in the output grid. All other cells in the output grid are changed to gray (5).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule:
    The middle row remains unchanged, and all other cells become gray (5).
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the height of the grid
    height = output_grid.shape[0]

    # Calculate the index of the middle row.
    middle_row_index = height // 2

    # Iterate through all cells of the grid.
    for i in range(height):
        for j in range(output_grid.shape[1]):
            # Change all but middle row to gray (5).
            if i != middle_row_index:
              output_grid[i,j] = 5

    return output_grid
```
