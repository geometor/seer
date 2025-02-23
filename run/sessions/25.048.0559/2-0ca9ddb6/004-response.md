# 2-0ca9ddb6 • 004 • Response

---

*text:*

```python
"""
This script transforms an input grid based on the following rules:
1. Identifies all positions of red (2) and blue (1) cells.
2. Constructs a plus-shaped pattern around each red cell using yellow (4) cells.
3. Constructs a plus-shaped pattern around each blue cell using orange (7) cells.
4. Retains the original positions of the red and blue cells, and any other color.
"""

import numpy as np

def find_all_cells(grid, color):
    """Finds the coordinates of all occurrences of a single cell of the specified color."""
    return np.argwhere(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all red and blue cells
    red_positions = find_all_cells(input_grid, 2)
    blue_positions = find_all_cells(input_grid, 1)

    # Construct plus pattern around each red cell
    for red_pos in red_positions:
        row, col = red_pos
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        if row < rows - 1:
            output_grid[row + 1, col] = 4  # Below
        if col > 0:
            output_grid[row, col - 1] = 4  # Left
        if col < cols - 1:
            output_grid[row, col + 1] = 4  # Right

    # Construct plus pattern around each blue cell
    for blue_pos in blue_positions:
        row, col = blue_pos
        if row > 0:
            output_grid[row - 1, col] = 7  # Above
        if row < rows - 1:
            output_grid[row + 1, col] = 7  # Below
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < cols - 1:
            output_grid[row, col + 1] = 7  # Right

    return output_grid
```

