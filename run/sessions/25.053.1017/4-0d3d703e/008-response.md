# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The input grid is transformed into the output grid by replacing each number with a corresponding new number. The mapping is as follows:

*   9 is replaced by 8.
*   4 is replaced by 3.
*   2 is replaced by 6.

The structure of the grid (3x3) and relative position of the pixels are preserved; only the values of the pixels change according to this mapping.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the mapping dictionary.
    mapping = {
        9: 8,
        4: 3,
        2: 6,
    }

    # Iterate through the grid and apply the mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in mapping:
                output_grid[i, j] = mapping[output_grid[i, j]]

    return output_grid
```

