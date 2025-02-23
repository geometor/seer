# 4-0d3d703e • 010 • example_2 - CODE

---
```python
"""
Transforms a 3x3 grid of single-digit integers by replacing each integer with a new integer according to a predefined mapping, while maintaining the original grid structure and positions.

Mapping:
    2 -> 6
    3 -> 4
    8 -> 9
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to a specific color mapping.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Define the mapping.
    mapping = {
        2: 6,
        3: 4,
        8: 9,
    }

    # Apply the mapping to each element of the grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] in mapping:
                output_grid[i, j] = mapping[input_grid[i, j]]

    return output_grid
```
