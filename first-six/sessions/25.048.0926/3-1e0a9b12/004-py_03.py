"""
The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order based on column and then row and removing color duplicates. The remaining cells are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    Colored cells are moved to the last row, maintaining their order (column-major),
    removing duplicates, and the rest of the grid is filled with white (0).
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify non-white cells and their original order.
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], r, c)) # Store color, row, and col

    # 2. Sort non-white cells by column and then row to preserve the column-major order in the bottom row.
    non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[2], x[1]))

    # 3. Place the sorted non-white cells in the last row of the output grid, removing duplicates.
    last_row_index = 0
    used_colors = set()
    for cell in non_white_cells_sorted:
        if cell[0] not in used_colors:
            output_grid[rows - 1, last_row_index] = cell[0]
            used_colors.add(cell[0])
            last_row_index += 1
            

    return output_grid.tolist()