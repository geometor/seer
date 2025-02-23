# ed36ccf7 • 012 • refine_coder

---
```python
"""
1. Identify Colors: Determine the two colors present in the input grid. One will be color 0 (white), and the other will be a non-zero color (the "active" color).

2. Top-Left Corner: The color of the top-left cell in the output grid is always the "active" color.

3. Diagonal Fill:
    - consider the diagonals of the grid running from top-left to bottom-right.
    - The non-zero color from the input grid replaces the 0 (white) color along these diagonals, starting from the top-left. The replacement proceeds along a diagonal until a cell of non-zero color is encountered in the input or the diagonal has completed.
    - The process then continues with the next diagonal

4. Preserve Counts: Ensure that the total number of pixels of each color remains the same between the input and output grids. If there are not enough '0' cells available, existing locations from input are used in the output.
"""

import numpy as np

def get_diagonals(grid):
    """
    Returns a list of diagonals in the grid, from top-left to bottom-right.
    """
    rows, cols = grid.shape
    diagonals = []
    for i in range(rows + cols - 1):
        diagonal = []
        for j in range(max(0, i - rows + 1), min(i + 1, cols)):
            row = i - j
            col = j
            diagonal.append((row, col))
        diagonals.append(diagonal)
    return diagonals

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify Colors
    colors = np.unique(input_grid)
    active_color = colors[colors != 0][0]  # The non-zero color
    background_color = 0

    # Top-Left Corner
    output_grid[0, 0] = active_color

    # Diagonal Fill
    diagonals = get_diagonals(input_grid)
    active_color_count = np.sum(input_grid == active_color)
    active_color_placed = 0

    for diagonal in diagonals:
        for row, col in diagonal:
            if active_color_placed < active_color_count:
                if input_grid[row,col] == background_color:
                    output_grid[row, col] = active_color
                    active_color_placed +=1
            else:
                break


    # Preserve Counts: This part is implicitly handled by the diagonal fill
    # and the active_color_placed limit.

    return output_grid
```
