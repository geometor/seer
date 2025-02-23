import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white cells to the last row,
    maintaining their original column order.
    """
    output_grid = np.zeros_like(input_grid)
    last_row = output_grid.shape[0] - 1

    for j in range(input_grid.shape[1]):
        # Collect all non-white cells from the current column
        non_white_cells = []
        for i in range(input_grid.shape[0]):
            if input_grid[i, j] != 0:
                non_white_cells.append(input_grid[i, j])

        # Place the collected non-white cells in the last row
        for k, color in enumerate(non_white_cells):
            output_grid[last_row - len(non_white_cells) + 1 + k, j] = color

    return output_grid