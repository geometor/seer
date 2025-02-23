# AboveBelow10 • 008 • example_2 • investigate_coder

---
```python
"""
Identify all green pixels (value 3) in the input grid. For each green pixel, change all pixels below it and to its right to green (value 3), bounded by the original diagonal line and the edges of the grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding green pixels downwards and to the right.
    
    Args:
        input_grid (list of lists): The input grid.
    
    Returns:
        list of lists: The transformed grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is green (value 3)
            if input_grid[r, c] == 3:
                # Expand the green color downwards and to the right
                output_grid[r:, c:] = 3

    return output_grid.tolist()
```
