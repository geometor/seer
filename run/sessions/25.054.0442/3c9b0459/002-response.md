# 3c9b0459 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is a 180-degree rotation of the grid. Each pixel at position (row, column) in the input grid moves to position (2-row, 2-column) in the output grid, with the row and column indices using zero-based indexing, consistent with python.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the input grid
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Iterate through each cell of the input grid
    for i in range(rows):
        for j in range(cols):
            # Apply the 180-degree rotation transformation
            output_grid[rows - 1 - i][cols - 1 - j] = input_grid[i][j]

    return output_grid
```

