# 7df24a62 • 018 • refine_coder

---
```python
"""
1.  **Identify Objects:** The input grid contains yellow (4) and potentially other colored pixels. Yellow pixels can exist as single, isolated units or as connected components forming larger shapes.
2.  **Determine Isolation:** A yellow pixel is considered "isolated" if it has no orthogonally adjacent (up, down, left, or right) neighboring pixels of the same color (yellow). Diagonally adjacent yellow pixels do not negate isolation.
3.  **Apply Halo:** For each isolated yellow pixel, change the color of all adjacent pixels (including diagonally adjacent ones) from white (0) to blue (1), creating a "halo" effect, except when it's not 0.
4. **Preserve:** Pixels that are not adjacent to single isolated yellow are not modified.
"""

import numpy as np

def get_adjacent_positions(grid, row, col, include_diagonal=True):
    """Gets the adjacent positions for a given cell."""
    rows, cols = grid.shape
    adjacent_positions = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):  # Exclude the cell itself
                if not include_diagonal and (abs(i - row) + abs(j-col) > 1):
                    continue
                adjacent_positions.append((i, j))
    return adjacent_positions

def is_isolated(grid, row, col):
    """Checks if a yellow pixel is isolated (not orthogonally adjacent to other yellow pixels)."""
    if grid[row, col] != 4:
        return False

    adjacent_coords = get_adjacent_positions(grid, row, col, include_diagonal=False)
    for r, c in adjacent_coords:
        if grid[r, c] == 4:
            return False  # Not isolated if orthogonally adjacent to another yellow pixel
    return True

def transform(input_grid):
    """Transforms the input grid according to the halo rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell to find isolated yellow pixels
    for row in range(rows):
        for col in range(cols):
            if is_isolated(input_grid, row, col):
                # Apply blue halo to all adjacent positions, including diagonals
                adjacent_coords = get_adjacent_positions(input_grid, row, col, include_diagonal=True)
                for r, c in adjacent_coords:
                    if output_grid[r, c] == 0:  # Only change background (0) pixels
                        output_grid[r, c] = 1

    return output_grid
```
