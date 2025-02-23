# 1fad071e • 002 • example_1 • investigate_coder

---
```python
"""
The program analyzes the input grid and identifies the presence and quantity of distinct blue (1) regions. The output is a 1x5 grid where the first section represents the number of distinct blue regions (as blue pixels), and the remaining pixels are white (0).
"""

import numpy as np

def count_contiguous_blocks(grid, color):
    """Counts the number of contiguous blocks of a given color in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    count = 0

    def dfs(row, col):
        """Depth-first search to explore a contiguous block."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                dfs(row, col)
                count += 1
    return count

def transform(input_grid):
    # Initialize output grid as 1x5 with all white pixels.
    output_grid = np.zeros((1, 5), dtype=int)

    # Count contiguous blocks of blue (1).
    blue_count = count_contiguous_blocks(input_grid, 1)

    # Fill the beginning of the output grid with blue pixels based on the count.
    for i in range(min(blue_count, 5)):
        output_grid[0, i] = 1

    return output_grid
```
