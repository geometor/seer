# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The process transforms the input grid by examining each cell.
If a cell contains the color red (2), then in the output grid, yellow cells (4) are placed at the four diagonal positions relative to this red cell.
If a cell contains the color blue (1), then in the output grid, orange cells (7) are placed at the four orthogonal (up, down, left, right) positions relative to this blue cell.
If a cell is of any other color, it remains unchanged in the output grid, unless it becomes modified by the placement of new colors around red or blue cells.
The modifications for red and blue cells are independent and can potentially overlap. If they do overlap, the color placed last will overwrite the previous one. In this example, no overlaps occur.
The process is applied to each cell in the input grid that is either red or blue.
"""

import numpy as np

def get_neighbors(grid, row, col, diagonal=False):
    """
    Returns the neighbors of a cell.
    If diagonal is True, returns diagonal neighbors.
    Otherwise, returns orthogonal neighbors.
    """
    rows, cols = grid.shape
    neighbors = []
    if diagonal:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if 0 <= row + dr < rows and 0 <= col + dc < cols:
                neighbors.append((row + dr, col + dc))
    else:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= row + dr < rows and 0 <= col + dc < cols:
                neighbors.append((row + dr, col + dc))
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    output_grid = np.copy(input_grid)  # Initialize output grid as a copy of the input grid
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is red (2)
            if input_grid[row, col] == 2:
                # Place yellow (4) cells at diagonal positions
                for r, c in get_neighbors(input_grid, row, col, diagonal=True):
                    output_grid[r, c] = 4
            # If the cell is blue (1)
            elif input_grid[row, col] == 1:
                # Place orange (7) cells at orthogonal positions
                for r, c in get_neighbors(input_grid, row, col, diagonal=False):
                    output_grid[r, c] = 7

    return output_grid
```
