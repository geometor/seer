# 3aa6fb7a • 008 • example_2 • investigate_coder

---
```python
"""
Identifies adjacent azure (8) pixels and inserts a blue (1) pixel between them.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """
    Gets the valid neighbors of a cell.

    """
    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid by finding pairs of adjacent azure pixels and inserts blue between

    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    azure_pixels = []

    # Find all azure pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:
                azure_pixels.append((r, c))

    # Iterate through azure pixels and check neighbors
    for r, c in azure_pixels:
        neighbors = get_neighbors(input_grid, r, c)
        for nr, nc in neighbors:
            if input_grid[nr, nc] == 0:  # Check if neighbor is empty
                # check the neighbors of the neighbors for a second azure
                second_neighbors = get_neighbors(input_grid, nr, nc)
                count = 0
                for snr, snc in second_neighbors:
                    if input_grid[snr,snc] == 8:
                        count = count + 1
                if count >= 2: # at least 2 to avoid filling between diagonal 8s
                    output_grid[nr, nc] = 1  # Insert blue pixel

    return output_grid
```
