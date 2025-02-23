# 00d62c1b • 040 • refine_coder

---
```python
"""
1.  **Identify Green Pixels:** Locate all pixels with a value of 3 (green).
2.  **Check Neighbors**: For each green pixel, check its 8 neighbors (including diagonals)
3.  **Change color**: If the only neighboring pixels are either background (0) or other green pixels (3), change color from green (3) to yellow (4) if:
    *   The green pixel has *two or more* diagonally-adjacent green neighbors.
    *  The green pixel is completly surrounded (all 8 neighbors) are green

4.  **Preserve other pixels**: Any pixel that does not meet these conditions should remain unchanged.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the neighbors (including diagonals) of a cell."""
    neighbors = []
    rows, cols = grid.shape
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append(grid[i, j])
    return neighbors

def get_diagonal_neighbors(grid, row, col):
    """Gets only the diagonal neighbors of a cell"""
    neighbors = []
    rows, cols = grid.shape
    for i in range(-1,2,2):
        for j in range(-1,2,2):
          if 0 <= row + i < rows and 0 <= col + j < cols:
                neighbors.append(grid[row+i, col+j])

    return neighbors

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is green (3)
            if input_grid[row, col] == 3:
                neighbors = get_neighbors(input_grid, row, col)
                # Check if neighbors are only green or background
                if all(neighbor == 3 or neighbor == 0 for neighbor in neighbors):
                    diagonal_neighbors = get_diagonal_neighbors(input_grid, row, col)
                    count_green_diagonal = sum(1 for dn in diagonal_neighbors if dn == 3)
                    # Inner Infill: Check for surrounding green pixels
                    if all(neighbor == 3 for neighbor in neighbors):
                        output_grid[row, col] = 4  # Change to yellow (4)
                    elif count_green_diagonal >= 2:
                        output_grid[row, col] = 4


    return output_grid
```
