"""
The transformation rule identifies vertical blue lines and extends them upwards and downwards.  Any non-blue, non-black cell acts as a "blocker," preventing the blue line from extending into adjacent cells (horizontally or vertically).  A blue line cannot extend through another blue cell.
"""

import numpy as np

def find_vertical_blue_lines(grid):
    """
    Finds the starting and ending points of vertical blue lines.
    Returns a list of tuples: (column_index, start_row, end_row)
    """
    blue_lines = []
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
                blue_lines.append((col, start_row, row - 1))
                start_row = -1
        if in_line:  # Handle lines that extend to the bottom
            blue_lines.append((col, start_row, grid.shape[0] - 1))
    return blue_lines

def is_blocking_cell(grid, row, col):
    """Checks if a cell is a blocking cell (non-black, non-blue)."""
    rows, cols = grid.shape
    if 0 <= row < rows and 0 <= col < cols:
        return grid[row, col] != 0 and grid[row, col] != 1
    return False  # Treat out-of-bounds as non-blocking

def is_adjacent_to_blocker(grid, row, col):
    """Checks for adjacent blocking cells (horizontally/vertically)."""
    for dr in [-1, 1]:
        if is_blocking_cell(grid, row + dr, col):
            return True
    for dc in [-1, 1]:
        if is_blocking_cell(grid, row, col + dc):
            return True
    return False
    
def transform(input_grid):
    """
    Transforms the input grid: extends vertical blue lines, blocked by other colors.
    """
    output_grid = input_grid.copy()
    blue_lines = find_vertical_blue_lines(input_grid)

    for col, start_row, end_row in blue_lines:
        # Extend upwards
        row = start_row - 1
        while row >= 0:
            if is_adjacent_to_blocker(output_grid, row, col) or output_grid[row, col] == 1: # added to avoid to paint over blue cells.
                break  # Stop extending if adjacent to blocker or blue
            if output_grid[row,col] != 0: # it's a blocker
                break;
            output_grid[row, col] = 1
            row -= 1

        # Extend downwards
        row = end_row + 1
        while row < input_grid.shape[0]:
            if is_adjacent_to_blocker(output_grid, row, col) or output_grid[row, col] == 1: # added to avoid to paint over blue cells.
                break  # Stop extending if adjacent to blocker or blue
            if output_grid[row,col] != 0: # it's a blocker
                break;    
            output_grid[row, col] = 1
            row += 1

    return output_grid