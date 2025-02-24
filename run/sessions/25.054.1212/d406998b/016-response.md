# d406998b • 016 • refine_coder

---
```python
"""
Iterates through the input grid and identifies horizontal or vertical sequences
consisting of one white pixel (0) next to one gray pixel (5). If such a sequence
is found, the gray pixel is changed to green (3).
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """
    Gets the adjacent pixels (up, down, left, right) of a given cell in the grid.

    Args:
        grid: The 2D numpy array representing the grid.
        row: The row index of the cell.
        col: The column index of the cell.

    Returns:
        A list of tuples, where each tuple represents an adjacent pixel
        and contains (row, col, color).
    """
    rows, cols = grid.shape
    adjacent_pixels = []
    # Check up, down, left, right.
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            adjacent_pixels.append((new_row, new_col, grid[new_row, new_col]))
    return adjacent_pixels

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid.
    for row in range(rows):
        for col in range(cols):
            # Check if the current pixel is part of a white-gray or gray-white sequence.
            if output_grid[row, col] == 5: # start on grey
                adjacent_pixels = get_adjacent_pixels(output_grid, row, col)
                for r, c, color in adjacent_pixels:
                    if color == 0: # check if it is a grey-white sequence
                        output_grid[row,col] = 3 # it is, replace grey with green
                        break # found a sequence, move on

    return output_grid
```
