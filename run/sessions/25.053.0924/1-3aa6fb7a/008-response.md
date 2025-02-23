# 1-3aa6fb7a • 008 • example_2 - CODE

---
```python
"""
Transformation Rule:

1.  **Identify '8' Pixels:** Locate all pixels with the value '8' (azure) in the input grid.
2.  **Identify Potential '1' Locations:** Examine the empty (value '0', white) pixels that are adjacent to the '8' pixels. Check how many '8' neighbors (including diagonals) exist for these locations.
3. **Insert '1':** If an empty cell has three and only three adjacent '8' pixels (diagonally, vertically, or horiontally), and at least one neighbor must be horizontally or vertically adjacent (not diagonal only), change its value to '1' (blue) in the output grid.
4.  **No Other Changes:** All other pixels retain their original values from the input grid.
"""

import numpy as np

def count_neighbors(grid, r, c, neighbor_val):
    """Counts the number of neighbors with a specific value around a cell."""
    count = 0
    for i in range(max(0, r - 1), min(grid.shape[0], r + 2)):
        for j in range(max(0, c - 1), min(grid.shape[1], c + 2)):
            if (i != r or j != c) and grid[i, j] == neighbor_val:
                count += 1
    return count

def has_adjacent_neighbor(grid, r, c, neighbor_val):
    """Checks if a cell has at least one directly adjacent (non-diagonal) neighbor with specified value"""
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == neighbor_val:
             return True

    return False

def transform(input_grid):
    """Transforms the input grid according to the rule."""
    output_grid = np.copy(input_grid)  # Initialize output as a copy of the input

    # Iterate through all cells
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            # Check for '0' (empty) cells
            if input_grid[r, c] == 0:
                # Count '8' neighbors
                neighbors_8 = count_neighbors(input_grid, r, c, 8)
                #check for an adjacent (non-diagonal neighbor)
                adj_neighbor = has_adjacent_neighbor(input_grid,r,c,8)
                # If three '8' neighbors and one is adjacent (not diagonal) insert '1'
                if neighbors_8 == 3 and adj_neighbor:
                    output_grid[r, c] = 1

    return output_grid
```
