"""
The transformation process examines each cell in the input grid.
If a cell is red (color 2), yellow cells (color 4) are placed at its four diagonal positions in the output grid.
If a cell is blue (color 1), orange cells (color 7) are placed at its four orthogonal positions (up, down, left, right) in the output grid.
If a cell is magenta (color 6), it remains unchanged.
All other cells remain unchanged unless modified by the placement of yellow or orange cells due to the rules for red and blue cells.
The changes for red and blue cells are made independently and may overlap; the last applied change will overwrite the previous one.
The transformation applies only to cells that are either red or blue in the input grid.
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