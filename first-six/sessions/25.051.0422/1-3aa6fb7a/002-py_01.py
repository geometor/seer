"""
The transformation involves adding blue (color 1) pixels adjacent to the right and to the left of the two vertical azure lines. The azure and white objects remain unchanged.
"""

import numpy as np

def find_vertical_lines(grid, color):
    lines = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r+1, c] == color:
                lines.append([(r, c), (r + 1, c)])
    return lines

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find vertical lines of color 8
    vertical_lines = find_vertical_lines(input_grid, 8)

    # check the assumption of only two vertical lines
    if len(vertical_lines) != 2:
            raise ValueError("This program assumes exactly two vertical lines of color 8")

    # fill the right neighbor of the first vertical line with blue (color 1)
    first_line = vertical_lines[0]
    right_neighbor_row = first_line[0][0]
    right_neighbor_col = first_line[0][1] + 1

    if right_neighbor_col < cols:
       output_grid[right_neighbor_row, right_neighbor_col] = 1

    # fill the left neighbor of the second vertical line with blue (color 1)
    second_line = vertical_lines[1]
    left_neighbor_row = second_line[0][0]
    left_neighbor_col = second_line[0][1] - 1

    if left_neighbor_col >= 0:
       output_grid[left_neighbor_row, left_neighbor_col] = 1
    
    return output_grid