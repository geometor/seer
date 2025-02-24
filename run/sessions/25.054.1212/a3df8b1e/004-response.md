# a3df8b1e • 004 • refine_coder

---
```python
"""
Creates a checkerboard pattern and inverts rows based on input '1's.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Create base checkerboard pattern
    for i in range(rows):
        for j in range(cols):
            output_grid[i][j] = (i + j) % 2

    # Invert rows based on input '1's
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == 1:
                for k in range(i + 1, rows):  # Start inverting from the row *below* the '1'
                    for l in range(cols):
                        output_grid[k][l] = 1 - output_grid[k][l]  # Invert the cell
                break # assumes there's only one '1' in input
        else:
            continue
        break

    return output_grid
```

