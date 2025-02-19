import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white cells down to the
    lowest available position in their respective columns, maintaining
    their relative vertical order.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    for c in range(cols):
        # Collect non-white cells in this column
        column_cells = []
        for r in range(rows):
            if input_grid[r, c] != 0:
                column_cells.append((r, input_grid[r, c]))

        # Place them at the bottom, maintaining order
        row_index = rows - 1
        for _, color in reversed(column_cells):  # Iterate in reverse to place from bottom up
            output_grid[row_index, c] = color
            row_index -= 1

    return output_grid