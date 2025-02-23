"""
The transformation identifies a vertical line of gray cells (value 5) in the input grid. It then analyzes the distribution of blue cells (value 1) in each row relative to this gray line. For each row, if there are more blue cells to the left of the gray line than to the right, a red cell (value 2) is placed in the leftmost column of the corresponding row in the output grid. Conversely, if there are more blue cells to the right of the gray line, a red cell is placed in the rightmost column of the corresponding row in the output grid. The output grid is always 3x3, and any cells not set to red are filled with white (value 0).
"""

import numpy as np

def find_gray_column(grid):
    # Find the column index containing gray cells (value 5).
    for j in range(grid.shape[1]):
        if np.any(grid[:, j] == 5):
            return j
    return -1

def count_blue_cells(grid, row, gray_column):
    # Count blue cells (value 1) to the left and right of the gray column in the given row.
    left_count = 0
    for j in range(gray_column):
        if grid[row, j] == 1:
            left_count += 1

    right_count = 0
    for j in range(gray_column + 1, grid.shape[1]):
        if grid[row, j] == 1:
            right_count += 1
    return left_count, right_count

def transform(input_grid):
    """
    Transforms the input grid based on the distribution of blue cells relative to a vertical gray line.
    """
    input_grid = np.array(input_grid)
    gray_column = find_gray_column(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)

    if gray_column != -1:
        for row in range(3):
            left_count, right_count = count_blue_cells(input_grid, row, gray_column)
            if left_count > right_count:
                output_grid[row, 0] = 2  # Red on the left
            elif right_count > left_count:
                output_grid[row, 2] = 2  # Red on the right
    return output_grid