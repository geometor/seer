"""
The transformation rule takes the existing vertical blue lines and extends them, but the green cells act as "blockers," preventing the blue lines from expanding into adjacent cells, either vertically or horizontally.
"""

import numpy as np

def find_vertical_lines(grid):
    """
    Finds the starting and ending points of vertical blue lines.
    Returns a list of tuples: (column_index, start_row, end_row)
    """
    vertical_lines = []
    for col in range(grid.shape[1]):
        in_line = False
        start_row = -1
        for row in range(grid.shape[0]):
            if grid[row, col] == 1:
                if not in_line:
                    in_line = True
                    start_row = row
            elif in_line:
                in_line = False
                vertical_lines.append((col, start_row, row - 1))
                start_row = -1
        if in_line:  # Handle lines that extend to the bottom
            vertical_lines.append((col, start_row, grid.shape[0] - 1))
    return vertical_lines

def is_adjacent_to_green(grid, row, col):
    """Checks if a cell is adjacent to a green cell (horizontally or vertically)."""
    rows, cols = grid.shape
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (dr == 0 or dc == 0) and (dr != 0 or dc != 0):  # Check horizontal/vertical, not diagonal
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 3:
                    return True
    return False

def transform(input_grid):
    """
    Transforms the input grid according to the rule: extend vertical blue lines,
    but green cells block the extension.
    """
    output_grid = input_grid.copy()
    vertical_lines = find_vertical_lines(input_grid)

    for col, start_row, end_row in vertical_lines:
        # Extend upwards
        for row in range(start_row - 1, -1, -1):
            if not is_adjacent_to_green(input_grid, row, col):
                output_grid[row, col] = 1
            else:
                break  # Stop extending if adjacent to green

        # Extend downwards
        for row in range(end_row + 1, input_grid.shape[0]):
            if not is_adjacent_to_green(input_grid, row, col):
                output_grid[row, col] = 1
            else:
                break # Stop extending if adjacent to green

    return output_grid