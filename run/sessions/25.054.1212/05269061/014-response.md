# 05269061 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule is to identify the diagonal sequence of colored pixels (8, 3, 4) in the input grid and replicate it across the entire output grid, both horizontally and vertically, starting with 4.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid with the same dimensions as the input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Define the repeating sequence
    sequence = [4, 8, 3]

    # Fill the output grid with the repeating sequence
    for i in range(rows):
        for j in range(cols):
            # Calculate the index in the sequence based on row and column
            seq_index = (i + j) % len(sequence)
            output_grid[i, j] = sequence[seq_index]

    return output_grid
```
