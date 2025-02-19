# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule consists of increasing the value associated with each color.
If the input value is 1, the output value is 5.
Otherwise, the output value is the input value + 1.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping.
    Args:
        input_grid: A 2D numpy array representing the input grid.
    Returns:
        A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color mapping rules.
            if input_grid[i, j] == 1:
                output_grid[i, j] = 5
            else:
                output_grid[i, j] = input_grid[i, j] + 1

    return output_grid
```

