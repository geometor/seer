# bbc9ae5d • 010 • refine_coder

---
```python
"""
Transforms a single-row grid into a multi-row grid where the most frequent non-zero color is replicated diagonally downwards and to the right.
"""

import numpy as np

def get_most_frequent_non_zero_color(grid):
    """Finds the most frequent non-zero color in a grid."""
    non_zero_elements = grid[grid != 0]
    if non_zero_elements.size == 0:
        return 0
    counts = np.bincount(non_zero_elements)
    return np.argmax(counts)

def transform(input_grid):
    # Identify the most frequent non-zero color
    most_frequent_color = get_most_frequent_non_zero_color(input_grid)

    # Count occurrences of the most frequent color
    count = np.count_nonzero(input_grid == most_frequent_color)

    # Determine output dimensions
    num_rows = 2 * count -1 if count > 0 else 1 # handles edge case when entire input is zeros
    num_cols = input_grid.shape[1]
    output_grid = np.zeros((num_rows, num_cols), dtype=int)

    # Populate output grid
    for r in range(num_rows):
      if most_frequent_color != 0:
        output_grid[r, :min(r + 1, num_cols)] = most_frequent_color #min added to fix possible index error.

    return output_grid
```
