# 7447852a • 002 • example_1 • investigate_coder

---
```python
"""
Transforms an input grid of pixels into an output grid, replacing some red pixels (2) with yellow pixels (4) based on adjacency rules. A red pixel is changed to yellow if it has at least one orthogonally adjacent white pixel (0) and one orthogonally adjacent red pixel (2).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the adjacency rules.
    """
    rows, cols = input_grid.shape
    output_grid = np.copy(input_grid)  # Initialize output grid

    def is_valid(r, c):
        """Checks if the given row and column are within grid bounds."""
        return 0 <= r < rows and 0 <= c < cols

    def get_adjacent_colors(r, c):
        """Gets the colors of orthogonally adjacent cells."""
        adjacent_colors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Right, Left, Down, Up
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                adjacent_colors.append(input_grid[nr, nc])
        return adjacent_colors

    # Iterate through each cell of the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Check if the cell is red
                adjacent_colors = get_adjacent_colors(r, c)
                has_white_neighbor = 0 in adjacent_colors
                has_red_neighbor = 2 in adjacent_colors

                if has_white_neighbor and has_red_neighbor:
                    output_grid[r, c] = 4  # Change to yellow

    return output_grid
```
