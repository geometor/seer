# bbc9ae5d • 012 • refine_coder

---
```python
"""
Transforms a single-row grid into a multi-row grid where the most frequent non-zero color is replicated diagonally downwards and to the right, starting from its first occurrence. The output grid's width is the same as the input, and the number of rows is based on the count of the most frequent color and starting column.
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
    # Find the most frequent non-zero color
    most_frequent_color = get_most_frequent_non_zero_color(input_grid)

    # Handle all-zero input case
    if most_frequent_color == 0:
        return input_grid.copy()

    # Find the first occurrence of the most frequent color
    first_occurrence_col = np.where(input_grid == most_frequent_color)[0][0]

    # Count occurrences of the most frequent color
    count = np.count_nonzero(input_grid == most_frequent_color)

    # Determine output dimensions
    num_rows = count + first_occurrence_col
    num_cols = input_grid.shape[1]
    output_grid = np.zeros((num_rows, num_cols), dtype=int)

    # Copy the first row from input to output
    output_grid[0, :] = input_grid

    # Populate output grid with diagonal replication
    for i in range(1, num_rows):
        for j in range(num_cols):
          if j >= first_occurrence_col and j - first_occurrence_col <= i :
            if j < num_cols and j-(j-first_occurrence_col)-first_occurrence_col < num_cols :
                output_grid[i, j] = most_frequent_color

    return output_grid
```
