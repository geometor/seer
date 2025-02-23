# 3631a71a • 014 • example_3 • investigate_coder

---
```python
"""
A 3x3 "median filter" approach with a special rule for a clear majority is
applied on the grid. The "majority" color, or if none, fill with an external common
color.
"""

import numpy as np
from collections import Counter

def get_surrounding_colors(grid, row, col, block_size=3):
    """Gets colors surrounding a block in the grid."""
    surrounding = []
    start_row, start_col = row - 1, col - 1
    end_row, end_col = row + block_size, col + block_size

    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if (start_row <= i < end_row and start_col <= j < end_col):
                continue  # Skip the inner block itself
            if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]:
                surrounding.append(grid[i, j])
    return surrounding

def transform(input_grid):
    """Transforms the input grid by applying a 3x3 filter."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    block_size = 3

    for row in range(rows - block_size + 1):
        for col in range(cols - block_size + 1):
            block = input_grid[row:row+block_size, col:col+block_size]
            
            # Count occurrences of each color in the block
            color_counts = Counter(block.flatten())
            most_common_color, count = color_counts.most_common(1)[0]

            # If a color occupies more than half the block, fill with that color
            if count > (block_size * block_size) // 2:
                output_grid[row:row+block_size, col:col+block_size] = most_common_color
            else:
                # Find most common surrounding color
                surrounding_colors = get_surrounding_colors(input_grid, row, col)
                if surrounding_colors:
                    surrounding_counts = Counter(surrounding_colors)
                    most_common_surrounding = surrounding_counts.most_common(1)[0][0]
                    output_grid[row:row+block_size, col:col+block_size] = most_common_surrounding
                # else: leave as is (this case should be handled by initialization copy)
    return output_grid
```
