# a85d4709 • 006 • refine_coder

---
```python
"""
The transformation applies a repeating pattern of '3' (green), '4' (yellow), and '2' (red) to the input grid, restarting the pattern at the beginning of each row. Gray pixels ('5') in the input do *not* interrupt the sequence.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same shape as the input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape
    pattern = [3, 4, 2]

    # Iterate through each cell of the input grid
    for i in range(rows):
        pattern_index = 0  # Reset pattern index for each row
        for j in range(cols):
            # Assign the current pattern color to the output, based on the pattern_index, increment and wrap
            output_grid[i, j] = pattern[pattern_index]
            pattern_index = (pattern_index + 1) % len(pattern)

    return output_grid
```

