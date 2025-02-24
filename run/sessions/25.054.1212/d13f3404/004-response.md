# d13f3404 • 004 • refine_coder

---
```python
"""
Expands a 3x3 input grid into a 6x6 output grid. Non-zero pixels from the input are propagated diagonally downwards and to the right in the output, starting from the corresponding position in the output grid (scaled by 2x).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the diagonal expansion rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros((6, 6), dtype=int)  # Initialize output grid with zeros

    # Iterate through the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check for non-zero pixels
            if input_grid[i, j] != 0:
                # Calculate the starting position in the output grid (2x scaling)
                start_row = i * 2
                start_col = j * 2

                # Diagonal expansion
                current_row, current_col = start_row, start_col
                while current_row < 6 and current_col < 6:
                    output_grid[current_row, current_col] = input_grid[i, j]
                    current_row += 1
                    current_col += 1

    return output_grid.tolist()
```
