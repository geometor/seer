"""
The transformation rule identifies vertical lines of color 8 (azure) in the input grid.
For each of these lines, it finds the cell immediately to the right of the top cell of the line.
The color of this cell is then changed to 1 (blue) in the output grid. The azure lines themselves are kept.
"""

import numpy as np

def find_vertical_lines(grid, color):
    """
    Finds vertical lines of a specified color in the grid.
    Returns a list of (row, col) tuples representing the top cell of each line.
    """
    lines = []
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_lines = find_vertical_lines(input_grid, 8)

    for top_row, top_col in azure_lines:
        # Find the cell to the right of the top cell
        right_neighbor_row = top_row
        right_neighbor_col = top_col + 1

        # Check if the right neighbor is within bounds
        if right_neighbor_col < output_grid.shape[1]:
            output_grid[right_neighbor_row, right_neighbor_col] = 1

    return output_grid