"""
The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    Colored cells are moved to the last row, maintaining their order,
    and the rest of the grid is filled with white (0).
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify non-white cells and their original order.
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], r, c)) # Store color and original position

    # 2. Sort non-white cells to preserve the column-major order in the bottom row
    non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[1], x[2]))
    # non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[2], x[1]))
     
    # 3. Place the sorted non-white cells in the last row of the output grid.
    last_row_index = 0
    for cell in non_white_cells_sorted:
        output_grid[rows - 1, last_row_index] = cell[0]
        last_row_index += 1

    return output_grid.tolist()